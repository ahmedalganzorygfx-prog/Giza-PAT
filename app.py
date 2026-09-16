import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO

# ---------------------------------------------------------
# 1. تهيئة وإعدادات الصفحة
# ---------------------------------------------------------
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide"
)

# تطبيق أنماط التنسيق ودعم اللغة العربية (RTL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .header-box {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    }
    .metric-card {
        background-color: #f8f9fa;
        border-right: 5px solid #1e3c72;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. إدارة قاعدة البيانات (SQLite)
# ---------------------------------------------------------
DB_FILE = "giza_academy_full.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # جدول طلبات شهادات الصلاحية والخدمات
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL,
            national_id TEXT NOT NULL,
            teacher_code TEXT NOT NULL,
            administration TEXT NOT NULL,
            school TEXT NOT NULL,
            cert_type TEXT NOT NULL,
            specializations TEXT,
            status TEXT DEFAULT 'قيد المراجعة بالفرع',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # جدول مواعيد البرامج التدريبية والاختبارات بالفرع
    c.execute('''
        CREATE TABLE IF NOT EXISTS training_schedules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_name TEXT NOT NULL,
            target_group TEXT NOT NULL,
            start_date TEXT NOT NULL,
            venue TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            status TEXT DEFAULT 'متاح للحجز'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------------------------------------------------------
# 3. الدوال التخصيصية
# ---------------------------------------------------------
def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=4, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def get_connection():
    return sqlite3.connect(DB_FILE)

# ---------------------------------------------------------
# 4. الهيكل العلوي وشريط التوجيه
# ---------------------------------------------------------
st.markdown('''
    <div class="header-box">
        <h1>الأكاديمية المهنية للمعلمين - فرع الجيزة</h1>
        <p>المنصة الرقمية الموحدة لإدارة برامج الصلاحية والاعتماد والتطوير المهني</p>
    </div>
''', unsafe_allow_html=True)

# قائمة مهام الفرع الرئيسية
menu = [
    "الرئيسية والدليل الإرشادي",
    "تقديم طلب شهادة صلاحية",
    "متابعة الطلبات وتدقيق الملفات",
    "جدول البرامج التدريبية والاختبارات",
    "إحصائيات وتقارير الفرع",
    "إدارة النظام (خاص بالفرع)"
]

choice = st.sidebar.radio("مهام الفرع والخدمات", menu)

# قائمة الإدارات التعليمية بالجيزة
GIZA_ADMINS = [
    "جنوب الجيزة", "شمال الجيزة", "الدقي", "العجوزة", "العمرانية", 
    "الهرم", "بولاق الدكرور", "6 أكتوبر", "الشيخ زايد", "كرداسة", 
    "أوسيم", "منشأة القناطر", "البدرشين", "العياط", "الصف", "أتفيح"
]

# أنواع شهادات الصلاحية والخدمات بالفرع
CERT_TYPES = [
    "معلم مساعد (التثبيت)",
    "التسكين على كادر المعلمين",
    "الترقي للدرجات الأعلى",
    "تغيير المسمى الوظيفي",
    "إعادة التعيين والتسوية (قرار 160 لسنة 2024)",
    "القيادات الإشرافية (مدير/وكيل مدرسة)",
    "القيادات الإشرافية (مدير/وكيل إدارة تعليمية)",
    "القيادات الإشرافية (أساسيات التوجيه الفني)"
]

# ---------------------------------------------------------
# 5. صفحات النظام
# ---------------------------------------------------------

# 5.1 الرئيسية
if choice == "الرئيسية والدليل الإرشادي":
    st.subheader("📌 المهام الأساسية لفرع الجيزة")
    st.write("تعمل المنصة على تنفيذ مهام الفرع الخاصة بإصدار شهادات الصلاحية وتنظيم البرامج التأهيلية لجميع الفئات:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 1. الصلاحية والتثبيت\n* المعلم المساعد (مستوفاة الشروط)\n* التسكين لأول مرة على الكادر")
        st.info("### 4. المسمى الوظيفي\n* نقل التخصصات والمراحل\n* مطابقة المؤهل مع التوجيه")
    with col2:
        st.success("### 2. برامج الترقي\n* استيفاء المدة البينية (5 سنوات)\n* تقييم الملفات واختبارات الترقي")
        st.success("### 5. قرار 160 لسنة 2024\n* تسوية المؤهل الأعلى أثناء الخدمة\n* إصدار شهادات إعادة التعيين")
    with col3:
        st.warning("### 3. القيادات الإشرافية\n* الإدارة المدرسية (مدير / وكيل)\n* الإدارة التعليمية (مدير / وكيل)\n* التوجيه الفني")
        st.warning("### 6. التحقق والتوثيق\n* اصدار شهادات الصلاحية مزودة بـ QR Code\n* منع التزوير والتحقق الرقمي")

# 5.2 تقديم طلب جديد
elif choice == "تقديم طلب شهادة صلاحية":
    st.subheader("📝 التقديم لإصدار شهادة الصلاحية")
    st.caption("يرجى إدخال البيانات بدقة وفقاً لصحيفة الأحوال الإلكترونية.")

    with st.form("request_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("الاسم الرباعي كاملاً")
            nat_id = st.text_input("الرقم القومي (14 رقم)")
            code = st.text_input("كود المعلم")
        with col2:
            admin_name = st.selectbox("الإدارة التعليمية", GIZA_ADMINS)
            school = st.text_input("اسم المدرسة / جهة العمل")
            cert_type = st.selectbox("مسار شهادة الصلاحية المطلوبة", CERT_TYPES)

        spec = st.text_input("مادة التخصص الحالية / المؤهل الدراسي")
        
        st.markdown("---")
        st.write("📄 **المستندات المطلوبة (صحيفة أحوال + المؤهل + التقرير)**")
        uploaded_file = st.file_uploader("قم برفع الملفات بصيغة PDF أو صورة", type=["pdf", "png", "jpg", "jpeg"])

        submitted = st.form_submit_button("إرسال الطلب لفرع الجيزة")

        if submitted:
            if name and code and len(nat_id) == 14:
                conn = get_connection()
                c = conn.cursor()
                c.execute('''
                    INSERT INTO requests (teacher_name, national_id, teacher_code, administration, school, cert_type, specializations)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, nat_id, code, admin_name, school, cert_type, spec))
                conn.commit()
                conn.close()
                st.success(f"تم تسجيل طلبك بنجاح للأستاذ/ة: {name}. رقم الطلب المسجل محفوظ.")
            else:
                st.error("يرجى التأكد من استكمال كافة البيانات وصحة الرقم القومي (14 رقم).")

# 5.3 متابعة وتدقيق الطلبات
elif choice == "متابعة الطلبات وتدقيق الملفات":
    st.subheader("🔍 الاستعلام وتدقيق حالة الملفات")
    
    search_type = st.radio("بحث بواسطة:", ["الرقم القومي", "كود المعلم"], horizontal=True)
    search_val = st.text_input("أدخل قيمة البحث:")

    if st.button("استعلام"):
        if search_val:
            conn = get_connection()
            col_name = "national_id" if search_type == "الرقم القومي" else "teacher_code"
            df = pd.read_sql_query(f"SELECT * FROM requests WHERE {col_name} = ?", conn, params=(search_val,))
            conn.close()

            if not df.empty:
                for idx, row in df.iterrows():
                    st.markdown(f"### طلب رقم #{row['id']} - {row['cert_type']}")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write(f"**الاسم:** {row['teacher_name']}")
                        st.write(f"**كود المعلم:** {row['teacher_code']}")
                        st.write(f"**الإدارة التعليمية:** {row['administration']}")
                    with c2:
                        st.write(f"**الرقم القومي:** {row['national_id']}")
                        st.write(f"**المدرسة:** {row['school']}")
                        st.write(f"**التاريخ:** {row['created_at']}")
                    
                    status = row['status']
                    if status == "مقبول ومُعتمد (تم أصدار الشهادة)":
                        st.success(f"**حالة الطلب:** {status}")
                        # توليد كود التحقق QR
                        qr_content = f"الأكاديمية المهنية للمعلمين - فرع الجيزة\nالشهادة: {row['cert_type']}\nالاسم: {row['teacher_name']}\nالرقم القومي: {row['national_id']}\nالحالة: معتمدة"
                        qr_img = generate_qr(qr_content)
                        st.image(qr_img, width=140, caption="كود التحقق الرقمي من الشهادة")
                    elif "مرفوض" in status:
                        st.error(f"**حالة الطلب:** {status}")
                        st.info(f"**ملاحظات الفرع:** {row['notes']}")
                    else:
                        st.warning(f"**حالة الطلب:** {status}")
                    st.markdown("---")
            else:
                st.info("لم يتم العثور على أية نتائج مطابقة.")
        else:
            st.error("يرجى كتابة رمز أو رقم البحث.")

# 5.4 جدول التدريب والاختبارات
elif choice == "جدول البرامج التدريبية والاختبارات":
    st.subheader("📅 مواعيد البرامج التدريبية والاختبارات بفرع الجيزة")
    
    conn = get_connection()
    df_schedules = pd.read_sql_query("SELECT * FROM training_schedules", conn)
    conn.close()

    if not df_schedules.empty:
        st.dataframe(df_schedules, use_container_width=True)
    else:
        st.info("لا توجد مواعيد تدريبية أو اختبارات مضافة حالياً في الجدول.")

# 5.5 الإحصائيات وتقارير الفرع
elif choice == "إحصائيات وتقارير الفرع":
    st.subheader("📊 تقارير وإحصائيات أنشطة فرع الجيزة")
    
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM requests", conn)
    conn.close()

    if not df.empty:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("إجمالي الطلبات", len(df))
        m2.metric("شهادات معتمدة", len(df[df['status'].str.contains("مُعتمد", na=False)]))
        m3.metric("قيد المراجعة", len(df[df['status'].str.contains("المراجعة", na=False)]))
        m4.metric("طلبات غير مكتملة", len(df[df['status'].str.contains("مرفوض", na=False)]))

        st.markdown("---")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.write("### التوزيع حسب نوع شهادة الصلاحية")
            cert_counts = df['cert_type'].value_counts()
            st.bar_chart(cert_counts)

        with col_chart2:
            st.write("### التوزيع حسب الإدارات التعليمية")
            admin_counts = df['administration'].value_counts()
            st.bar_chart(admin_counts)
    else:
        st.info("لا توجد بيانات كافية لاستعراض الإحصائيات.")

# 5.6 لوحة تحكم أدمن الفرع
elif choice == "إدارة النظام (خاص بالفرع)":
    st.subheader("⚙️ لوحة تحكم واعتماد الطلبات - فرع الجيزة")
    
    pwd = st.text_input("كلمة مرور المسؤول (Admin)", type="password")
    if pwd == "giza2026":
        st.success("تم تسجيل الدخول بصلاحيات مدير الفرع/الإحصاء.")
        
        tab1, tab2 = st.tabs(["مراجعة واعتماد الطلبات", "إضافة برنامج تدريبي / اختبار"])
        
        with tab1:
            conn = get_connection()
            df = pd.read_sql_query("SELECT * FROM requests ORDER BY id DESC", conn)
            conn.close()

            if not df.empty:
                for idx, row in df.iterrows():
                    with st.expander(f"طلب #{row['id']}: {row['teacher_name']} ({row['cert_type']}) - الإدارة: {row['administration']}"):
                        st.write(f"**كود المعلم:** {row['teacher_code']} | **الرقم القومي:** {row['national_id']}")
                        st.write(f"**المدرسة:** {row['school']} | **التخصص/المؤهل:** {row['specializations']}")
                        
                        col_st, col_nt = st.columns([1, 2])
                        with col_st:
                            new_status = st.selectbox(
                                "تحديث الحالة", 
                                ["قيد المراجعة بالفرع", "مقبول ومُعتمد (تم أصدار الشهادة)", "مرفوض - استكمال مستندات"], 
                                key=f"st_{row['id']}"
                            )
                        with col_nt:
                            notes = st.text_input("ملاحظات الفرع", value=row['notes'] if row['notes'] else "", key=f"nt_{row['id']}")
                        
                        if st.button("حفظ التحديث", key=f"btn_{row['id']}"):
                            conn = get_connection()
                            c = conn.cursor()
                            c.execute("UPDATE requests SET status = ?, notes = ? WHERE id = ?", (new_status, notes, row['id']))
                            conn.commit()
                            conn.close()
                            st.success("تم حفظ التحديث بنجاح!")
                            st.rerun()
            else:
                st.info("لا توجد طلبات واردة حالياً.")
                
        with tab2:
            st.write("### إضافة موعد تدريب أو اختبار جديد بالفرع")
            with st.form("add_schedule"):
                prog_name = st.text_input("اسم البرنامج / الاختبار")
                target = st.selectbox("الفئة المستهدفة", CERT_TYPES)
                s_date = st.text_input("التاريخ والموعد (مثال: 25 سبتمبر 2026 - 10 صباحاً)")
                venue = st.text_input("مكان التنفيذ (مثال: قاعة التدريب بمقر الفرع)")
                cap = st.number_input("السعة الاستيعابية", min_value=1, value=50)
                
                if st.form_submit_button("إضافة للجدول"):
                    conn = get_connection()
                    c = conn.cursor()
                    c.execute('''
                        INSERT INTO training_schedules (program_name, target_group, start_date, venue, capacity)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (prog_name, target, s_date, venue, cap))
                    conn.commit()
                    conn.close()
                    st.success("تمت إضافة البرنامج التدريبي بنجاح!")
    elif pwd != "":
        st.error("كلمة المرور غير صحيحة.")
