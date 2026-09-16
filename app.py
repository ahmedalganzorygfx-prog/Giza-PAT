import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO
from PIL import Image
import os
import urllib.request
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

# ---------------------------------------------------------
# 1. تهيئة وإعدادات الصفحة والتنسيقات (Dark Mode RTL - بدون خلفية بيضاء)
# ---------------------------------------------------------
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    /* صندوق الترويسة الرئيسي */
    .header-box {
        background-color: var(--background-secondary-color, rgba(128, 128, 128, 0.12));
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
    }
    
    .main-header {
        color: var(--text-color, #1E3A8A);
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    .main-subheading {
        color: var(--text-color, #2A5298);
        opacity: 0.85;
        font-size: 16px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0px;
    }

    .section-title {
        color: var(--text-color, #1E3A8A);
        border-bottom: 3px solid #1E3A8A;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-align: right;
    }

    /* حاوية شفافية اللوجو بدون خلفيات أو إطارات */
    .transparent-logo-container {
        display: inline-block;
        margin: 0 auto 10px auto;
        max-width: 150px;
        max-height: 150px;
    }

    .transparent-logo-container img {
        width: 100%;
        height: auto;
        object-fit: contain;
        /* ظل خفيف ناصع يضمن ظهور اللوجو المفرغ على الوضع الداكن والفاتح */
        filter: drop-shadow(0px 0px 8px rgba(255, 255, 255, 0.65));
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. قائمة الإدارات التعليمية كاملة
# ---------------------------------------------------------
GIZA_ADMINISTRATIONS = [
    "أبو النمرس", "أطفيح", "أكتوبر", "أوسيم", "البدرشين", "الحوامدية", 
    "الدقى", "الديوان العام", "الشيخ زايد", "الصف", "العجوزة", "العمرانية", 
    "الهرم", "الواحات البحرية", "الوراق", "بولاق الدكرور", "جنوب الجيزة", 
    "حدائق أكتوبر", "ديوان المديرية", "شمال الجيزة", "كرداسة", "منشأة القناطر"
]

# ---------------------------------------------------------
# 3. إدارة قاعدة البيانات (SQLite)
# ---------------------------------------------------------
DB_NAME = "giza_academy_v3.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL,
            national_id TEXT NOT NULL,
            teacher_code TEXT NOT NULL,
            administration TEXT NOT NULL,
            school TEXT NOT NULL,
            cert_type TEXT NOT NULL,
            current_status TEXT DEFAULT 'قيد المراجعة بالفرع',
            attachment_poa BLOB,
            attachment_qual BLOB,
            attachment_rep BLOB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value BLOB
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def save_logo_to_db(logo_bytes):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('logo', ?)", (logo_bytes,))
    conn.commit()
    conn.close()

def get_logo_from_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key = 'logo'")
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def add_request(name, nat_id, code, admin_name, school_name, cert_type, att_poa, att_qual, att_rep):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO requests (teacher_name, national_id, teacher_code, administration, school, cert_type, attachment_poa, attachment_qual, attachment_rep)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, nat_id, code, admin_name, school_name, cert_type, att_poa, att_qual, att_rep))
    conn.commit()
    conn.close()

def get_requests():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT id, teacher_name, national_id, teacher_code, administration, school, cert_type, current_status, created_at FROM requests ORDER BY id DESC", conn)
    conn.close()
    return df

def update_status(req_id, new_status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE requests SET current_status = ? WHERE id = ?", (new_status, req_id))
    conn.commit()
    conn.close()

def get_attachments(req_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT attachment_poa, attachment_qual, attachment_rep FROM requests WHERE id = ?", (req_id,))
    attachments = c.fetchone()
    conn.close()
    return attachments

# ---------------------------------------------------------
# 4. معالج إعداد الـ PDF والـ QR Code
# ---------------------------------------------------------
FONT_PATH = "Cairo-Regular.ttf"

if not os.path.exists(FONT_PATH):
    try:
        font_url = "https://github.com/google/fonts/raw/main/ofl/cairo/Cairo-Regular.ttf"
        urllib.request.urlretrieve(font_url, FONT_PATH)
    except Exception:
        pass

if os.path.exists(FONT_PATH):
    pdfmetrics.registerFont(TTFont('Cairo', FONT_PATH))
    HAS_FONT = True
else:
    HAS_FONT = False

def format_arabic_text(text):
    if not text: return ""
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def generate_pdf(request_data):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    font_name = 'Cairo' if HAS_FONT else 'Helvetica'
    
    c.setFont(font_name, 20)
    c.drawCentredString(width/2, height - 60, format_arabic_text("الأكاديمية المهنية للمعلمين"))
    c.setFont(font_name, 16)
    c.drawCentredString(width/2, height - 90, format_arabic_text("فرع الجيزة"))
    
    c.setFont(font_name, 14)
    c.drawCentredString(width/2, height - 130, format_arabic_text("إشعار اعتماد شهادة صلاحية"))
    
    y_pos = height - 180
    c.setFont(font_name, 12)
    c.drawString(width - 80, y_pos, format_arabic_text(f"السيد/ة الأستاذ/ة: {request_data['teacher_name']}"))
    y_pos -= 30
    c.drawString(width - 80, y_pos, format_arabic_text(f"الرقم القومي: {request_data['national_id']} | كود المعلم: {request_data['teacher_code']}"))
    y_pos -= 40
    c.setFont(font_name, 14)
    c.drawCentredString(width/2, y_pos, format_arabic_text(f"شهادة الصلاحية لـ: {request_data['cert_type']}"))
    
    qr_content = f"PAT-GIZA\nName: {request_data['teacher_name']}\nID: {request_data['national_id']}\nCert: {request_data['cert_type']}"
    qr_img = generate_qr(qr_content)
    c.drawInlineImage(Image.open(BytesIO(qr_img)), width/2 - 50, 80, width=100, height=100)
    
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.getvalue()

# ---------------------------------------------------------
# 5. الترويسة واللوجو المفرغ بالكامل (بدون خلفية)
# ---------------------------------------------------------
st.markdown('<div class="header-box">', unsafe_allow_html=True)

logo_bytes = None
for fname in ['logo.png', 'logo.jpg', 'logo.jpeg', 'Logo.png', 'Logo.PNG', 'LOGO.PNG']:
    if os.path.exists(fname):
        with open(fname, "rb") as f:
            logo_bytes = f.read()
        break

if not logo_bytes:
    logo_bytes = get_logo_from_db()

if logo_bytes:
    encoded_logo = base64.b64encode(logo_bytes).decode()
    st.markdown(f'''
        <div style="text-align: center;">
            <div class="transparent-logo-container">
                <img src="data:image/png;base64,{encoded_logo}" alt="لوجو الفرع">
            </div>
        </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; margin: 0;'>🎓</h1>", unsafe_allow_html=True)

st.markdown('''
    <h1 class="main-header">الأكاديمية المهنية للمعلمين - فرع الجيزة</h1>
    <p class="main-subheading">المنصة الرقمية الموحدة لإصدار وتدقيق شهادات الصلاحية</p>
</div>
''', unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. القائمة الرئيسية والتنقل
# ---------------------------------------------------------
menu = ["الرئيسية والخدمات", "تقديم طلب شهادة صلاحية", "متابعة حالة الطلب", "لوحة تحكم الفرع (الأدمن)"]
choice = st.sidebar.radio("القائمة الرئيسية", menu)

if choice == "الرئيسية والخدمات":
    st.markdown("<h2 class='section-title'>مسارات شهادات الصلاحية المتاحة بالفرع</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 1. معلم مساعد\nإصدار شهادات الصلاحية للتعين والتثبيت على وظيفة معلم.")
        st.info("### 4. المسمى الوظيفي\nشهادات تغيير المسمى الوظيفي ونقل التخصصات.")
    with col2:
        st.success("### 2. التسكين على الكادر\nشهادات الصلاحية للتسكين لأول مرة على كادر المعلمين.")
        st.success("### 5. قرار 160 لسنة 2024\nإعادة التعيين والتسوية الوظيفية للمؤهلات الأعلى.")
    with col3:
        st.warning("### 3. الترقي\nشهادات الترقي للدرجات والوظائف الأعلى بالكادر.")
        st.warning("### 6. القيادات الإشرافية\nصلاحية ممارسة مهام الإدارة والتوجيه الفني.")

elif choice == "تقديم طلب شهادة صلاحية":
    st.markdown("<h2 class='section-title'>تقديم طلب إصدار شهادة صلاحية جديد</h2>", unsafe_allow_html=True)

    with st.form("request_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم الرباعي")
            code = st.text_input("كود المعلم")
            school = st.text_input("المدرسة / جهة العمل")
        with col2:
            nat_id = st.text_input("الرقم القومي (14 رقم)")
            admin_name = st.selectbox("الإدارة التعليمية", GIZA_ADMINISTRATIONS)
            cert_type = st.selectbox("نوع شهادة الصلاحية المطلوبة", [
                "معلم مساعد (التثبيت)", "التسكين على الكادر", "الترقي للدرجة الأعلى",
                "تغيير المسمى الوظيفي", "إعادة تعيين (قرار 160 لسنة 2024)",
                "القيادات الإشرافية (مدير/وكيل/توجيه)"
            ])
            
        st.markdown("---")
        st.subheader("المستندات المرفقة (صور)")
        uploaded_poa = st.file_uploader("صورة صحيفة الأحوال الإلكترونية", type=["png", "jpg", "jpeg"])
        uploaded_qual = st.file_uploader("صورة المؤهل الدراسي الأعلى", type=["png", "jpg", "jpeg"])
        uploaded_rep = st.file_uploader("صورة تقارير الكفاية (إن وجد)", type=["png", "jpg", "jpeg"])

        submitted = st.form_submit_button("إرسال الطلب لفرع الجيزة")
        
        if submitted:
            if name and nat_id and code and len(nat_id) == 14:
                poa_bytes = uploaded_poa.read() if uploaded_poa else None
                qual_bytes = uploaded_qual.read() if uploaded_qual else None
                rep_bytes = uploaded_rep.read() if uploaded_rep else None
                
                add_request(name, nat_id, code, admin_name, school, cert_type, poa_bytes, qual_bytes, rep_bytes)
                st.success(f"تم تسجيل طلبك بنجاح للأستاذ/ة {name}! يمكنك متابعة الطلب باستخدام الرقم القومي.")
            else:
                st.error("يرجى التأكد من كتابة البيانات الأساسية وصحة الرقم القومي (14 رقم).")

elif choice == "متابعة حالة الطلب":
    st.markdown("<h2 class='section-title'>الاستعلام عن طلب شهادة الصلاحية</h2>", unsafe_allow_html=True)
    search_nat_id = st.text_input("أدخل الرقم القومي للاستعلام")
    if st.button("بحث"):
        if search_nat_id:
            df = get_requests()
            user_reqs = df[df["national_id"] == search_nat_id]
            if not user_reqs.empty:
                for idx, row in user_reqs.iterrows():
                    st.write("---")
                    st.markdown(f"**رقم الطلب:** {row['id']} | **نوع الشهادة:** {row['cert_type']}")
                    status = row['current_status']
                    if status == "مقبول ومُعتمد":
                        st.success(f"حالة الطلب: {status}")
                        pdf_bytes = generate_pdf(row.to_dict())
                        st.download_button(
                            label="تحميل شهادة الصلاحية (PDF)",
                            data=pdf_bytes,
                            file_name=f"certificate_{row['teacher_code']}.pdf",
                            mime="application/pdf"
                        )
                    else:
                        st.warning(f"حالة الطلب: {status}")
            else:
                st.info("لم يتم العثور على طلبات مسجلة بهذا الرقم القومي.")

elif choice == "لوحة تحكم الفرع (الأدمن)":
    st.markdown("<h2 class='section-title'>إدارة ومراجعة الطلبات - فرع الجيزة</h2>", unsafe_allow_html=True)
    pwd = st.text_input("كلمة مرور أدمن الفرع", type="password")
    if pwd == "admin123":
        st.success("تم الوصول بصلاحيات الإدارة.")
        
        with st.expander("🖼️ تغيير لوجو الفرع"):
            new_logo = st.file_uploader("قم برفع اللوجو الجديد (PNG مفرغ)", type=["png", "jpg", "jpeg"])
            if st.button("حفظ اللوجو الجديد"):
                if new_logo:
                    save_logo_to_db(new_logo.read())
                    st.success("تم تحديث اللوجو بنجاح!")
                    st.rerun()

        st.markdown("---")
        df = get_requests()
        if not df.empty:
            for idx, row in df.iterrows():
                with st.expander(f"طلب #{row['id']} - {row['teacher_name']} ({row['cert_type']})"):
                    st.write(f"**كود المعلم:** {row['teacher_code']} | **الرقم القومي:** {row['national_id']} | **الإدارة:** {row['administration']}")
                    
                    attachments = get_attachments(row['id'])
                    if attachments:
                        c_img1, c_img2, c_img3 = st.columns(3)
                        with c_img1:
                            if attachments[0]: st.image(attachments[0], caption="صحيفة الأحوال")
                        with c_img2:
                            if attachments[1]: st.image(attachments[1], caption="المؤهل الدراسي")
                        with c_img3:
                            if attachments[2]: st.image(attachments[2], caption="التقارير")
                            
                    new_st = st.selectbox("تحديث الحالة", ["قيد المراجعة بالفرع", "مقبول ومُعتمد", "مرفوض"], key=f"sel_{row['id']}")
                    if st.button("حفظ التغيير", key=f"btn_{row['id']}"):
                        update_status(row['id'], new_st)
                        st.success("تم التحديث!")
                        st.rerun()
