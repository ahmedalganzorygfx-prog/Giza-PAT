import streamlit as st
import os

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - منصة الفرع",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# قائمة الإدارات التعليمية لمحافظة الجيزة
EDARAT_LIST = [
    "أبو النمرس", "أطفيح", "أكتوبر", "أوسيم", "البدرشين", "الحوامدية", 
    "الدقى", "الديوان العام", "الشيخ زايد", "الصف", "العجوزة", "العمرانية", 
    "الهرم", "الواحات البحرية", "الوراق", "بولاق الدكرور", "جنوب الجيزة", 
    "حدائق أكتوبر", "ديوان المديرية", "شمال الجيزة", "كرداسة", "منشأة القناطر"
]

# تطبيق CSS متقدم لتصمييم شريط الهيدر المماثل للصورة المرفقة
st.markdown("""
    <style>
    /* الإعدادات العامة لاتجاه الصفحة RTL */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f8f9fa;
    }

    /* إخفاء شريط التنقل الجانبي الافتراضي لتسليط الضوء على الهيدر العلوي */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* شريط التنقل العلوي المماثل للصورة (Navigation Bar) */
    .top-navbar {
        background-color: #0b1a3e; /* اللون الكحلي الغامق */
        padding: 12px 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: rtl;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 25px;
    }

    .nav-right-container {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .nav-logo-text {
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        border-left: 1px solid rgba(255,255,255,0.2);
        padding-left: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* زر منصة المعلم باللون الأحمر المائل للذهبي */
    .teacher-platform-btn {
        background: linear-gradient(135deg, #c02425 0%, #b21f1f 100%);
        color: white !important;
        padding: 8px 24px;
        border-radius: 20px 8px 20px 8px;
        font-weight: bold;
        font-size: 1.05rem;
        text-decoration: none;
        box-shadow: 0 3px 8px rgba(178, 31, 31, 0.4);
        border: 1px solid #ffd700;
        transition: transform 0.2s ease;
    }

    .teacher-platform-btn:hover {
        transform: scale(1.03);
    }

    /* العناوين المنسقة بوسط الصفحة */
    .centered-header {
        text-align: center;
        margin: 25px 0 35px 0;
    }

    .main-header-title {
        color: #0b1a3e;
        font-size: 2.2rem;
        font-weight: 800;
        display: inline-block;
        padding-bottom: 8px;
        border-bottom: 4px solid #937B2B;
    }

    .sub-header-title {
        color: #666666;
        font-size: 1.1rem;
        margin-top: 8px;
    }

    /* شبكة عرض الإدارات التعليمية */
    .edarat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 15px;
        direction: rtl;
        margin-top: 20px;
    }

    .edara-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-right: 4px solid #0b1a3e;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        color: #1a202c;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }

    .edara-card:hover {
        border-right-color: #937B2B;
        transform: translateY(-3px);
        box-shadow: 0 5px 12px rgba(0,0,0,0.1);
        background-color: #fdfdfd;
    }

    /* تصميم بطاقات البرامج التدريبية */
    .program-card {
        background-color: #1b2631;
        border: 2px solid #937B2B;
        border-radius: 30px 0px 30px 0px;
        padding: 25px 20px;
        color: white;
        text-align: right;
        direction: rtl;
        min-height: 230px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        margin-bottom: 12px;
    }

    .program-title {
        color: #FFD700;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 12px;
    }

    .program-desc {
        font-size: 0.95rem;
        line-height: 1.7;
        color: #e0e0e0;
    }

    .card-footer {
        background-color: #ffffff;
        color: #937B2B;
        text-align: center;
        padding: 8px;
        font-weight: bold;
        border: 1.5px solid #937B2B;
        border-radius: 0 0 12px 12px;
        margin-top: 5px;
    }

    /* تخصيص أزرار Streamlit */
    .stButton>button {
        background-color: #b22222 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- التحكم بالتبويبات عبر session_state ----------------
if 'current_tab' not in st.session_state:
    st.session_state['current_tab'] = 'الرئيسية'

# إنشاء شريط التنقل العلوي HTML
st.markdown("""
    <div class="top-navbar">
        <div class="nav-right-container">
            <div class="nav-logo-text">
                🏛️ الأكاديمية المهنية للمعلمين
            </div>
        </div>
        <div class="teacher-platform-btn">
            منصة المٌعلم 🎓
        </div>
    </div>
""", unsafe_allow_html=True)

# أزرار اختيار التبويبات بالهيدر العلوي مطابق للشريط المطلوب
cols = st.columns([1, 1.2, 1.3, 1.3, 1.2, 1.2, 1.5])

with cols[0]:
    if st.button("الرئيسية", use_container_width=True):
        st.session_state['current_tab'] = 'الرئيسية'

with cols[1]:
    if st.button("عن الأكاديمية", use_container_width=True):
        st.session_state['current_tab'] = 'عن الأكاديمية'

with cols[2]:
    if st.button("ادارات الافراد", use_container_width=True):
        st.session_state['current_tab'] = 'ادارات الافراد'

with cols[3]:
    if st.button("الادارات التعليمية", use_container_width=True):
        st.session_state['current_tab'] = 'الادارات التعليمية'

with cols[4]:
    if st.button("خدمات الأكاديمية", use_container_width=True):
        st.session_state['current_tab'] = 'خدمات الأكاديمية'

with cols[5]:
    if st.button("مجتمعات التعلم", use_container_width=True):
        st.session_state['current_tab'] = 'مجتمعات التعلم'

with cols[6]:
    if st.button("منصة الفرع والبرامج", use_container_width=True):
        st.session_state['current_tab'] = 'منصة الفرع'

st.markdown("<hr style='margin-top: 5px; margin-bottom: 25px;'>", unsafe_allow_html=True)

current_tab = st.session_state['current_tab']

# 1️⃣ الصفحة الرئيسية
if current_tab == "الرئيسية":
    st.markdown("""
        <div class="centered-header">
            <div class="main-header-title">أهلاً بكم في البوابة الرقمية للفرع</div>
            <div class="sub-header-title">الأكاديمية المهنية للمعلمين - منصة التنمية المهنية والاعتماد الرقمي</div>
        </div>
    """, unsafe_allow_html=True)

    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        image_path = "image_526f40.jpg"
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True, caption="منصة الفرع والأكاديمية المهنية للمعلمين")
        else:
            st.info("🎓 شعار الأكاديمية المهنية للمعلمين")

# 2️⃣ عن الأكاديمية
elif current_tab == "عن الأكاديمية":
    st.markdown("""
        <div class="centered-header">
            <div class="main-header-title">عن الأكاديمية والفرع</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: white; padding: 30px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); line-height: 1.8; font-size: 1.1rem;">
            تسعى الأكاديمية المهنية للمعلمين بفرعها المعتمد إلى الارتقاء بمستوى المعلمين والقيادات التربوية، وتقديم أفضل البرامج التأهيلية للترقي والتسكين والتوجيه الفني وفق أحدث المعايير الرقمية.
        </div>
    """, unsafe_allow_html=True)

# 3️⃣ الإدارات التعليمية
elif current_tab == "الادارات التعليمية":
    st.markdown("""
        <div class="centered-header">
            <div class="main-header-title">الإدارات التعليمية التابعة للفرع</div>
            <div class="sub-header-title">دليل الإدارات والديوان بمحافظة الجيزة</div>
        </div>
    """, unsafe_allow_html=True)

    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
    for index, edara in enumerate(EDARAT_LIST):
        col_target = [col_e1, col_e2, col_e3, col_e4][index % 4]
        with col_target:
            st.markdown(f'<div class="edara-card">📍 إدارة {edara}</div>', unsafe_allow_html=True)

# 4️⃣ منصة الفرع والبرامج التدريبية
elif current_tab == "منصة الفرع":
    st.markdown("""
        <div class="centered-header">
            <div class="main-header-title">منصة الفرع - البرامج الرقمية المعتمدة</div>
        </div>
    """, unsafe_allow_html=True)

    sub_category = st.selectbox(
        "اختر الفئة التدريبية المطلوب عرض برامجها:",
        [
            "برامج القيادات التربوية",
            "برامج التسكين والترقي",
            "برنامج تغيير المسمى الوظيفي",
            "برامج الاعتماد"
        ]
    )

    if sub_category == "برامج القيادات التربوية":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برامج القيادات التربوية</h3>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة مدرسية</div>
                    <div class="program-desc">أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية للمعلمين المتاحة للفئات المستهدفة.</div>
                </div>
            """, unsafe_allow_html=True)
            st.button("التسجيل بالبرنامج", key="b1", use_container_width=True)
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-desc">إعداد وتأهيل القيادات للإدارات التعليمية لتطوير المهارات القيادية والإدارية.</div>
                </div>
            """, unsafe_allow_html=True)
            st.button("التسجيل بالبرنامج", key="b2", use_container_width=True)
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

        with c3:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-desc">تمكين الموجهين الفنيين من المهارات الأساسية للإشراف ومتابعة الأداء التعليمي.</div>
                </div>
            """, unsafe_allow_html=True)
            st.button("التسجيل بالبرنامج", key="b3", use_container_width=True)
            st.markdown('<div class="card-footer">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    elif sub_category == "برامج التسكين والترقي":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برامج التسكين والترقي</h3>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-desc">تأهيل المعلمين المساعدين لاستكمال متطلبات التسكين على الكادر.</div>
                </div>
            """, unsafe_allow_html=True)
            st.button("التسجيل بالبرنامج", key="b4", use_container_width=True)
            st.markdown('<div class="card-footer">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-desc">تطوير مهارات واستراتيجيات التدريس الحديثة للمعلمين المستحقين للترقية.</div>
                </div>
            """, unsafe_allow_html=True)
            st.button("التسجيل بالبرنامج", key="b5", use_container_width=True)
            st.markdown('<div class="card-footer">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    elif sub_category == "برنامج تغيير المسمى الوظيفي":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برنامج تغيير المسمى الوظيفي</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div class="program-title">برنامج تغيير المسمى الوظيفي</div>
                <div class="program-desc">برنامج معتمد لإعادة التأهيل التربوي والتخصصي لمطابقة التخصصات والتسكين الوظيفي.</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("التسجيل بالبرنامج", key="b6", use_container_width=True)
        st.markdown('<div class="card-footer" style="max-width: 500px; margin: auto;">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    elif sub_category == "برامج الاعتماد":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برامج الاعتماد</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div class="program-title">البرنامج الرقمي للاعتماد (TOT)</div>
                <div class="program-desc">دورة تدريب المدربين الرقمية لتأهيل وإعداد مدربين معتمدين وفق معايير الجودة.</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("التسجيل بالبرنامج", key="b7", use_container_width=True)
        st.markdown('<div class="card-footer" style="max-width: 500px; margin: auto;">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)

# التبويبات المتبقية
else:
    st.markdown(f"""
        <div class="centered-header">
            <div class="main-header-title">{current_tab}</div>
        </div>
    """, unsafe_allow_html=True)
    st.info(f"محتوى قسم {current_tab} متاح وجاهز للتخصيص.")
