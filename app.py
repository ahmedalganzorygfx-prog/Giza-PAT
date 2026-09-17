import streamlit as st
import os
import urllib.parse
import base64

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# دالة مساعدة لتحميل الصورة كـ base64 من مجلد المشروع محلياً لسرعة العرض
@st.cache_data
def get_image_url_or_base64(file_name, fallback_url=""):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(script_dir, file_name)
    
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            ext = file_name.split('.')[-1].lower()
            mime_type = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime_type};base64,{encoded}"
    return fallback_url

# قائمة الإدارات التعليمية لمحافظة الجيزة
EDARAT_LIST = [
    "أبو النمرس", "أطفيح", "أكتوبر", "أوسيم", "البدرشين", "الحوامدية", 
    "الدقى", "الديوان العام", "الشيخ زايد", "الصف", "العجوزة", "العمرانية", 
    "الهرم", "الواحات البحرية", "الوراق", "بولاق الدكرور", "جنوب الجيزة", 
    "حدائق أكتوبر", "ديوان المديرية", "شمال الجيزة", "كرداسة", "منشأة القناطر"
]

# قائمة الوظائف الحالية
JOBS_LIST = [
    "معلم مساعد", "معلم", "معلم أول", "معلم أول أ", "معلم خبير", "كبير معلمين"
]

# تحضير اللوجو
logo_src = get_image_url_or_base64("Logo.png", "https://via.placeholder.com/220x220?text=PAT+Logo")
logo_navbar_tag = f'<img src="{logo_src}" class="navbar-logo-img" alt="لوجو">' if logo_src else ""
logo_header_tag = f'<img src="{logo_src}" class="center-main-logo" alt="لوجو الأكاديمية">' if logo_src else ""

# تطبيق التنسيقات (CSS) السريعة والخفيفة
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    /* شريط التنقل العلوي الهيدر */
    .top-navbar {
        background-color: #0b1a3e !important;
        padding: 12px 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: rtl;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        margin-bottom: 20px;
        border-bottom: 3px solid #937B2B;
    }

    .nav-right-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .nav-logo-text {
        color: #ffffff !important;
        font-weight: bold;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .navbar-logo-img {
        height: 45px;
        width: auto;
        border-radius: 6px;
        object-fit: contain;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 3px;
    }

    .teacher-platform-btn {
        background: linear-gradient(135deg, #c02425 0%, #b21f1f 100%) !important;
        color: white !important;
        padding: 8px 24px;
        border-radius: 20px 8px 20px 8px;
        font-weight: bold;
        font-size: 1.05rem;
        text-decoration: none;
        box-shadow: 0 3px 8px rgba(178, 31, 31, 0.4);
        border: 1px solid #ffd700;
        display: inline-block;
        transition: transform 0.2s ease;
    }

    .teacher-platform-btn:hover {
        transform: scale(1.03);
    }

    /* تنسيق اللوجو في المنتصف أعلى العنوان الرئيسي */
    .centered-header {
        text-align: center !important;
        margin: 10px 0 25px 0;
    }

    .center-main-logo {
        height: 180px;
        width: auto;
        object-fit: contain;
        margin-bottom: 18px;
        display: inline-block;
        filter: drop-shadow(0px 6px 12px rgba(0,0,0,0.4));
    }

    .main-header-title {
        color: var(--text-color);
        font-size: 2.4rem;
        font-weight: 800;
        display: inline-block;
        padding-bottom: 8px;
        border-bottom: 4px solid #937B2B;
        text-align: center !important;
    }

    .sub-header-title {
        color: var(--text-color);
        opacity: 0.85;
        font-size: 1.2rem;
        margin-top: 14px;
        text-align: center !important;
    }

    /* تصميم العرض السلايدر السريع */
    .simple-slider-container {
        position: relative;
        width: 100%;
        margin: 0 auto 15px auto;
        border-radius: 16px;
        overflow: hidden;
        background-color: #0b1a3e !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
        border: 2px solid #937B2B;
    }

    .simple-slider-img {
        width: 100%;
        height: 480px;
        object-fit: contain !important;
        display: block;
        background-color: #0b1a3e;
        padding: 10px;
    }

    .simple-slider-caption {
        background: linear-gradient(135deg, #0b1a3e 0%, #1b2631 100%);
        color: #FFD700 !important;
        font-size: 1.25rem;
        font-weight: bold;
        padding: 16px;
        text-align: center !important;
        border-top: 2px solid #937B2B;
    }

    .edara-card {
        background-color: var(--secondary-background-color);
        border: 1px solid rgba(147, 123, 43, 0.3);
        border-right: 4px solid #0b1a3e;
        border-radius: 8px;
        padding: 15px;
        text-align: center !important;
        font-weight: bold;
        color: var(--text-color);
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    .program-card {
        background-color: #1b2631 !important;
        border: 2px solid #937B2B;
        border-radius: 30px 0px 30px 0px;
        padding: 25px 20px;
        color: white !important;
        text-align: center !important;
        direction: rtl;
        min-height: 230px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        margin-bottom: 12px;
    }

    .program-title {
        color: #FFD700 !important;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 12px;
        text-align: center !important;
    }

    .program-desc {
        font-size: 0.95rem;
        line-height: 1.7;
        color: #e0e0e0 !important;
        text-align: center !important;
    }

    .card-footer {
        background-color: var(--secondary-background-color);
        color: #937B2B;
        text-align: center !important;
        padding: 8px;
        font-weight: bold;
        border: 1.5px solid #937B2B;
        border-radius: 0 0 12px 12px;
        margin-top: 5px;
    }

    .support-form-container {
        background-color: var(--secondary-background-color);
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        border-top: 6px solid #937B2B;
        border-right: 1px solid rgba(147, 123, 43, 0.2);
        border-left: 1px solid rgba(147, 123, 43, 0.2);
        max-width: 850px;
        margin: 0 auto;
    }

    .support-form-title {
        color: var(--text-color);
        text-align: center !important;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px dashed #937B2B;
    }

    .stButton>button {
        background: linear-gradient(135deg, #0b1a3e 0%, #1b2631 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border-radius: 10px !important;
        border: 1px solid #937B2B !important;
        padding: 10px 20px !important;
    }

    .whatsapp-card {
        display: block;
        text-align: center !important;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        font-weight: bold;
        padding: 15px 10px;
        border-radius: 12px;
        text-decoration: none;
        border: 1px solid #ffffff;
    }

    .app-footer {
        margin-top: 50px;
        padding: 20px 0;
        background-color: #0b1a3e !important;
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.05rem;
        font-weight: bold;
        border-top: 3px solid #937B2B;
        border-radius: 12px 12px 0 0;
    }
    
    .app-footer span {
        color: #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التبويبات الحالية
if 'current_tab' not in st.session_state:
    st.session_state['current_tab'] = 'الرئيسية'

# الشريط العلوي للهيدر
st.markdown(f"""
    <div class="top-navbar">
        <div class="nav-right-container">
            <div class="nav-logo-text">
                {logo_navbar_tag}
                <span>الأكاديمية المهنية للمعلمين - فرع الجيزة</span>
            </div>
        </div>
        <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="teacher-platform-btn">
            منصة المٌعلم 🎓
        </a>
    </div>
""", unsafe_allow_html=True)

# أزرار التبويبات الرئيسية
cols = st.columns([1, 1, 1.1, 1.2, 1.2, 1.1, 1.3, 1.4])

with cols[0]:
    if st.button("الرئيسية", use_container_width=True):
        st.session_state['current_tab'] = 'الرئيسية'

with cols[1]:
    if st.button("عن الفرع", use_container_width=True):
        st.session_state['current_tab'] = 'عن الفرع'

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

with cols[7]:
    if st.button("التواصل مع الدعم", use_container_width=True):
        st.session_state['current_tab'] = 'التواصل مع الدعم'

st.markdown("<hr style='margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

current_tab = st.session_state['current_tab']

# 1️⃣ الصفحة الرئيسية (سريعة وتفاعلية مع أزرار التنقل الفوري)
if current_tab == "الرئيسية":

    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
            <div class="sub-header-title">البوابة الرقمية للخدمات والتدريبات والاعتماد المهني للمعلمين</div>
        </div>
    """, unsafe_allow_html=True)

    # قائمة صور البرامج
    program_slides = [
        {
            "title": "🎓 برنامج القيادات التربوية (مدير ووكيل إدارة مدرسية وتعليمية - التوجيه الفني)",
            "file_name": "leaders.jpg",
            "fallback": "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=1600&auto=format&fit=crop"
        },
        {
            "title": "📜 برامج التسكين والترقي والتطبيقات التربوية للمعلم المساعد",
            "file_name": "teachers.jpg",
            "fallback": "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=1600&auto=format&fit=crop"
        },
        {
            "title": "🔄 برنامج تغيير المسمى الوظيفي وتأهيل الكوادر التعليمية",
            "file_name": "job_change.jpg",
            "fallback": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1600&auto=format&fit=crop"
        },
        {
            "title": "🌟 البرنامج الرقمي للاعتماد وتأهيل المدربين المحترفين (TOT)",
            "file_name": "tot.jpg",
            "fallback": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1600&auto=format&fit=crop"
        }
    ]

    if 'slide_idx' not in st.session_state:
        st.session_state['slide_idx'] = 0

    current = program_slides[st.session_state['slide_idx']]
    img_src = get_image_url_or_base64(current['file_name'], current['fallback'])

    # عرض المعرض
    st.markdown(f"""
        <div class="simple-slider-container">
            <img src="{img_src}" class="simple-slider-img" alt="صورة العرض">
            <div class="simple-slider-caption">{current['title']}</div>
        </div>
    """, unsafe_allow_html=True)

    # أزرار تنقل تفاعلية فورية ومباشرة بدون بطء
    col_prev, col_blank, col_next = st.columns([2, 8, 2])
    with col_prev:
        if st.button("❮ السابق", use_container_width=True):
            st.session_state['slide_idx'] = (st.session_state['slide_idx'] - 1) % len(program_slides)
            st.rerun()

    with col_next:
        if st.button("التالي ❯", use_container_width=True):
            st.session_state['slide_idx'] = (st.session_state['slide_idx'] + 1) % len(program_slides)
            st.rerun()

# 2️⃣ عن الفرع
elif current_tab == "عن الفرع":
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">عن فرع الجيزة</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: var(--secondary-background-color); padding: 30px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); line-height: 1.8; font-size: 1.1rem; color: var(--text-color); text-align: center;">
            يقدم فرع الأكاديمية المهنية للمعلمين بمحافظة الجيزة البرامج التدريبية المعتمدة لترقي وتسكين أعضاء هيئة التعليم، وإعداد القيادات التربوية وتغيير المسمى الوظيفي بجميع الإدارات التعليمية التابعة للمحافظة.
        </div>
    """, unsafe_allow_html=True)

# 3️⃣ الإدارات التعليمية
elif current_tab == "الادارات التعليمية":
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الإدارات التعليمية - محافظة الجيزة</div>
            <div class="sub-header-title">دليل الإدارات التعليمية والديوان التابعة لفرع الجيزة</div>
        </div>
    """, unsafe_allow_html=True)

    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
    for index, edara in enumerate(EDARAT_LIST):
        col_target = [col_e1, col_e2, col_e3, col_e4][index % 4]
        with col_target:
            st.markdown(f'<div class="edara-card">📍 إدارة {edara}</div>', unsafe_allow_html=True)

# 4️⃣ منصة الفرع والبرامج
elif current_tab == "منصة الفرع":
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">منصة فرع الجيزة - البرامج الرقمية</div>
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
            st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-desc">إعداد وتأهيل القيادات للإدارات التعليمية لتطوير المهارات القيادية والإدارية.</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

        with c3:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-desc">تمكين الموجهين الفنيين من المهارات الأساسية للإشراف ومتابعة الأداء التعليمي.</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
            st.markdown('<div class="card-footer">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    elif sub_category == "برامج التسكين والترقي":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برامج التسكين والترقي</h3>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-desc">تأهيل المعلمين المساعدين لاستكمال متطلبات التسكين على الكادر الوظيفي.</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
            st.markdown('<div class="card-footer">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-desc">تطوير مهارات واستراتيجيات التدريس الحديثة للمعلمين المستحقين للترقية.</div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
            st.markdown('<div class="card-footer">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    elif sub_category == "برنامج تغيير المسمى الوظيفي":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برنامج تغيير المسمى الوظيفي</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div class="program-title">برنامج تغيير المسمى الوظيفي</div>
                <div class="program-desc">برنامج معتمد لإعادة التأهيل التربوي والتخصصي لمطابقة التخصصات والتسكين الوظيفي.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="max-width: 500px; margin: auto;"><a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer" style="max-width: 500px; margin: auto;">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    elif sub_category == "برامج الاعتماد":
        st.markdown('<h3 style="text-align: center; color: #937B2B;">برامج الاعتماد</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div class="program-title">البرنامج الرقمي للاعتماد (TOT)</div>
                <div class="program-desc">دورة تدريب المدربين الرقمية لتأهيل وإعداد مدربين معتمدين وفق معايير الجودة.</div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="max-width: 500px; margin: auto;"><a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer" style="max-width: 500px; margin: auto;">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)

# 5️⃣ نموذج التواصل مع فريق الدعم
elif current_tab == "التواصل مع الدعم":
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">التواصل مع فريق الدعم الفني</div>
            <div class="sub-header-title">يرجى تسجيل البيانات أدناه لتوجيه طلبك مباشرة إلى فريق الدعم المختص عبر الواتساب</div>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('''
            <div class="support-form-container">
                <div class="support-form-title">📋 استمارة تقديم طلب دعم فني</div>
        ''', unsafe_allow_html=True)
        
        with st.form("support_form", clear_on_submit=False):
            name = st.text_input("👤 الاسم ثلاثي / رباعي *", placeholder="أدخل اسمك بالكامل كما هو بالصحيفة")
            
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                edara = st.selectbox("📍 الإدارة التعليمية *", EDARAT_LIST)
            with col_f2:
                job = st.selectbox("💼 الوظيفة الحالية *", JOBS_LIST)
                
            phone = st.text_input("📱 رقم الموبايل (واتس آب للتواصل) *", placeholder="مثال: 01012345678")
            
            problem = st.text_area("📝 شرح المشكلة بالتفصيل *", placeholder="اكتب تفاصيل المشكلة أو الاستفسار بدقة...", height=120)
            
            file_uploaded = st.file_uploader(
                "📑 إرفاق صحيفة أحوال إلكترونية حديثة (PDF أو صورة) *", 
                type=["pdf", "png", "jpg", "jpeg"]
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("🚀 تجهيز الرسالة وتأكيد الطلب", use_container_width=True)
            
            if submitted:
                if not name or not phone or not problem or file_uploaded is None:
                    st.error("⚠️ يرجى استكمال كافة البيانات المطلوبة وإرفاق صحيفة الأحوال الإلكترونية.")
                else:
                    st.session_state['form_data'] = {
                        'name': name,
                        'edara': edara,
                        'job': job,
                        'phone': phone,
                        'problem': problem,
                        'file_name': file_uploaded.name
                    }
                    st.success("🎉 تم تجهيز طلبك بنجاح! اختر أحد أرقام فريق الدعم بالأسفل للإرسال المباشر:")

        if 'form_data' in st.session_state and st.session_state['form_data']:
            data = st.session_state['form_data']
            
            msg_text = f"""*طلب دعم فني - منصة فرع الجيزة*
📌 *الاسم:* {data['name']}
📍 *الإدارة التعليمية:* {data['edara']}
💼 *الوظيفة الحالية:* {data['job']}
📱 *رقم التواصل:* {data['phone']}
📑 *صحيفة الأحوال:* مرفقة ({data['file_name']})

📝 *تفاصيل المشكلة:*
{data['problem']}"""
            
            encoded_msg = urllib.parse.quote(msg_text)

            st.markdown("<br><h4 style='text-align: center; color: var(--text-color);'>📲 اضغط على أحد الأرقام التالية للإرسال الفوري عبر الواتساب:</h4>", unsafe_allow_html=True)
            
            whatsapp_numbers = [
                ("مسؤول الدعم (1)", "201069996245"),
                ("مسؤول الدعم (2)", "201120807631"),
                ("مسؤول الدعم (3)", "201201109892")
            ]

            cols_wa = st.columns(3)
            for idx, (label, num) in enumerate(whatsapp_numbers):
                wa_url = f"https://wa.me/{num}?text={encoded_msg}"
                with cols_wa[idx]:
                    st.markdown(
                        f'''<a href="{wa_url}" target="_blank" class="whatsapp-card">
                            💬 {label}<br>
                            <span style="font-size: 0.9rem; opacity: 0.9;">({num.replace('20', '0')})</span>
                        </a>''', 
                        unsafe_allow_html=True
                    )
            
            st.info("📌 **تنويه هام:** بعد فتح الواتساب، يرجى إعادة إرسال ملف صحيفة الأحوال الإلكترونية داخل شات المحادثة.")
            
        st.markdown('</div>', unsafe_allow_html=True)

# باقي التبويبات
else:
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{current_tab}</div>
        </div>
    """, unsafe_allow_html=True)
    st.info(f"قسم {current_tab} متاح وجاهز للإضافة والتخصيص.")

# ----------------- 🏛️ الختام (Footer) -----------------
st.markdown("""
    <div class="app-footer">
        تصميم وتنفيذ: <span>أحمد الجنزوري</span> - مدير الفرع
    </div>
""", unsafe_allow_html=True)
