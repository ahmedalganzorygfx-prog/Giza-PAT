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

# دالة قراءة وتحميل الصور المباشرة (بدون كاش قديم لضمان ظهور الصور الجديدة فوراً)
def get_image_base64_direct(file_name):
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        name_without_ext = os.path.splitext(file_name)[0]
        
        # جميع الاحتمالات الممكنة لأسماء وامتدادات الملفات (مكافحة مشاكل الحروف الكبيرة والنقط المفقودة)
        possible_names = [
            file_name,
            f"{name_without_ext}.jpg",
            f"{name_without_ext}.JPG",
            f"{name_without_ext}.jpeg",
            f"{name_without_ext}.JPEG",
            f"{name_without_ext}.png",
            f"{name_without_ext}.PNG",
            f"{name_without_ext}.webp",
            f"{name_without_ext}JPG",
            f"{name_without_ext}jpg"
        ]
        
        for fname in possible_names:
            img_path = os.path.join(script_dir, fname)
            if os.path.exists(img_path) and os.path.isfile(img_path):
                with open(img_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                    ext_name = os.path.splitext(fname)[1].replace('.', '').lower()
                    mime_type = "image/png" if ext_name == "png" else ("image/webp" if ext_name == "webp" else "image/jpeg")
                    return f"data:{mime_type};base64,{encoded}"
    except Exception:
        pass
    return None

def find_and_load_image(base_file_name, fallback_url=""):
    img_data = get_image_base64_direct(base_file_name)
    return img_data if img_data else fallback_url

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
logo_src = find_and_load_image("Logo.png", "https://via.placeholder.com/220x220?text=PAT+Logo")
logo_navbar_tag = f'<img src="{logo_src}" class="navbar-logo-img" alt="لوجو">' if logo_src else ""
logo_header_tag = f'<img src="{logo_src}" class="center-main-logo" alt="لوجو الأكاديمية">' if logo_src else ""

# رابط صفحة الفيسبوك الخاص بكم
FACEBOOK_PAGE_URL = "https://www.facebook.com/share/18PF695ehm/"

# تطبيق التنسيقات (CSS)
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    [data-testid="stSidebar"] { display: none; }

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

    .nav-right-container { display: flex; align-items: center; gap: 15px; }

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
    }

    .centered-header { text-align: center !important; margin: 10px 0 25px 0; }

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

    .section-title {
        text-align: center !important;
        color: #FFD700 !important;
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 35px;
        margin-bottom: 25px;
        padding-bottom: 8px;
        border-bottom: 2px dashed #937B2B;
    }

    /* 🎨 تصميم كروت البرامج بالصور والتفاصيل 🎨 */
    .program-card-wrapper {
        background-color: #1b2631;
        border: 2px solid #937B2B;
        border-radius: 60px 0px 60px 0px;
        overflow: hidden;
        margin-bottom: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }

    .program-card-wrapper:hover {
        transform: translateY(-5px);
        border-color: #FFD700;
    }

    .program-img-box {
        width: 100%;
        height: 190px;
        overflow: hidden;
        background-color: #0b1a3e;
    }

    .program-img-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .program-content-box {
        padding: 20px 15px;
        text-align: center !important;
    }

    .program-card-title {
        color: #FFD700 !important;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .program-card-desc {
        color: #e0e0e0 !important;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .card-footer-badge {
        background-color: var(--secondary-background-color);
        color: #937B2B;
        text-align: center !important;
        padding: 8px;
        font-weight: bold;
        border: 1.5px solid #937B2B;
        border-radius: 0 0 12px 12px;
        margin-top: 5px;
        margin-bottom: 25px;
    }

    .staff-card {
        background-color: #1b2631 !important;
        border: 2px solid #937B2B;
        border-radius: 20px;
        padding: 30px 20px;
        text-align: center !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }

    .avatar-frame {
        width: 150px;
        height: 150px;
        margin: 0 auto 18px auto;
        border-radius: 50%;
        border: 4px solid #FFD700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
        overflow: hidden;
        background-color: #0b1a3e;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .avatar-frame img { width: 100%; height: 100%; object-fit: cover !important; }
    .staff-name { color: #FFD700 !important; font-size: 1.35rem; font-weight: bold; margin-bottom: 8px; }
    .staff-role { color: #ffffff !important; font-size: 1.05rem; font-weight: 600; margin-bottom: 6px; }
    .staff-dept {
        color: #937B2B !important;
        font-size: 0.95rem;
        font-weight: bold;
        background-color: rgba(147, 123, 43, 0.15);
        padding: 4px 12px;
        border-radius: 12px;
        display: inline-block;
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

    .facebook-btn-tab {
        background: linear-gradient(135deg, #1877F2 0%, #0d5cb6 100%) !important;
        color: white !important;
        padding: 10px 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.05rem;
        text-decoration: none;
        display: block;
        text-align: center;
        border: 1px solid #ffffff;
        box-shadow: 0 3px 8px rgba(24, 119, 242, 0.3);
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
    
    .app-footer span { color: #FFD700; }
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

# قائمة التبويبات
cols = st.columns([1.1, 1, 1.1, 1.2, 1.2, 1.1, 1.4, 1.3])

tabs_names = [
    "الرئيسية", "عن الفرع", "ادارات الافراد", "الادارات التعليمية", 
    "خدمات الأكاديمية", "مجتمعات التعلم", "التواصل مع الدعم"
]

# عرض التبويبات
for idx, name in enumerate(tabs_names):
    with cols[idx]:
        if st.button(name, key=f"tab_btn_{idx}", use_container_width=True):
            st.session_state['current_tab'] = name

# زر الفيسبوك المخصص
with cols[7]:
    st.markdown(f"""
        <a href="{FACEBOOK_PAGE_URL}" target="_blank" class="facebook-btn-tab">
            📘 فيسبوك الفرع
        </a>
    """, unsafe_allow_html=True)

st.markdown("<hr style='margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True)

current_tab = st.session_state['current_tab']

# تحميل صور البرامج بالأداة المباشرة
img_leaders = find_and_load_image("leaders.jpg", "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=800&auto=format&fit=crop")
img_teachers = find_and_load_image("teachers.jpg", "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=800&auto=format&fit=crop")
img_job = find_and_load_image("job_change.jpg", "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800&auto=format&fit=crop")
img_tot = find_and_load_image("tot.jpg", "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=800&auto=format&fit=crop")

# 1️⃣ الصفحة الرئيسية
if current_tab == "الرئيسية":

    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
            <div class="sub-header-title">البوابة الرقمية للخدمات والتدريبات والاعتماد المهني للمعلمين</div>
        </div>
    """, unsafe_allow_html=True)

    # 1. قسم برامج القيادات التربوية
    st.markdown('<div class="section-title">👑 برامج القيادات التربوية</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leaders}" alt="مدير ووكيل إدارة مدرسية"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مدير ووكيل إدارة مدرسية</div>
                    <div class="program-card-desc">أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية للمعلمين المتاحة للفئات المستهدفة.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leaders}" alt="مدير ووكيل إدارة تعليمية"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-card-desc">إعداد وتأهيل القيادات للإدارات التعليمية لتطوير المهارات القيادية والإدارية.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leaders}" alt="أساسيات التوجيه الفني"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-card-desc">تمكين الموجهين الفنيين من المهارات الأساسية للإشراف ومتابعة الأداء التعليمي.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    # 2. قسم برامج التسكين والترقي
    st.markdown('<div class="section-title">📜 برامج التسكين والترقي</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teachers}" alt="التطبيقات التربوية المعلم المساعد"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-card-desc">تأهيل المعلمين المساعدين لاستكمال متطلبات التسكين على الكادر الوظيفي.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teachers}" alt="مهارات عامة في التدريس"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-card-desc">تطوير مهارات واستراتيجيات التدريس الحديثة للمعلمين المستحقين للترقية.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    # 3. قسم تغيير المسمى الوظيفي وبرامج الاعتماد
    st.markdown('<div class="section-title">🔄 برامج تغيير المسمى الوظيفي والاعتماد</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_job}" alt="تغيير المسمى الوظيفي"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج تغيير المسمى الوظيفي</div>
                    <div class="program-card-desc">برنامج معتمد لإعادة التأهيل التربوي والتخصصي لمطابقة التخصصات والتسكين الوظيفي.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_tot}" alt="الاعتماد TOT"></div>
                <div class="program-content-box">
                    <div class="program-card-title">البرنامج الرقمي للاعتماد (TOT)</div>
                    <div class="program-card-desc">دورة تدريب المدربين الرقمية لتأهيل وإعداد مدربين معتمدين وفق معايير الجودة.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<a href="https://www.pat.edu.eg/platform-programs" target="_blank"><button style="width:100%; border-radius:8px; background-color:#b22222; color:white; font-weight:bold; border:none; padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>', unsafe_allow_html=True)
        st.markdown('<div class="card-footer-badge">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)

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

# 3️⃣ إدارات الأفراد
elif current_tab == "ادارات الافراد":
    st.markdown(f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">إدارات الأفراد - الهيكل الإداري</div>
            <div class="sub-header-title">قيادات وكوادر الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
        </div>
    """, unsafe_allow_html=True)

    img_ahmed = find_and_load_image("ahmed.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png")
    img_khaled = find_and_load_image("khaled.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png")
    img_omar = find_and_load_image("omar.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_ahmed}" alt="أحمد حسني الجنزوري">
                </div>
                <div class="staff-name">أحمد حسني الجنزوري</div>
                <div class="staff-role">👔 مدير الفرع</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_khaled}" alt="خالد عبدالحكيم هارون">
                </div>
                <div class="staff-name">خالد عبدالحكيم هارون</div>
                <div class="staff-role">🤝 مسئول الموارد البشرية</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_omar}" alt="أحمد محمد عمر">
                </div>
                <div class="staff-name">أحمد محمد عمر</div>
                <div class="staff-role">🎯 مسئول التنمية المهنية</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """, unsafe_allow_html=True)

# 4️⃣ الإدارات التعليمية
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
