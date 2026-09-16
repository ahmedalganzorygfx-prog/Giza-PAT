import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO
from PIL import Image

# ########################################################
# 1. تهيئة وإعدادات الصفحة (تم التحديث لإضافة اللوجو)
# ########################################################
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide"
)

# تخصيص الاتجاه من اليمين إلى اليسار وتنسيق الأزرار والواجهة مع توسيع منطقة العنوان للوجو
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .header-box {
        background-color: #f0f2f6; /* لون خلفية فاتح لمنطقة الشعار والعنوان */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    .main-header {
        color: #1E3A8A;
        text-align: center;
        margin-top: 10px; /* مسافة بين اللوجو والعنوان */
        margin-bottom: 0px;
    }
    .sub-header {
        color: #1E3A8A;
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    .logo-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 150px; /* التحكم في حجم اللوجو */
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. إدارة قاعدة البيانات (SQLite)
# ---------------------------------------------------------
# تم تحديث اسم قاعدة البيانات لاستيعاب المرفقات الإضافية
def init_db():
    conn = sqlite3.connect("giza_academy_v3.db")
    c = conn.cursor()
    # جدول طلبات شهادات الصلاحية مع توسيع حقول المرفقات
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
            attachment_poa BLOB, -- مرفق صحيفة الأحوال
            attachment_qual BLOB, -- مرفق المؤهل الدراسي
            attachment_rep BLOB, -- مرفق التقارير
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# دالة لإضافة طلب جديد مع المرفقات
def add_request(name, nat_id, code, admin_name, school_name, cert_type, att_poa, att_qual, att_rep):
    conn = sqlite3.connect("giza_academy_v3.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO requests (teacher_name, national_id, teacher_code, administration, school, cert_type, attachment_poa, attachment_qual, attachment_rep)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, nat_id, code, admin_name, school_name, cert_type, att_poa, att_qual, att_rep))
    conn.commit()
    conn.close()

# دالة للحصول على جميع الطلبات
def get_requests():
    conn = sqlite3.connect("giza_academy_v3.db")
    df = pd.read_sql_query("SELECT id, teacher_name, national_id, teacher_code, administration, school, cert_type, current_status, created_at FROM requests ORDER BY id DESC", conn)
    conn.close()
    return df

# دالة لتحديث حالة الطلب
def update_status(req_id, new_status):
    conn = sqlite3.connect("giza_academy_v3.db")
    c = conn.cursor()
    c.execute("UPDATE requests SET current_status = ? WHERE id = ?", (new_status, req_id))
    conn.commit()
    conn.close()

# دالة للحصول على مرفقات طلب محدد
def get_attachments(req_id):
    conn = sqlite3.connect("giza_academy_v3.db")
    c = conn.cursor()
    c.execute("SELECT attachment_poa, attachment_qual, attachment_rep FROM requests WHERE id = ?", (req_id,))
    attachments = c.fetchone()
    conn.close()
    return attachments

# ########################################################
# 3. معالج إعداد الـ PDF الـ QR Code
# ########################################################
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

# تحميل خط يدعم اللغة العربية لتوليد الـ PDF
# ملاحظة: يجب أن يتوفر ملف خط عربي (مثل Cairo-Regular.ttf) في نفس مجلد التطبيق
try:
    pdfmetrics.registerFont(TTFont('Cairo', 'Cairo-Regular.ttf'))
except Exception as e:
    st.sidebar.error(f"تحذير: لم يتم العثور على ملف الخط 'Cairo-Regular.ttf'. قد تظهر النصوص العربية بشكل غير صحيح في الـ PDF. {e}")

# دالة لتنسيق النصوص العربية للـ PDF
def format_arabic_text(text):
    if not text: return ""
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

# دالة إنشاء كود QR
def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# دالة توليد ملف الـ PDF لشهادة الصلاحية
def generate_pdf(request_data):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4
    
    # تنسيق الـ PDF (الترويسة)
    c.setFont('Cairo', 22)
    c.drawCentredString(width/2, height - 60, format_arabic_text("الأكاديمية المهنية للمعلمين"))
    c.setFont('Cairo', 18)
    c.drawCentredString(width/2, height - 90, format_arabic_text("فرع الجيزة"))
    
    # تنسيق نص الشهادة
    c.setFont('Cairo', 14)
    c.drawCentredString(width/2, height - 130, format_arabic_text("إشعار اعتماد شهادة صلاحية"))
    
    # بيانات المعلم
    c.setFont('Cairo', 12)
    y_pos = height - 170
    c.drawString(width - 80, y_pos, format_arabic_text(f"تشهد الأكاديمية المهنية للمعلمين - فرع الجيزة بأن:"))
    y_pos -= 30
    c.drawString(width - 120, y_pos, format_arabic_text(f"السيد/ة الأستاذ/ة: {request_data['teacher_name']}"))
    y_pos -= 25
    c.drawString(width - 120, y_pos, format_arabic_text(f"الرقم القومي: {request_data['national_id']}"))
    y_pos -= 25
    c.drawString(width - 120, y_pos, format_arabic_text(f"كود المعلم: {request_data['teacher_code']}"))
    y_pos -= 40
    c.setFont('Cairo', 14)
    c.drawCentredString(width/2, y_pos, format_arabic_text(f"قد استوفى كافة متطلبات الحصول على:"))
    y_pos -= 30
    c.setFont('Cairo', 16)
    c.drawCentredString(width/2, y_pos, format_arabic_text(f"شهادة الصلاحية لـ ({request_data['cert_type']})"))
    
    y_pos -= 50
    c.setFont('Cairo', 12)
    c.drawString(width - 80, y_pos, format_arabic_text(f"وذلك بعد اجتياز البرامج التدريبية والاختبارات المقررة."))
    
    # كود الـ QR
    qr_content = f"الأكاديمية المهنية للمعلمين\nفرع الجيزة\nالشهادة: {request_data['cert_type']}\nالاسم: {request_data['teacher_name']}\nالرقم القومي: {request_data['national_id']}\nتاريخ الاعتماد: {request_data['created_at'].split()[0]}"
    qr_img = generate_qr(qr_content)
    # رسم كود الـ QR في الـ PDF
    c.drawInlineImage(Image.open(BytesIO(qr_img)), width - 150, 80, width=100, height=100)
    
    # التذييل
    y_pos = height - 50
    c.setFont('Cairo', 10)
    c.drawString(width - 80, 50, format_arabic_text(f"مدير فرع الجيزة"))
    
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.getvalue()

# ########################################################
# 4. الواجهة الرئيسية وشريط التنقل (تم تحديث منطقة الترويسة)
# ########################################################
# تم استخدام div جديد لتحتوي على اللوجو والعنوان معاً
st.markdown('<div class="header-box">', unsafe_allow_html=True)

# استدعاء وعرض اللوجو أولاً (يجب وضع ملف باسم logo.png في نفس المجلد)
try:
    logo = Image.open('logo.png')
    st.image(logo, use_column_width=False, caption="", output_format="PNG", width=150)
    # لضمان توسيط اللوجو بدقة، سنستخدم class للـ div الذي يحتوي على الصورة
    st.markdown('<style> .element-container img { display: block; margin-left: auto; margin-right: auto; } </style>', unsafe_allow_html=True)
except Exception as e:
    st.sidebar.error("خطأ: لم يتم العثور على ملف الشعار 'logo.png'. يرجى وضعه في مجلد المشروع.")

# عرض العناوين داخل الـ div
st.markdown('''
        <h1 class="main-header">الأكاديمية المهنية للمعلمين - فرع الجيزة</h1>
        <p style="text-align: center; color: #1E3A8A; font-weight: bold;">المنصة الرقمية لإصدار وتدقيق شهادات الصلاحية للخدمات والمسارات المهنية</p>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # إغلاق div الـ header-box


menu = ["الرئيسية والخدمات", "تقديم طلب شهادة صلاحية", "متابعة حالة الطلب", "لوحة تحكم الفرع (الأدمن)"]
choice = st.sidebar.radio("القائمة الرئيسية", menu)

# ########################################################
# 5. صفحة الرئيسية والخدمات
# ########################################################
if choice == "الرئيسية والخدمات":
    st.markdown("<h2 class='sub-header'>مسارات شهادات الصلاحية المتاحة بالفرع</h2>", unsafe_allow_html=True)
    st.write(" تقدم المنصة خدمة تقديم واستخراج شهادات الصلاحية المعتمدة (في شكل ملف PDF مزود بـ QR Code للتحقق) للمسارات المهنية الستة التالية:")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 1. معلم مساعد\nإصدار شهادات الصلاحية للتعين والتثبيت على وظيفة معلم.")
        st.info("### 4. المسمى الوظيفي\nشهادات تغيير المسمى الوظيفي ونقل التخصصات بين المراحل والمواد.")

    with col2:
        st.success("### 2. التسكين على الكادر\nشهادات الصلاحية للتسكين لأول مرة على كادر المعلمين لشاغلي وظائف المعلمين.")
        st.success("### 5. قرار 160 لسنة 2024\nإعادة التعيين والتسوية الوظيفية للحاصلين على مؤهلات أعلى أثناء الخدمة.")

    with col3:
        st.warning("### 3. الترقي\nشهادات الترقي للدرجات والوظائف الأعلى بالكادر (معلم أول، معلم أول أ، معلم خبير، كبير معلمين).")
        st.warning("### 6. القيادات الإشرافية\nصلاحية ممارسة مهام (مدير/وكيل مدرسة - مدير/وكيل إدارة تعليمية - التوجيه الفني).")

# ########################################################
# 6. صفحة تقديم طلب جديد (تم توسيع جدول المرفقات)
# ########################################################
elif choice == "تقديم طلب شهادة صلاحية":
    st.markdown("<h2 class='sub-header'>تقديم طلب إصدار شهادة صلاحية جديد</h2>", unsafe_allow_html=True)

    with st.form("request_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم الرباعي")
            code = st.text_input("كود المعلم")
            school = st.text_input("المدرسة")
        with col2:
            nat_id = st.text_input("الرقم القومي (14 رقم)")
            admin_name = st.selectbox("الإدارة التعليمية", [
                "إدارة جنوب الجيزة", "إدارة شمال الجيزة", "إدارة الدقي", 
                "إدارة العجوزة", "إدارة العمرانية", "إدارة الهرم", 
                "إدارة 6 أكتوبر", "إدارة الشيخ زايد", "إدارة كرداسة", 
                "إدارة أوسيم", "إدارة البدرشين", "إدارة العياط", "إدارات أخرى"
            ])
            cert_type = st.selectbox("نوع شهادة الصلاحية المطلوبة", [
                "معلم مساعد (التثبيت)",
                "التسكين على الكادر",
                "الترقي للدرجة الأعلى",
                "تغيير المسمى الوظيفي",
                "إعادة تعيين (قرار 160 لسنة 2024)",
                "القيادات الإشرافية (مدير/وكيل/توجيه)"
            ])
            
        st.markdown("---")
        # ####### توسيع جدول المرفقات ########
        st.subheader("المستندات المرفقة المطلوبة (صور)")
        
        # مرفق صحيفة الأحوال
        uploaded_poa = st.file_uploader("يرجى رفع صورة صحيفة الأحوال الإلكترونية", type=["png", "jpg", "jpeg"])
        # مرفق المؤهل الدراسي
        uploaded_qual = st.file_uploader("يرجى رفع صورة المؤهل الدراسي الأعلى الحاصل عليه", type=["png", "jpg", "jpeg"])
        # مرفق التقارير
        uploaded_rep = st.file_uploader("يرجى رفع صورة تقرير الكفاية لآخر عامين (إن وجد)", type=["png", "jpg", "jpeg"])

        submitted = st.form_submit_button("إرسال الطلب للفرع")
        
        if submitted:
            if name and nat_id and code and len(nat_id) == 14 and uploaded_poa and uploaded_qual:
                # تحويل الملفات المرفوعة إلى بيانات باينري للتخزين في SQLite
                poa_bytes = uploaded_poa.read()
                qual_bytes = uploaded_qual.read()
                rep_bytes = uploaded_rep.read() if uploaded_rep else None # مرفق التقارير اختياري في هذه المرحلة
                
                # إضافة الطلب مع المرفقات إلى قاعدة البيانات
                add_request(name, nat_id, code, admin_name, school, cert_type, poa_bytes, qual_bytes, rep_bytes)
                st.success(f"تم تسجيل طلبك بنجاح للأستاذ/ة {name}! يمكنك متابعة حالة الطلب باستخدام الرقم القومي.")
            else:
                st.error("يرجى ملء جميع البيانات الأساسية، وصحة الرقم القومي (14 رقم)، ورفع صحيفة الأحوال والمؤهل الدراسي على الأقل.")

# ########################################################
# 7. صفحة متابعة حالة الطلب للمعلم (تم دمج تحميل الـ PDF)
# ########################################################
elif choice == "متابعة حالة الطلب":
    st.markdown("<h2 class='sub-header'>الاستعلام عن طلب شهادة الصلاحية</h2>", unsafe_allow_html=True)
    
    search_nat_id = st.text_input("أدخل الرقم القومي للاستعلام")
    if st.button("بحث"):
        if search_nat_id:
            df = get_requests()
            user_reqs = df[df["national_id"] == search_nat_id]
            
            if not user_reqs.empty:
                for idx, row in user_reqs.iterrows():
                    st.write("---")
                    st.markdown(f"**رقم الطلب:** {row['id']}")
                    st.markdown(f"**نوع الشهادة:** {row['cert_type']}")
                    st.markdown(f"**تاريخ التقديم:** {row['created_at']}")
                    
                    status = row['current_status']
                    if status == "مقبول ومُعتمد":
                        st.success(f"حالة الطلب: {status}")
                        
                        # توليد ملف الـ PDF للشهادة المعتمدة
                        pdf_bytes = generate_pdf(row.to_dict())
                        
                        st.write("تهانينا! تم اعتماد شهادة الصلاحية الخاصة بك من فرع الجيزة. يمكنك تحميل وطباعة إشعار الاعتماد الرسمي.")
                        
                        # زر تحميل الـ PDF
                        st.download_button(
                            label="تحميل شهادة الصلاحية (PDF)",
                            data=pdf_bytes,
                            file_name=f"certificate_{row['teacher_code']}.pdf",
                            mime="application/pdf",
                            key=f"dl_{row['id']}"
                        )
                    elif status == "مرفوض":
                        st.error(f"حالة الطلب: {status} (يرجى مراجعة الفرع لاستكمال الملف)")
                    else:
                        st.warning(f"حالة الطلب: {status}")
            else:
                st.info("لم يتم العثور على طلبات مسجلة بهذا الرقم القومي.")
        else:
            st.error("يرجى كتابة الرقم القومي أولاً.")

# ########################################################
# 8. لوحة تحكم الفرع (الأدمن) - تم دمج عرض المرفقات
# ########################################################
elif choice == "لوحة تحكم الفرع (الأدمن)":
    st.markdown("<h2 class='sub-header'>إدارة ومراجعة الطلبات - فرع الجيزة</h2>", unsafe_allow_html=True)
    
    pwd = st.text_input("كلمة مرور أدمن الفرع", type="password")
    if pwd == "admin123": # كلمة مرور افتراضية للتجربة
        st.success("تم الوصول بصلاحيات الإدارة.")
        
        df = get_requests()
        if not df.empty:
            st.subheader("إحصائيات سريعة")
            m1, m2, m3 = st.columns(3)
            m1.metric("إجمالي الطلبات", len(df))
            m2.metric("قيد المراجعة بالفرع", len(df[df['current_status'] == 'قيد المراجعة بالفرع']))
            m3.metric("تمت الموافقة والاعتماد", len(df[df['current_status'] == 'مقبول ومُعتمد']))
            
            st.markdown("---")
            st.subheader("قائمة الطلبات المسجلة للمراجعة")
            
            # جدول التعديل المباشر
            for idx, row in df.iterrows():
                with st.expander(f"طلب رقم {row['id']} - الأستاذ/ة {row['teacher_name']} ({row['cert_type']})"):
                    st.write(f"**الاسم:** {row['teacher_name']} | **كود المعلم:** {row['teacher_code']}")
                    st.write(f"**الرقم القومي:** {row['national_id']} | **الإدارة:** {row['administration']}")
                    st.write(f"**المدرسة:** {row['school']} | **تاريخ التقديم:** {row['created_at']}")
                    st.write(f"**الحالة الحالية:** {row['current_status']}")
                    
                    st.markdown("#### المستندات المرفقة:")
                    attachments = get_attachments(row['id'])
                    
                    if attachments:
                        # عرض مرفق صحيفة الأحوال
                        if attachments[0]:
                            try:
                                poa_img = Image.open(BytesIO(attachments[0]))
                                st.image(poa_img, caption="صحيفة الأحوال الإلكترونية", width=250)
                            except:
                                st.write("صورة صحيفة الأحوال غير صالحة.")
                        else:
                            st.write("لا يوجد ملف صحيفة أحوال مرفق.")
                        
                        # عرض مرفق المؤهل الدراسي
                        if attachments[1]:
                            try:
                                qual_img = Image.open(BytesIO(attachments[1]))
                                st.image(qual_img, caption="المؤهل الدراسي الأعلى", width=250)
                            except:
                                st.write("صورة المؤهل الدراسي غير صالحة.")
                        else:
                            st.write("لا يوجد ملف مؤهل دراسي مرفق.")
                            
                        # عرض مرفق التقارير
                        if attachments[2]:
                            try:
                                rep_img = Image.open(BytesIO(attachments[2]))
                                st.image(rep_img, caption="تقارير الكفاية", width=250)
                            except:
                                st.write("صورة تقارير الكفاية غير صالحة.")
                        else:
                            st.write("لا يوجد ملف تقارير مرفق (اختياري).")

                    st.markdown("---")
                    
                    # تحديث الحالة
                    new_st = st.selectbox(f"تحديث حالة الطلب #{row['id']}", ["قيد المراجعة بالفرع", "مقبول ومُعتمد", "مرفوض"], key=f"sel_{row['id']}")
                    if st.button(f"حفظ التغيير #{row['id']}"):
                        update_status(row['id'], new_st)
                        st.success("تم تحديث حالة الطلب بنجاح!")
                        st.rerun()
        else:
            st.info("لا توجد طلبات مسجلة مسبقاً.")
    elif pwd != "":
        st.error("كلمة المرور غير صحيحة.")
