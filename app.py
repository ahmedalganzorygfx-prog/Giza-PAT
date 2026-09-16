import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. التنسيق والظهور (CSS)
st.markdown("""
    <style>
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .top-bar {
        background-color: #0c1836;
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }
    .btn-teacher {
        background-color: #bd2227;
        color: white;
        padding: 6px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: bold;
    }
    .instruction-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border-right: 5px solid #bd2227;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر العلوي
st.markdown("""
    <div class="top-bar">
        <div>
            <a href="#" class="btn-teacher">منصة المعلم</a>
            <span style="margin-right: 20px; font-weight: 500;">الأكاديمية المهنية للمعلمين</span>
        </div>
        <div style="font-size: 1.2rem; font-weight: bold;">
            فرع الجيزة
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. التحكم بالصلاحيات عبر القائمة الجانبية
st.sidebar.header("🔐 دخول إدارة الفرع")
role = st.sidebar.radio("نوع المستخدم:", ["معلم / مستخدم عادي", "مدير النظام (Admin)"])
is_admin = (role == "مدير النظام (Admin)")

if is_admin:
    st.sidebar.success("تم تفعيل صلاحيات الأدمن (التنزيل والتحميل متاح)")
else:
    st.sidebar.info("صلاحيات التنزيل واستخراج الملفات مخصصة للأدمن فقط")

# 5. التبويبات الرئيسية استناداً إلى البرامج والمجلدات
tab_home, tab_certs, tab_exam_app, tab_stats, tab_jobs, tab_assistant, tab_attendance = st.tabs([
    "🏠 الرئيسية",
    "📜 Academy Certificates",
    "💻 ExamApp",
    "📊 إحصائيات مسمي وظيفي 2026",
    "📝 اختبارات الوظائف الإشرافية",
    "📂 ملفات المعلم المساعد",
    "⏱️ نظام الحضور"
])

# --- التبويب الأول: الرئيسية ---
with tab_home:
    st.markdown("""
        <div class="instruction-card">
            <h4 style="color: #bd2227; margin-bottom: 10px;">الخدمات الرقمية لفرع الجيزة - إرشادات التشغيل:</h4>
            <ul style="line-height: 1.8; color: #333;">
                <li>الدخول على الخدمات من جهاز PC ومتصفح حديث الإصدار Google Chrome.</li>
                <li>التأكد من كتابة الرقم القومي وكود المعلم بطريقة صحيحة بالأرقام الإنجليزية.</li>
                <li>الالتزام بالمواعيد المحددة لأداء الخدمات والرجوع لإدارة الفرع عند الحاجة.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    st.info("قم باختيار البرنامج المطلوب من التبويبات أعلاه لبدء استخدام المنصة.")

# --- 1. برنامج Academy Certificates ---
with tab_certs:
    st.subheader("📜 برنامج الشهادات (Academy Certificates)")
    search_code = st.text_input("بحث برقم القومي / كود المعلم:", key="cert_search")
    
    if st.button("استعلام عن الشهادة"):
        st.success("تم العثور على الشهادة المطلوبة.")
        st.write("بيانات الشهادة: **معتمدة من فرع الجيزة**")

    if is_admin:
        st.download_button(
            label="📥 تنزيل الشهادة (PDF)",
            data="محتوى الشهادة",
            file_name="certificate.pdf",
            mime="application/pdf"
        )

# --- 2. برنامج ExamApp ---
with tab_exam_app:
    st.subheader("💻 تطبيق الاختبارات الرقمية (ExamApp)")
    st.write("بوابة إجراء الاختبارات وتوثيق النتائج لمرشحي الفرع.")
    if st.button("تشغيل جلسة الاختبار"):
        st.info("جاري إعداد بيئة الاختبار الرقمي...")

# --- 3. برنامج إحصائيات مسمي وظيفي 2026 ---
with tab_stats:
    st.subheader("📊 إحصائيات مسمي وظيفي 2026")
    df_stats = pd.DataFrame({
        "المسمى الوظيفي": ["معلم", "معلم أول", "معلم أول أ", "معلم خبير", "معلم كبير"],
        "عدد المستهدفين بالفرع": [1200, 850, 640, 410, 190],
        "نسبة الإنجاز": ["95%", "90%", "88%", "92%", "98%"]
    })
    st.dataframe(df_stats, width="stretch", hide_index=True)
    
    if is_admin:
        st.download_button(
            label="📥 تصدير تقرير الإحصائيات (Excel)",
            data=df_stats.to_csv(index=False).encode('utf-8-sig'),
            file_name="job_title_stats_2026.csv",
            mime="text/csv"
        )

# --- 4. برنامج استكمال اختبارات الوظائف الاشرافية والمعلم المساعد ---
with tab_jobs:
    st.subheader("📝 استكمال اختبارات الوظائف الإشرافية والمعلم المساعد")
    st.text_input("رقم الملف / كود المتقدم:", key="jobs_search")
    st.selectbox("نوع الوظيفة المتقدم لها:", ["مدير مدرية / إدارة", "وكيل مدرية / إدارة", "موجه فني", "معلم مساعد"])
    st.button("تسجيل استكمال البيانات")

# --- 5. برنامج ملفات المعلم المساعد ---
with tab_assistant:
    st.subheader("📂 ملفات المعلم المساعد")
    st.write("نظام فحص وتدقيق صحة المستندات الخاصة بالمعلمين المساعدين.")
    
    uploaded_file = st.file_uploader("رفع مسح ضوئي لملف المتقدم (PDF):", type=["pdf", "png", "jpg"])
    if uploaded_file and is_admin:
        st.success(f"تم رفع الملف: {uploaded_file.name} بنجاح.")

# --- 6. برنامج نظام الحضور ---
with tab_attendance:
    st.subheader("⏱️ نظام الحضور والانصراف التدريبي")
    st.date_input("تاريخ اليوم التدريبي:")
    st.time_input("ساعة تسجيل الحضور:")
    st.button("تأكيد تسجيل الحضور")
    
    if is_admin:
        st.download_button(
            label="📥 تنزيل كشف الحضور اليومي (Excel)",
            data="كشف الحضور والغياب",
            file_name="attendance_report.csv",
            mime="text/csv"
        )
