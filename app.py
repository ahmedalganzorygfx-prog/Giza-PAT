import base64
import os
import urllib.parse
import streamlit as st

# 1️⃣ ضبط إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# 2️⃣ دالة قراءة وتحميل الصور المباشرة
def get_image_base64_direct(file_name):
  try:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    name_without_ext = os.path.splitext(file_name)[0]

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
        f"{name_without_ext}jpg",
    ]

    for fname in possible_names:
      img_path = os.path.join(script_dir, fname)
      if os.path.exists(img_path) and os.path.isfile(img_path):
        with open(img_path, "rb") as f:
          encoded = base64.b64encode(f.read()).decode("utf-8")
          ext_name = os.path.splitext(fname)[1].replace(".", "").lower()
          mime_type = (
              "image/png"
              if ext_name == "png"
              else ("image/webp" if ext_name == "webp" else "image/jpeg")
          )
          return f"data:{mime_type};base64,{encoded}"
  except Exception:
    pass
  return None


def find_and_load_image(base_file_name, fallback_url=""):
  img_data = get_image_base64_direct(base_file_name)
  return img_data if img_data else fallback_url


# 3️⃣ قوائم البيانات الأساسية ورابط الخريطة
EDARAT_LIST = [
    "أبو النمرس",
    "أطفيح",
    "أكتوبر",
    "أوسيم",
    "البدرشين",
    "الحوامدية",
    "الدقى",
    "الديوان العام",
    "الشيخ زايد",
    "الصف",
    "العجوزة",
    "العمرانية",
    "الهرم",
    "الواحات البحرية",
    "الوراق",
    "بولاق الدكرور",
    "جنوب الجيزة",
    "حدائق أكتوبر",
    "ديوان المديرية",
    "شمال الجيزة",
    "كرداسة",
    "منشأة القناطر",
]

JOBS_LIST = [
    "معلم مساعد",
    "معلم",
    "معلم أول",
    "معلم أول أ",
    "معلم خبير",
    "كبير معلمين",
]

# تحضير اللوجو ورابط الفيسبوك والخريطة
logo_src = find_and_load_image(
    "Logo.png", "https://via.placeholder.com/220x220?text=PAT+Logo"
)
logo_navbar_tag = (
    f'<img src="{logo_src}" class="navbar-logo-img" alt="لوجو">'
    if logo_src
    else ""
)
logo_header_tag = (
    f'<img src="{logo_src}" class="center-main-logo" alt="لوجو الأكاديمية">'
    if logo_src
    else ""
)
FACEBOOK_PAGE_URL = "https://www.facebook.com/share/18PF695ehm/"
LOCATION_MAP_URL = "https://maps.app.goo.gl/RVpBuBNVfHFnr7qz9"

# 4️⃣ تطبيق التنسيقات المتكيفة والمتجاوبة المحدثة (Responsive CSS)
st.markdown(
    """
    <style>
    /* 🎯 إخفاء الأزرار الفرعية والإبقاء على القائمة الثلاثية ⋮ فقط 🎯 */
    footer { visibility: hidden !important; }
    
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 99999 !important;
    }

    [data-testid="stToolbarActions"] { display: none !important; }
    [data-testid="stActionButtonIcon"] { display: none !important; }

    html, body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    [data-testid="stSidebar"] { display: none; }

    /* 📱 الهيدر الأساسي - متجاوب 📱 */
    .top-navbar {
        background-color: #0b1a3e !important;
        padding: 12px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: rtl;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        margin-bottom: 20px;
        border-bottom: 3px solid #937B2B;
        flex-wrap: wrap;
        gap: 12px;
    }

    .nav-right-container { 
        display: flex; 
        align-items: center; 
        gap: 12px; 
    }

    .nav-logo-text {
        color: #ffffff !important;
        font-weight: bold;
        font-size: 1.15rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .navbar-logo-img {
        height: 42px;
        width: auto;
        border-radius: 6px;
        object-fit: contain;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 3px;
    }

    .teacher-platform-btn {
        background: linear-gradient(135deg, #c02425 0%, #b21f1f 100%) !important;
        color: white !important;
        padding: 8px 18px;
        border-radius: 20px 8px 20px 8px;
        font-weight: bold;
        font-size: 0.95rem;
        text-decoration: none;
        box-shadow: 0 3px 8px rgba(178, 31, 31, 0.4);
        border: 1px solid #ffd700;
        display: inline-block;
        text-align: center;
    }

    .centered-header { text-align: center !important; margin: 10px 0 25px 0; }

    .center-main-logo {
        height: 150px;
        width: auto;
        object-fit: contain;
        margin-bottom: 15px;
        display: inline-block;
        filter: drop-shadow(0px 6px 12px rgba(0,0,0,0.3));
    }

    .main-header-title {
        color: var(--text-color) !important;
        font-size: 2rem;
        font-weight: 800;
        display: inline-block;
        padding-bottom: 8px;
        border-bottom: 4px solid #937B2B;
        text-align: center !important;
    }

    .sub-header-title {
        color: var(--text-color) !important;
        opacity: 0.85;
        font-size: 1.1rem;
        margin-top: 12px;
        text-align: center !important;
    }

    .section-title {
        text-align: center !important;
        color: #C9A227 !important;
        font-size: 1.6rem;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
        padding-bottom: 8px;
        border-bottom: 2px dashed #937B2B;
    }

    .highlight-name {
        color: #C9A227 !important;
        font-weight: bold !important;
    }

    /* 🎴 كروت البرامج والخدمات المتكيفة 🎴 */
    .program-card-wrapper {
        background-color: var(--secondary-background-color) !important;
        border: 2px solid #937B2B;
        border-radius: 40px 0px 40px 0px;
        overflow: hidden;
        margin-bottom: 15px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        transition: transform 0.3s ease;
    }

    .program-card-wrapper:hover {
        transform: translateY(-4px);
        border-color: #C9A227;
    }

    .program-img-box {
        width: 100%;
        height: 180px;
        overflow: hidden;
        background-color: #0b1a3e;
    }

    .program-img-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .program-content-box {
        padding: 18px 12px;
        text-align: center !important;
    }

    .program-card-title {
        color: #C9A227 !important;
        font-size: 1.15rem;
        font-weight: bold;
        margin-bottom: 8px;
    }

    .program-card-desc {
        color: var(--text-color) !important;
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .card-footer-badge {
        background-color: var(--secondary-background-color) !important;
        color: #937B2B !important;
        text-align: center !important;
        padding: 8px;
        font-weight: bold;
        border: 1.5px solid #937B2B;
        border-radius: 0 0 12px 12px;
        margin-top: 5px;
        margin-bottom: 25px;
        font-size: 0.9rem;
    }

    /* 👤 كروت فريق العمل المتكيفة 👤 */
    .staff-card {
        background-color: var(--secondary-background-color) !important;
        border: 2px solid #937B2B;
        border-radius: 20px;
        padding: 25px 15px;
        text-align: center !important;
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        margin-bottom: 20px;
    }

    .avatar-frame {
        width: 130px;
        height: 130px;
        margin: 0 auto 15px auto;
        border-radius: 50%;
        border: 3px solid #C9A227;
        box-shadow: 0 0 12px rgba(201, 162, 39, 0.3);
        overflow: hidden;
        background-color: #0b1a3e;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .avatar-frame img { width: 100%; height: 100%; object-fit: cover !important; }
    .staff-name { color: #C9A227 !important; font-size: 1.2rem; font-weight: bold; margin-bottom: 6px; }
    .staff-role { color: var(--text-color) !important; font-size: 0.95rem; font-weight: 600; margin-bottom: 6px; }
    .staff-dept {
        color: #937B2B !important;
        font-size: 0.88rem;
        font-weight: bold;
        background-color: rgba(147, 123, 43, 0.15);
        padding: 4px 10px;
        border-radius: 12px;
        display: inline-block;
    }

    .info-card-box {
        direction: rtl;
        text-align: right;
        background-color: var(--secondary-background-color) !important;
        color: var(--text-color) !important;
        padding: 20px;
        border-radius: 16px 0px 16px 0px;
        border: 2px solid #937B2B;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 18px;
    }

    .edara-card {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid rgba(147, 123, 43, 0.3);
        border-right: 4px solid #0b1a3e;
        border-radius: 8px;
        padding: 12px;
        text-align: center !important;
        font-weight: bold;
        color: var(--text-color) !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        font-size: 0.95rem;
    }

    .support-form-container {
        background-color: var(--secondary-background-color) !important;
        padding: 25px 20px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.1);
        border-top: 5px solid #937B2B;
        border-right: 1px solid rgba(147, 123, 43, 0.2);
        border-left: 1px solid rgba(147, 123, 43, 0.2);
        max-width: 850px;
        margin: 0 auto;
    }

    .support-form-title {
        color: var(--text-color) !important;
        text-align: center !important;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 18px;
        padding-bottom: 8px;
        border-bottom: 2px dashed #937B2B;
    }

    /* 📍 خريطة الموقع المتكيفة 📍 */
    .location-card-container {
        background-color: var(--secondary-background-color) !important;
        border: 2px solid #937B2B;
        border-radius: 18px;
        padding: 20px 15px;
        max-width: 850px;
        margin: 25px auto 0 auto;
        text-align: center !important;
        box-shadow: 0 8px 22px rgba(0,0,0,0.1);
    }

    .location-btn {
        background: linear-gradient(135deg, #0b1a3e 0%, #1b2631 100%) !important;
        color: #FFD700 !important;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1rem;
        text-decoration: none;
        display: inline-block;
        border: 1.5px solid #937B2B;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin-bottom: 15px;
    }

    .map-frame {
        width: 100%;
        height: 320px;
        border-radius: 12px;
        border: 2px solid #937B2B;
    }

    .stButton>button {
        background: linear-gradient(135deg, #0b1a3e 0%, #1b2631 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        border-radius: 8px !important;
        border: 1px solid #937B2B !important;
        padding: 8px 15px !important;
    }

    .facebook-btn-tab {
        background: linear-gradient(135deg, #1877F2 0%, #0d5cb6 100%) !important;
        color: white !important;
        padding: 8px 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 0.95rem;
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
        padding: 12px 8px;
        border-radius: 10px;
        text-decoration: none;
        border: 1px solid #ffffff;
        margin-bottom: 10px;
    }

    .app-footer {
        margin-top: 40px;
        padding: 18px 0;
        background-color: #0b1a3e !important;
        color: #ffffff !important;
        text-align: center !important;
        font-size: 0.95rem;
        font-weight: bold;
        border-top: 3px solid #937B2B;
        border-radius: 12px 12px 0 0;
    }
    
    .app-footer span { color: #FFD700; }

    /* 📱 Media Queries للشاشات الصغيرة والموبايل 📱 */
    @media (max-width: 768px) {
        .top-navbar {
            flex-direction: column;
            text-align: center;
            justify-content: center;
            padding: 15px 10px;
        }

        .nav-logo-text {
            font-size: 1rem;
            flex-direction: column;
            gap: 6px;
        }

        .main-header-title {
            font-size: 1.6rem;
        }

        .sub-header-title {
            font-size: 0.95rem;
        }

        .section-title {
            font-size: 1.3rem;
        }

        .center-main-logo {
            height: 120px;
        }

        .map-frame {
            height: 250px;
        }

        .support-form-container {
            padding: 20px 12px;
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 5️⃣ إدارة حالة التبويبات الحالية
if "current_tab" not in st.session_state:
  st.session_state["current_tab"] = "الرئيسية"

# الشريط العلوي للهيدر
st.markdown(
    f"""
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
""",
    unsafe_allow_html=True,
)

# قائمة التبويبات
cols = st.columns([1.1, 1, 1.1, 1.2, 1.2, 1.1, 1.4, 1.3])

tabs_names = [
    "الرئيسية",
    "عن الفرع",
    "ادارات الافراد",
    "الادارات التعليمية",
    "خدمات الأكاديمية",
    "مجتمعات التعلم",
    "التواصل مع الدعم",
]

# عرض التبويبات
for idx, name in enumerate(tabs_names):
  with cols[idx]:
    if st.button(name, key=f"tab_btn_{idx}", use_container_width=True):
      st.session_state["current_tab"] = name

# زر الفيسبوك المخصص
with cols[7]:
  st.markdown(
      f"""
        <a href="{FACEBOOK_PAGE_URL}" target="_blank" class="facebook-btn-tab">
            📘 فيسبوك الفرع
        </a>
    """,
      unsafe_allow_html=True,
  )

st.markdown(
    "<hr style='margin-top: 5px; margin-bottom: 20px;'>", unsafe_allow_html=True
)

current_tab = st.session_state["current_tab"]

# تحميل صور البرامج المخصصة بالأداة المباشرة
img_leader_school = find_and_load_image(
    "leader_school.jpg",
    find_and_load_image(
        "leaders.jpg",
        "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=800&auto=format&fit=crop",
    ),
)
img_leader_edu = find_and_load_image(
    "leader_edu.jpg",
    find_and_load_image(
        "leaders.jpg",
        "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?q=80&w=800&auto=format&fit=crop",
    ),
)
img_leader_guidance = find_and_load_image(
    "leader_guidance.jpg",
    find_and_load_image(
        "leaders.jpg",
        "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=800&auto=format&fit=crop",
    ),
)

img_teacher_assistant = find_and_load_image(
    "teacher_assistant.jpg",
    find_and_load_image(
        "teachers.jpg",
        "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=800&auto=format&fit=crop",
    ),
)
img_teacher_skills = find_and_load_image(
    "teacher_skills.jpg",
    find_and_load_image(
        "teachers.jpg",
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=800&auto=format&fit=crop",
    ),
)

img_job = find_and_load_image(
    "job_change.jpg",
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800&auto=format&fit=crop",
)
img_tot = find_and_load_image(
    "tot.jpg",
    "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=800&auto=format&fit=crop",
)

# 1️⃣ الصفحة الرئيسية
if current_tab == "الرئيسية":

  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
            <div class="sub-header-title">البوابة الرقمية للخدمات والتدريبات والاعتماد المهني للمعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # 1. قسم برامج القيادات التربوية
  st.markdown(
      '<div class="section-title">👑 برامج القيادات التربوية</div>',
      unsafe_allow_html=True,
  )
  c1, c2, c3 = st.columns([1, 1, 1])

  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_school}" alt="مدير ووكيل إدارة مدرسية"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مدير ووكيل إدارة مدرسية</div>
                    <div class="program-card-desc">أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية للمعلمين المتاحة للفئات المستهدفة.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج مدير ووكيل إدارة مدرسية</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_edu}" alt="مدير ووكيل إدارة تعليمية"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-card-desc">إعداد وتأهيل القيادات للإدارات التعليمية لتطوير المهارات القيادية والإدارية.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج مدير ووكيل إدارة تعليمية</div>',
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_guidance}" alt="أساسيات التوجيه الفني"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-card-desc">تمكين الموجهين الفنيين من المهارات الأساسية للإشراف ومتابعة الأداء التعليمي.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج أساسيات التوجيه الفني</div>',
        unsafe_allow_html=True,
    )

  # 2. قسم برامج التسكين والترقي
  st.markdown(
      '<div class="section-title">📜 برامج التسكين والترقي</div>',
      unsafe_allow_html=True,
  )
  c1, c2 = st.columns([1, 1])
  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teacher_assistant}" alt="التطبيقات التربوية المعلم المساعد"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-card-desc">تأهيل المعلمين المساعدين لاستكمال متطلبات التسكين على الكادر الوظيفي.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج التطبيقات التربوية للمعلم'
        ' المساعد</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teacher_skills}" alt="مهارات عامة في التدريس"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-card-desc">تطوير مهارات واستراتيجيات التدريس الحديثة للمعلمين المستحقين للترقية.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج مهارات عامة في التدريس</div>',
        unsafe_allow_html=True,
    )

  # 3. قسم تغيير المسمى الوظيفي وبرامج الاعتماد
  st.markdown(
      '<div class="section-title">🔄 برامج تغيير المسمى الوظيفي والاعتماد</div>',
      unsafe_allow_html=True,
  )
  c1, c2 = st.columns([1, 1])
  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_job}" alt="تغيير المسمى الوظيفي"></div>
                <div class="program-content-box">
                    <div class="program-card-title">برنامج تغيير المسمى الوظيفي</div>
                    <div class="program-card-desc">برنامج معتمد لإعادة التأهيل التربوي والتخصصي لمطابقة التخصصات والتسكين الوظيفي.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج تغيير المسمى الوظيفي</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_tot}" alt="الاعتماد TOT"></div>
                <div class="program-content-box">
                    <div class="program-card-title">البرنامج الرقمي للاعتماد (TOT)</div>
                    <div class="program-card-desc">دورة تدريب المدربين الرقمية لتأهيل وإعداد مدربين معتمدين وفق معايير الجودة.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:8px;'
        " background-color:#b22222; color:white; font-weight:bold; border:none;"
        ' padding:8px; cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">البرنامج الرقمي للاعتماد TOT</div>',
        unsafe_allow_html=True,
    )

# 2️⃣ عن الفرع
elif current_tab == "عن الفرع":
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">عن فرع الأكاديمية المهنية للمعلمين بالجيزة</div>
            <div class="sub-header-title">مسيرة العطاء، التأسيس، والتطوير الرقمي لخدمة المعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # تبويب 1: التأسيس والانطلاقة
  st.markdown(
      """
        <div class="info-card-box">
            <h3 style="color: #C9A227; margin-top: 0; padding-bottom: 10px; border-bottom: 1px dashed #937B2B;">🏛️ التأسيس والانطلاقة (2017)</h3>
            <p style="font-size: 1.05rem; line-height: 1.8; margin-bottom: 0;">
                أُنشئ فرع الأكاديمية المهنية للمعلمين بمحافظة الجيزة في عام <b>2017</b> ليكون الحاضنة الرئيسية لتطوير وتمكين الكوادر التعليمية والتربوية بالمحافظة، وتقديم الخدمات الاعتمادية والتدريبية وفق أعلى معايير الجودة.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # تبويب 2: مرحلة البناء والتأسيس
  st.markdown(
      """
        <div class="info-card-box">
            <h3 style="color: #C9A227; margin-top: 0; padding-bottom: 10px; border-bottom: 1px dashed #937B2B;">📜 مرحلة البناء والتأسيس (2017 – 2023)</h3>
            <p style="font-size: 1.05rem; line-height: 1.8;">
                شهدت الفترة من <b>2017 حتى 2023</b> إرساء القواعد التنظيمية والإدارية للفرع تحت قيادة <span class="highlight-name">الأستاذة / أمل عبد المقصود</span> (مدير الفرع)، وبمعاونة فريق عمل متميز في قسم تكنولوجيا المعلومات (IT) ضم كلاً من:
            </p>
            <ul style="font-size: 1rem; line-height: 2.2; padding-right: 20px;">
                <li><span class="highlight-name">أ . أحمد حسني الجنزوري</span> (عضو تكنولوجيا المعلومات IT)</li>
                <li><span class="highlight-name">أ . خالد عبد الحكيم هارون</span> (عضو تكنولوجيا المعلومات IT)</li>
            </ul>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # تبويب 3: مرحلة التطوير والتحول الرقمي
  st.markdown(
      """
        <div class="info-card-box">
            <h3 style="color: #C9A227; margin-top: 0; padding-bottom: 10px; border-bottom: 1px dashed #937B2B;">🚀 مرحلة التطوير والتحول الرقمي (2023 – حتى الآن)</h3>
            <p style="font-size: 1.05rem; line-height: 1.8;">
                مع بداية عام <b>2023</b>، انطلقت مرحلة جديدة ترتكز على <b>الميكنة والتحول الرقمي للخدمات</b>، برئاسة <span class="highlight-name">الأستاذ / أحمد حسني الجنزوري</span> مديراً للفرع، وفريق عمل متميز يتكون من:
            </p>
            <ul style="font-size: 1rem; line-height: 2.2; padding-right: 20px;">
                <li><span class="highlight-name">أ . خالد عبد الحكيم هارون</span> (مسئول الموارد البشرية وتكنولوجيا المعلومات IT)</li>
                <li><span class="highlight-name">أ . أحمد محمد عمر</span> (مسئول التنمية المهنية والاعتماد)</li>
                <li><span class="highlight-name">أ . أمينة فوزي عبد الرحمن</span> (مسئول التنمية المهنية والاعتماد)</li>
            </ul>
            <p style="font-size: 1rem; line-height: 1.8; margin-top: 10px; margin-bottom: 0;">
                تتضافر الجهود حالياً لتسهيل حصول المعلمين على البرامج الرقمية للقيادات والترقي وتغيير المسمى الوظيفي والدعم الفني المباشر لجميع الإدارات التعليمية بمحافظة الجيزة.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 3️⃣ إدارات الأفراد
elif current_tab == "ادارات الافراد":
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">إدارات الأفراد - الهيكل الإداري</div>
            <div class="sub-header-title">قيادات وكوادر الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  img_ahmed = find_and_load_image(
      "ahmed.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
  )
  img_khaled = find_and_load_image(
      "khaled.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
  )
  img_omar = find_and_load_image(
      "omar.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
  )
  img_amina = find_and_load_image(
      "amina.jpg",
      find_and_load_image(
          "fawzy.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135789.png"
      ),
  )

  c1, c2, c3, c4 = st.columns([1, 1, 1, 1])

  with c1:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_ahmed}" alt="أحمد حسني الجنزوري">
                </div>
                <div class="staff-name"><span class="highlight-name">أحمد حسني الجنزوري</span></div>
                <div class="staff-role" style="margin-top:10px;">👔 مدير الفرع</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_khaled}" alt="خالد عبدالحكيم هارون">
                </div>
                <div class="staff-name"><span class="highlight-name">خالد عبدالحكيم هارون</span></div>
                <div class="staff-role" style="margin-top:10px;">🤝 مسئول الموارد البشرية</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_omar}" alt="أحمد محمد عمر">
                </div>
                <div class="staff-name"><span class="highlight-name">أحمد محمد عمر</span></div>
                <div class="staff-role" style="margin-top:10px;">🎯 مسئول التنمية المهنية</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c4:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame">
                    <img src="{img_amina}" alt="أمينة فوزي عبدالرحمن">
                </div>
                <div class="staff-name"><span class="highlight-name">أمينة فوزي عبدالرحمن</span></div>
                <div class="staff-role" style="margin-top:10px;">🎯 مسئول التنمية المهنية</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

# 4️⃣ الإدارات التعليمية
elif current_tab == "الادارات التعليمية":
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الإدارات التعليمية - محافظة الجيزة</div>
            <div class="sub-header-title">دليل الإدارات التعليمية والديوان التابعة لفرع الجيزة</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  col_e1, col_e2, col_e3, col_e4 = st.columns([1, 1, 1, 1])
  for index, edara in enumerate(EDARAT_LIST):
    col_target = [col_e1, col_e2, col_e3, col_e4][index % 4]
    with col_target:
      st.markdown(
          f'<div class="edara-card">📍 إدارة {edara}</div>',
          unsafe_allow_html=True,
      )

# 5️⃣ خدمات الأكاديمية
elif current_tab == "خدمات الأكاديمية":
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">خدمات الأكاديمية المهنية للمعلمين</div>
            <div class="sub-header-title">دليل الخدمات والتسجيل الرقمي المتاح لجميع أعضاء هيئة التعليم</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # قسم 1: البرامج الاعتمادية والتدريبية
  st.markdown(
      '<div class="section-title">🎓 البرامج الاعتمادية والتأهيلية</div>',
      unsafe_allow_html=True,
  )
  s1, s2 = st.columns([1, 1])
  with s1:
    st.markdown(
        """
            <div class="info-card-box">
                <h3 style="color: #C9A227; margin-top:0;">🌟 برامج الترقي للكادر الوظيفي</h3>
                <p style="line-height: 1.8;">
                    تقديم التدريبات الرقمية المعتمدة لاستكمال متطلبات الترقي للمعلمين المستحقين بالنظام الإلكتروني الحديث، ومتابعة رفع واستيفاء ملفات الترقي بالتعاون مع الإدارات التعليمية.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with s2:
    st.markdown(
        """
            <div class="info-card-box">
                <h3 style="color: #C9A227; margin-top:0;">👑 برامج القيادات التربوية</h3>
                <p style="line-height: 1.8;">
                    تأهيل الكوادر التربوية لشغل وظائف (مدير ووكيل إدارة مدرسية، مدير ووكيل إدارة تعليمية، أساسيات التوجيه الفني) والحصول على شهادات التنمية المهنية المعتمدة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  # قسم 2: الاعتماد وتعديل المسار الوظيفي
  st.markdown(
      '<div class="section-title">📜 الاعتماد وتغيير المسمى الوظيفي</div>',
      unsafe_allow_html=True,
  )
  s3, s4 = st.columns([1, 1])
  with s3:
    st.markdown(
        """
            <div class="info-card-box">
                <h3 style="color: #C9A227; margin-top:0;">🔄 تغيير المسمى الوظيفي</h3>
                <p style="line-height: 1.8;">
                    استقبال وتدقيق أوراق المعلمين الراغبين في تغيير المسمى الوظيفي، وتوفير برامج إعادة التأهيل التربوي والتخصصي المعتمدة لمطابقة المؤهلات والتسكين الصحيح.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with s4:
    st.markdown(
        """
            <div class="info-card-box">
                <h3 style="color: #C9A227; margin-top:0;">💼 واعتماد المدربين والمراكز (TOT)</h3>
                <p style="line-height: 1.8;">
                    منح شهادات الاعتماد الرقمية للمدربين المعتمدين (TOT)، واعتماد برامج التنمية المهنية المستمرة والمؤسسات التدريبية وفق معايير الجودة الشاملة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  # قسم 3: التقدم للبرامج مدفوعة الأجر
  st.markdown(
      '<div class="section-title">📝 التقدم للبرامج مدفوعة الأجر</div>',
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="support-form-container" style="text-align: center;">
            <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-color);">
                تتيح الأكاديمية المهنية للمعلمين بفرع الجيزة إمكانية التقدم والتسجيل الإلكتروني المباشر للبرامج التدريبية مدفوعة الأجر والخاصة بالترقي والاعتماد وتطوير المهارات.
            </p>
            <br>
            <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="location-btn" style="text-decoration: none;">
                🌐 الانتقال إلى منصة التقديم والتسجيل في البرامج
            </a>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 6️⃣ نموذج التواصل مع فريق الدعم + موقع الفرع مع الـ Pin المباشر
elif current_tab == "التواصل مع الدعم":
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">التواصل مع فريق الدعم الفني</div>
            <div class="sub-header-title">يرجى تسجيل البيانات أدناه لتوجيه طلبك مباشرة إلى فريق الدعم المختص عبر الواتساب</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  with st.container():
    st.markdown(
        """
            <div class="support-form-container">
                <div class="support-form-title">📋 استمارة تقديم طلب دعم فني</div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("support_form", clear_on_submit=False):
      name = st.text_input(
          "👤 الاسم ثلاثي / رباعي *",
          placeholder="أدخل اسمك بالكامل كما هو بالصحيفة",
      )

      col_f1, col_f2 = st.columns([1, 1])
      with col_f1:
        edara = st.selectbox("📍 الإدارة التعليمية *", EDARAT_LIST)
      with col_f2:
        job = st.selectbox("💼 الوظيفة الحالية *", JOBS_LIST)

      phone = st.text_input(
          "📱 رقم الموبايل (واتس آب للتواصل) *", placeholder="مثال: 01012345678"
      )

      problem = st.text_area(
          "📝 شرح المشكلة بالتفصيل *",
          placeholder="اكتب تفاصيل المشكلة أو الاستفسار بدقة...",
          height=120,
      )

      file_uploaded = st.file_uploader(
          "📑 إرفاق صحيفة أحوال إلكترونية حديثة (PDF أو صورة) *",
          type=["pdf", "png", "jpg", "jpeg"],
      )

      st.markdown("<br>", unsafe_allow_html=True)
      submitted = st.form_submit_button(
          "🚀 تجهيز الرسالة وتأكيد الطلب", use_container_width=True
      )

      if submitted:
        if not name or not phone or not problem or file_uploaded is None:
          st.error(
              "⚠️ يرجى استكمال كافة البيانات المطلوبة وإرفاق صحيفة الأحوال"
              " الإلكترونية."
          )
        else:
          st.session_state["form_data"] = {
              "name": name,
              "edara": edara,
              "job": job,
              "phone": phone,
              "problem": problem,
              "file_name": file_uploaded.name,
          }
          st.success(
              "🎉 تم تجهيز طلبك بنجاح! اختر أحد أرقام فريق الدعم بالأسفل"
              " للإرسال المباشر:"
          )

    if "form_data" in st.session_state and st.session_state["form_data"]:
      data = st.session_state["form_data"]

      msg_text = f"""*طلب دعم فني - منصة فرع الجيزة*
📌 *الاسم:* {data['name']}
📍 *الإدارة التعليمية:* {data['edara']}
💼 *الوظيفة الحالية:* {data['job']}
📱 *رقم التواصل:* {data['phone']}
📑 *صحيفة الأحوال:* مرفقة ({data['file_name']})

📝 *تفاصيل المشكلة:*
{data['problem']}"""

      encoded_msg = urllib.parse.quote(msg_text)

      st.markdown(
          "<br><h4 style='text-align: center; color: var(--text-color);'>📲"
          " اضغط على أحد الأرقام التالية للإرسال الفوري عبر الواتساب:</h4>",
          unsafe_allow_html=True,
      )

      whatsapp_numbers = [
          ("مسؤول الدعم (1)", "201069996245"),
          ("مسؤول الدعم (2)", "201120807631"),
          ("مسؤول الدعم (3)", "201201109892"),
      ]

      cols_wa = st.columns([1, 1, 1])
      for idx, (label, num) in enumerate(whatsapp_numbers):
        wa_url = f"https://wa.me/{num}?text={encoded_msg}"
        with cols_wa[idx]:
          st.markdown(
              f"""<a href="{wa_url}" target="_blank" class="whatsapp-card">
                            💬 {label}<br>
                            <span style="font-size: 0.85rem; opacity: 0.9;">({num.replace('20', '0')})</span>
                        </a>""",
              unsafe_allow_html=True,
          )

      st.info(
          "📌 **تنويه هام:** بعد فتح الواتساب، يرجى إعادة إرسال ملف صحيفة الأحوال"
          " الإلكترونية داخل شات المحادثة."
      )

    st.markdown("</div>", unsafe_allow_html=True)

  # 📍 قسم موقع/لوكيشن الفرع بالـ Pin المباشر على الأكاديمية
  st.markdown(
      f"""
        <div class="location-card-container">
            <h3 style="color: #C9A227; margin-top: 0; font-size: 1.4rem; margin-bottom: 12px;">📍 موقع فرع الأكاديمية المهنية للمعلمين بالجيزة</h3>
            <p style="color: var(--text-color); font-size: 1rem; margin-bottom: 18px;">
                يمكنكم زيارة مقر الفرع مباشرة أو فتح الخريطة عبر تطبيق خرائط جوجل من خلال الرابط أدناه:
            </p>
            <a href="{LOCATION_MAP_URL}" target="_blank" class="location-btn">
                🗺️ فتح الموقع في خرائط Google Maps
            </a>
            <div style="margin-top: 10px;">
                <iframe 
                    class="map-frame"
                    src="https://maps.google.com/maps?q=%D8%A7%D9%84%D8%A7%D9%83%D8%A7%D8%AF%D9%8A%D9%85%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D9%87%D9%8A%D8%A9%20%D9%84%D9%84%D9%85%D8%B9%D9%84%D9%85%D9%8A%D9%8BD%20%D9%81%D8%B1%D8%B9%20%D8%A7%D9%84%D8%AC%D9%8A%D8%B2%D8%A9&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

# باقي التبويبات
else:
  st.markdown(
      f"""
        <div class="centered-header">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{current_tab}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  st.info(f"قسم {current_tab} متاح وجاهز للإضافة والتخصيص.")

# ----------------- 🏛️ الختام (Footer) -----------------
st.markdown(
    """
    <div class="app-footer">
        تصميم وتنفيذ: <span>أحمد الجنزوري</span> - مدير الفرع
    </div>
""",
    unsafe_allow_html=True,
)
