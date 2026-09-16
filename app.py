import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. رابط Google Sheets الخاص بك (رابط التصدير المباشر CSV)
SHEET_CERTS_URL = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/export?format=csv&gid=0"

@st.cache_data(ttl=60)
def load_live_data(url):
    try:
        return pd.read_csv(url)
    except Exception:
        # بيانات افتراضية في حال التعثر
        return pd.DataFrame({
            "كود المعلم": ["123456", "654321"],
            "الاسم": ["أحمد محمود", "سارة إبراهيم"],
            "البرنامج": ["تطبيقات الذكاء الاصطناعي", "اختبارات الوظائف الإشرافية"],
            "حالة الشهادة": ["معتمدة وجاهزة", "قيد المراجعة"]
        })

# 3. تنسيق الواجهة (CSS)
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

# 4. الترويسة الهيدر
st.markdown("""
    <div class="top-bar">
        <div>
            <a href="#" class="btn-teacher">منصة المعلم</a>
            <span style="margin-right: 20px; font-weight: 500;">الأكاديمية المهنية للمعلمين</span>
        </div>
        <div style="font-size: 1.2rem; font-weight: bold;">فرع الجيزة</div>
    </div>
""", unsafe_allow_html=True)

# 5. إدارة الصلاحيات في القائمة الجانبية
st.sidebar.header("🔐 دخول إدارة الفرع")
role = st.sidebar.radio("نوع المستخدم:", ["معلم / مستخدم عادي", "مدير النظام (Admin)"])
is_admin = (role == "مدير النظام (Admin)")

if st.sidebar.button("🔄 تحديث البيانات الآن"):
    st.cache_data.clear()
    st.sidebar.success("تم إعادة تنشيط البيانات المباشرة!")

if is_admin:
    st.sidebar.success("صلاحيات الأدمن مفعلة (التحميل متاح)")
else:
    st.sidebar.info("صلاحيات التنزيل مخصصة للمدير فقط")

# 6. التبويبات الرئيسية لبرامج الفرع
tab_home, tab_certs, tab_exam, tab_stats, tab_jobs, tab_assistant, tab_attendance = st.tabs([
    "🏠 الرئيسية",
    "📜 Academy Certificates",
    "💻 ExamApp",
    "📊 إحصائيات مسمي وظيفي 2026",
    "📝 اختبارات الوظائف الإشرافية",
    "📂 ملفات المعلم المساعد",
    "⏱️ نظام الحضور"
])

df_certs = load_live_data(SHEET_CERTS_URL)

# --- الرئيسية ---
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

# --- 1. Academy Certificates ---
with tab_certs:
    st.subheader("📜 الاستعلام المباشر عن الشهادات")
    code = st.text_input("أدخل كود المعلم أو الرقم القومي:")
    if st.button("استعلام"):
        if code:
            df_certs['كود المعلم'] = df_certs['كود المعلم'].astype(str)
            match = df_certs[df_certs['كود المعلم'] == code.strip()]
            if not match.empty:
                row = match.iloc[0]
                st.success(f"الاسم: **{row.get('الاسم', '')}**")
                st.write(f"البرنامج: **{row.get('البرنامج', '')}**")
                st.write(f"حالة الشهادة: **{row.get('حالة الشهادة', '')}**")
                if is_admin:
                    st.download_button("📥 تنزيل النتيجة (Excel)", data=match.to_csv(index=False).encode('utf-8-sig'), file_name="cert.csv")
            else:
                st.error("لم يتم العثور على بيانات المتقدم.")

# --- 2. ExamApp ---
with tab_exam:
    st.subheader("💻 تطبيق الاختبارات الرقمية (ExamApp)")
    st.info("منصة متابعة جلسات الاختبارات الخاصة بالفرع.")

# --- 3. إحصائيات 2026 ---
with tab_stats:
    st.subheader("📊 إحصائيات مسمي وظيفي 2026")
    st.dataframe(df_certs, width="stretch", hide_index=True)
    if is_admin:
        st.download_button("📥 تنزيل الكشف الكامل", data=df_certs.to_csv(index=False).encode('utf-8-sig'), file_name="stats_2026.csv")

# --- 4. الوظائف الإشرافية ---
with tab_jobs:
    st.subheader("📝 استكمال اختبارات الوظائف الإشرافية")
    st.text_input("رقم الملف / الكود:")
    st.button("حفظ واستكمال")

# --- 5. المعلم المساعد ---
with tab_assistant:
    st.subheader("📂 ملفات المعلم المساعد")
    st.file_uploader("رفع مستندات المعلم المساعد (PDF):", type=["pdf"])

# --- 6. نظام الحضور ---
with tab_attendance:
    st.subheader("⏱️ نظام الحضور والانصراف")
    st.date_input("تاريخ اليوم التدريبي:")
    st.button("تسجيل الحضور")
