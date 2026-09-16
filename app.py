import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO
from PIL import Image

# ---------------------------------------------------------
# 1. إعدادات الصفحة والأنماط
# ---------------------------------------------------------
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide"
)

# تخصيص الاتجاه من اليمين إلى اليسار وتنسيق الأزرار والواجهة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .main-header {
        background-color: #1E3A8A;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
    }
    .sub-header {
        color: #1E3A8A;
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. إدارة قاعدة البيانات (SQLite)
# ---------------------------------------------------------
def init_db():
    conn = sqlite3.connect("giza_academy.db")
    c = conn.cursor()
    # جدول طلبات شهادات الصلاحية
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL,
            national_id TEXT NOT NULL,
            teacher_code TEXT NOT NULL,
            administration TEXT NOT NULL,
            school TEXT NOT NULL,
            cert_type TEXT NOT NULL,
            status TEXT DEFAULT 'قيد المراجعة',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def add_request(name, nat_id, code, admin_name, school_name, cert_type):
    conn = sqlite3.connect("giza_academy.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO requests (teacher_name, national_id, teacher_code, administration, school, cert_type)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, nat_id, code, admin_name, school_name, cert_type))
    conn.commit()
    conn.close()

def get_requests():
    conn = sqlite3.connect("giza_academy.db")
    df = pd.read_sql_query("SELECT * FROM requests ORDER BY id DESC", conn)
    conn.close()
    return df

def update_status(req_id, new_status):
    conn = sqlite3.connect("giza_academy.db")
    c = conn.cursor()
    c.execute("UPDATE requests SET status = ? WHERE id = ?", (new_status, req_id))
    conn.commit()
    conn.close()

# ---------------------------------------------------------
# 3. دالة إنشاء QR Code
# ---------------------------------------------------------
def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# ---------------------------------------------------------
# 4. الواجهة الرئيسية وشريط التنقل
# ---------------------------------------------------------
st.markdown('''
    <div class="main-header">
        <h1>الأكاديمية المهنية للمعلمين - فرع الجيزة</h1>
        <p>المنصة الرقمية لإصدار وتدقيق شهادات الصلاحية للخدمات والمسارات المهنية</p>
    </div>
''', unsafe_allow_html=True)

menu = ["الرئيسية والخدمات", "تقديم طلب شهادة صلاحية", "متابعة حالة الطلب", "لوحة تحكم الفرع (الأدمن)"]
choice = st.sidebar.radio("القائمة الرئيسية", menu)

# ---------------------------------------------------------
# 5. صفحة الرئيسية والخدمات
# ---------------------------------------------------------
if choice == "الرئيسية والخدمات":
    st.markdown("<h2 class='sub-header'>مسارات شهادات الصلاحية المتاحة بالفرع</h2>", unsafe_allow_html=True)
    st.write("تقدم المنصة خدمة تقديم واستخراج شهادات الصلاحية المعتمدة للمسارات التالية:")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 1. معلم مساعد\nإصدار شهادات الصلاحية للتعين والتثبيت على وظيفة معلم.")
        st.info("### 4. المسمى الوظيفي\nشهادات تغيير المسمى الوظيفي ونقل التخصصات.")

    with col2:
        st.success("### 2. التسكين على الكادر\nشهادات الصلاحية للتسكين لأول مرة على كادر المعلمين.")
        st.success("### 5. قرار 160 لسنة 2024\nإعادة التعيين والتسوية للحاصلين على مؤهلات أعلى.")

    with col3:
        st.warning("### 3. الترقي\nشهادات الترقي للدرجات والوظائف الأعلى.")
        st.warning("### 6. القيادات الإشرافية\nصلاحية ممارسة مهام (مدير/وكيل مدرسة - مدير/وكيل إدارة - توجيه فني).")

# ---------------------------------------------------------
# 6. صفحة تقديم طلب جديد
# ---------------------------------------------------------
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
        st.subheader("المستندات المرفقة")
        uploaded_file = st.file_buffer = st.file_uploader("يرجى رفع ملفات التقديم (صحيفة الأحوال + المؤهل + التقارير) في ملف PDF أو صورة", type=["pdf", "png", "jpg", "jpeg"])

        submitted = st.form_submit_button("إرسال الطلب للفرع")
        
        if submitted:
            if name and nat_id and code and len(nat_id) == 14:
                add_request(name, nat_id, code, admin_name, school, cert_type)
                st.success(f"تم تسجيل طلبك بنجاح يا أستاذ/ة {name}! يمكنك متابعة الطلب باستخدام الرقم القومي.")
            else:
                st.error("يرجى ملء جميع البيانات بشكل صحيح وتأكد من أن الرقم القومي مكون من 14 رقم.")

# ---------------------------------------------------------
# 7. صفحة متابعة حالة الطلب للمعلم
# ---------------------------------------------------------
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
                    
                    status = row['status']
                    if status == "مقبول ومُعتمد":
                        st.success(f"حالة الطلب: {status}")
                        # توليد كود الـ QR للمصادقة
                        qr_data = f"PAT-GIZA CERTIFICATE\nName: {row['teacher_name']}\nID: {row['national_id']}\nType: {row['cert_type']}\nStatus: Certified"
                        qr_img = generate_qr(qr_data)
                        
                        col_a, col_b = st.columns([1, 2])
                        with col_a:
                            st.image(qr_img, width=150, caption="رمز التحقق الرقمي QR Code")
                        with col_b:
                            st.info("تهانينا! تم اعتماد شهادة الصلاحية الخاصة بك من فرع الجيزة. يمكنك مراجعة الفرع لاستلام الشهادة الورقية أو طباعة إشعار الاعتماد.")
                    elif status == "مرفوض":
                        st.error(f"حالة الطلب: {status} (يرجى مراجعة الفرع لتحديث المستندات)")
                    else:
                        st.warning(f"حالة الطلب: {status}")
            else:
                st.info("لم يتم العثور على طلبات مسجلة بهذا الرقم القومي.")
        else:
            st.error("يرجى كتابة الرقم القومي أولاً.")

# ---------------------------------------------------------
# 8. لوحة تحكم الفرع (الأدمن)
# ---------------------------------------------------------
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
            m2.metric("قيد المراجعة", len(df[df['status'] == 'قيد المراجعة']))
            m3.metric("تمت الموافقة والاعتماد", len(df[df['status'] == 'مقبول ومُعتمد']))
            
            st.markdown("---")
            st.subheader("قائمة الطلبات المسجلة")
            
            # جدول التعديل المباشر
            for idx, row in df.iterrows():
                with st.expander(f"طلب رقم {row['id']} - {row['teacher_name']} ({row['cert_type']})"):
                    st.write(f"**الاسم:** {row['teacher_name']} | **كود المعلم:** {row['teacher_code']}")
                    st.write(f"**الرقم القومي:** {row['national_id']} | **الإدارة:** {row['administration']}")
                    st.write(f"**المدرسة:** {row['school']}")
                    st.write(f"**الحالة الحالية:** {row['status']}")
                    
                    new_st = st.selectbox(f"تحديث حالة الطلب #{row['id']}", ["قيد المراجعة", "مقبول ومُعتمد", "مرفوض - مستندات غير مكتملة"], key=f"sel_{row['id']}")
                    if st.button(f"حفظ التغيير #{row['id']}"):
                        update_status(row['id'], new_st)
                        st.success("تم تحديث الحالة بنجاح!")
                        st.rerun()
        else:
            st.info("لا توجد طلبات مسجلة حالياً.")
    elif pwd != "":
        st.error("كلمة المرور غير صحيحة.")
