import base64
import datetime
import os
import urllib.parse
import streamlit as st


# دالة قراءة وتحميل الصور المباشرة مع التخزين المؤقت لتسريع الأداء
@st.cache_data
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


# جلب اللوجو وتجهيز المتغيرات
browser_logo_icon = find_and_load_image("Logo.png", "🎓")

# 1️⃣ ضبط إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon=browser_logo_icon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

# 4️⃣ تصميم الأنماط (CSS) لشريط التنقل العلوي المطابق للصورة تماماً
st.markdown(
    """
    <style>
    footer { visibility: hidden !important; display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    [data-testid="stToolbarActions"] { display: none !important; }
    [data-testid="stActionButtonIcon"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }

    html, body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #060d1f !important;
        color: #ffffff !important;
    }

    .info-card-box {
        direction: rtl;
        text-align: right;
        background: linear-gradient(145deg, rgba(15, 32, 67, 0.95) 0%, rgba(8, 18, 41, 0.9) 100%) !important;
        backdrop-filter: blur(12px);
        color: #ffffff !important;
        padding: 30px 28px;
        border-radius: 22px;
        border: 1.5px solid rgba(201, 162, 39, 0.45);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 26px;
        height: 100% !important;
    }

    .info-card-box h3 {
        color: #FFD700 !important;
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        margin-top: 0;
        padding-bottom: 14px;
        border-bottom: 1.5px dashed rgba(201, 162, 39, 0.5);
    }

    .info-card-box p {
        font-size: 1.05rem !important;
        line-height: 1.85 !important;
        color: #f1f5f9 !important;
        font-weight: 500 !important;
    }

    .staff-item-badge {
        background: rgba(11, 26, 62, 0.8) !important;
        border: 1px solid rgba(201, 162, 39, 0.4) !important;
        border-right: 5px solid #FFD700 !important;
        border-radius: 12px !important;
        padding: 10px 14px !important;
        margin-bottom: 10px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }

    .highlight-name {
        color: #FFD700 !important;
        font-weight: 800 !important;
    }

    label[data-testid="stWidgetLabel"], .stWidgetLabel, label p {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }

    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {
        background-color: #0f2043 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(201, 162, 39, 0.45) !important;
    }

    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #C9A227 0%, #937B2B 100%) !important;
        color: #0b1a3e !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        border-radius: 12px !important;
        width: 100% !important;
    }

    /* تصميم شريط التنقل العلوي الاحترافي */
    .top-navbar {
        background: linear-gradient(135deg, #0b1a3e 0%, #101c38 100%) !important;
        backdrop-filter: blur(12px);
        padding: 12px 22px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: rtl;
        box-shadow: 0 6px 25px rgba(0,0,0,0.6);
        margin: 0 -1rem 15px -1rem;
        border-bottom: 3px solid #d4af37;
        flex-wrap: nowrap;
        gap: 15px;
    }

    .nav-right-container { 
        display: flex; 
        align-items: center; 
        gap: 12px; 
        flex-shrink: 0;
    }

    .nav-logo-text {
        color: #ffffff !important;
        font-weight: 800;
        font-size: 1.15rem;
        display: flex;
        align-items: center;
        gap: 10px;
        white-space: nowrap;
    }

    .navbar-logo-img {
        height: 45px;
        width: auto;
        border-radius: 6px;
        object-fit: contain;
        background: rgba(255, 255, 255, 0.08);
        padding: 3px;
        border: 1px solid rgba(201, 162, 39, 0.5);
    }

    .nav-center-tabs {
        display: flex;
        align-items: center;
        gap: 20px;
        flex-grow: 1;
        justify-content: center;
        flex-wrap: nowrap;
        overflow-x: auto;
    }

    .nav-tab-link {
        color: #ffffff !important;
        background: transparent;
        padding: 6px 4px;
        font-weight: 700;
        font-size: 1rem;
        text-decoration: none;
        white-space: nowrap;
        transition: all 0.25s ease;
        cursor: pointer;
        border-bottom: 2px solid transparent;
    }

    .nav-tab-link:hover, .nav-tab-link.active {
        color: #FFD700 !important;
        border-bottom-color: #FFD700 !important;
    }

    .nav-left-actions {
        display: flex;
        align-items: center;
        gap: 12px;
        flex-shrink: 0;
    }

    .teacher-platform-btn {
        background: linear-gradient(135deg, #b71c1c 0%, #7f0000 100%) !important;
        color: #ffffff !important;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.95rem;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(183, 28, 28, 0.4);
        border: 1.5px solid #FFD700;
        display: inline-block;
        text-align: center;
        white-space: nowrap !important;
    }

    .welcome-marquee-container {
        background: rgba(11, 26, 62, 0.7);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 14px;
        padding: 10px 15px;
        margin-bottom: 20px;
        overflow: hidden;
        white-space: nowrap;
    }

    .welcome-marquee-text {
        display: inline-block;
        color: #FFD700;
        font-weight: 800;
        font-size: 1.15rem;
        animation: marqueeAnim 22s linear infinite;
    }

    @keyframes marqueeAnim {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }

    .hero-banner {
        background: linear-gradient(135deg, rgba(11, 26, 62, 0.95) 0%, rgba(15, 32, 67, 0.85) 100%);
        border-radius: 18px;
        padding: 25px 15px;
        text-align: center !important;
        margin: 10px 0 25px 0;
        border: 1.5px solid rgba(201, 162, 39, 0.4);
    }

    .center-main-logo {
        height: 140px;
        width: auto;
        object-fit: contain;
        margin-bottom: 15px;
        display: inline-block;
        filter: drop-shadow(0px 8px 20px rgba(0,0,0,0.5));
    }

    .main-header-title {
        color: #ffffff !important;
        font-size: 1.85rem;
        font-weight: 800;
        display: inline-block;
        padding-bottom: 8px;
        border-bottom: 3px solid #C9A227;
        margin-bottom: 8px;
    }

    .sub-header-title {
        color: #94a3b8 !important;
        font-size: 1.02rem;
        font-weight: 500;
    }

    .section-title {
        text-align: center !important;
        color: #C9A227 !important;
        font-size: 1.75rem;
        font-weight: 800;
        margin-top: 40px;
        margin-bottom: 30px;
        padding-bottom: 10px;
        border-bottom: 2px dashed rgba(201, 162, 39, 0.4);
    }

    .program-card-wrapper {
        background: rgba(15, 32, 67, 0.6) !important;
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 18px;
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
        padding: 22px 18px;
        text-align: center !important;
    }

    .program-card-title {
        color: #C9A227 !important;
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .program-card-desc {
        color: #cbd5e1 !important;
        font-size: 0.96rem;
        line-height: 1.65;
    }

    .card-footer-badge {
        background: rgba(11, 26, 62, 0.8) !important;
        color: #FFD700 !important;
        text-align: center !important;
        padding: 10px;
        font-weight: bold;
        border: 1px solid rgba(201, 162, 39, 0.4);
        border-radius: 12px;
        margin-top: 8px;
        margin-bottom: 25px;
    }

    .staff-card {
        background: linear-gradient(145deg, rgba(15, 32, 67, 0.8) 0%, rgba(6, 13, 31, 0.9) 100%) !important;
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 24px;
        padding: 30px 20px;
        text-align: center !important;
        margin-bottom: 20px;
    }

    .avatar-frame {
        width: 140px;
        height: 140px;
        margin: 0 auto 18px auto;
        border-radius: 50%;
        border: 3.5px solid #C9A227;
        overflow: hidden;
        background-color: #0b1a3e;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .avatar-frame img { width: 100%; height: 100%; object-fit: cover !important; }
    .staff-name { color: #C9A227 !important; font-size: 1.28rem; font-weight: 800; margin-bottom: 8px; }
    .staff-role { color: #e2e8f0 !important; font-size: 1rem; font-weight: 600; margin-bottom: 10px; }
    .staff-dept {
        color: #FFD700 !important;
        font-size: 0.88rem;
        font-weight: bold;
        background: rgba(201, 162, 39, 0.18);
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
    }

    .edara-card {
        background: rgba(15, 32, 67, 0.7) !important;
        border: 1px solid rgba(201, 162, 39, 0.25);
        border-right: 5px solid #C9A227;
        border-radius: 12px;
        padding: 15px;
        text-align: center !important;
        font-weight: bold;
        color: #ffffff !important;
        margin-bottom: 14px;
    }

    .support-form-container {
        background: rgba(15, 32, 67, 0.85) !important;
        padding: 32px 28px;
        border-radius: 24px;
        border-top: 5px solid #C9A227;
        max-width: 900px;
        margin: 0 auto;
    }

    .support-form-title {
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 24px;
        border-bottom: 2px dashed rgba(201, 162, 39, 0.4);
        padding-bottom: 12px;
    }

    .location-card-container {
        background: rgba(15, 32, 67, 0.8) !important;
        border: 1.5px solid #C9A227;
        border-radius: 24px;
        padding: 28px 20px;
        max-width: 900px;
        margin: 35px auto 0 auto;
        text-align: center !important;
    }

    .location-btn {
        background: linear-gradient(135deg, #0b1a3e 0%, #1b2631 100%) !important;
        color: #FFD700 !important;
        padding: 12px 26px;
        border-radius: 14px;
        font-weight: bold;
        font-size: 1.05rem;
        text-decoration: none;
        display: inline-block;
        border: 1.5px solid #C9A227;
        margin-bottom: 20px;
    }

    .map-frame {
        width: 100%;
        height: 340px;
        border-radius: 16px;
        border: 2px solid #C9A227;
    }

    .whatsapp-card {
        display: block;
        text-align: center !important;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        font-weight: bold;
        padding: 15px 12px;
        border-radius: 14px;
        text-decoration: none;
        border: 1px solid #ffffff;
        margin-bottom: 12px;
    }

    .app-footer {
        margin-top: 50px;
        padding: 24px 0;
        background: linear-gradient(135deg, #4a3515 0%, #1e294b 50%, #040915 100%) !important;
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.05rem;
        font-weight: bold;
        border-top: 3.5px solid #d4af37;
        border-radius: 20px 20px 0 0;
    }
    
    .app-footer span { color: #FFD700; }
    </style>
""",
    unsafe_allow_html=True,
)

# 5️⃣ إدارة حالة التبويبات عبر الـ Query Params لتنقل فوري وسلس للغاية داخل نفس الصفحة
query_params = st.query_params
if "tab" in query_params:
  st.session_state["current_tab"] = query_params["tab"]

if "current_tab" not in st.session_state:
  st.session_state["current_tab"] = "الرئيسية"

current_tab = st.session_state["current_tab"]

tabs_list = [
    "الرئيسية",
    "عن الفرع",
    "ادارات الافراد",
    "الادارات التعليمية",
    "خدمات الأكاديمية",
    "أحدث التعليمات والقرارات",
    "مجتمعات التعلم",
    "التواصل مع الدعم",
]

# بناء روابط شريط التنقل العلوي الأفقية المماثلة للصورة
tabs_html_links = ""
for t_name in tabs_list:
  active_class = " active" if current_tab == t_name else ""
  tabs_html_links += (
      f'<a href="?tab={urllib.parse.quote(t_name)}" class="nav-tab-link'
      f'{active_class}">{t_name}</a>'
  )

# شريط التنقل العلوي المتكامل
st.markdown(
    f"""
    <div class="top-navbar">
        <div class="nav-right-container">
            <div class="nav-logo-text">
                {logo_navbar_tag}
                <span>الأكاديمية المهنية للمعلمين</span>
            </div>
        </div>
        <div class="nav-center-tabs">
            {tabs_html_links}
        </div>
        <div class="nav-left-actions">
            <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="teacher-platform-btn">منصة المٌعلم 🎓</a>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<hr style='margin-top: 5px; margin-bottom: 20px; border-color:"
    " rgba(201, 162, 39, 0.3);'>",
    unsafe_allow_html=True,
)

# تحميل الصور مرة واحدة مع التخزين المؤقت لتسريع الأداء
@st.cache_data
def get_cached_images():
  return {
      "leader_school": find_and_load_image(
          "leader_school.jpg",
          "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=800&auto=format&fit=crop",
      ),
      "leader_edu": find_and_load_image(
          "leader_edu.jpg",
          "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?q=80&w=800&auto=format&fit=crop",
      ),
      "leader_guidance": find_and_load_image(
          "leader_guidance.jpg",
          "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=800&auto=format&fit=crop",
      ),
      "teacher_assistant": find_and_load_image(
          "teacher_assistant.jpg",
          "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?q=80&w=800&auto=format&fit=crop",
      ),
      "teacher_skills": find_and_load_image(
          "teacher_skills.jpg",
          "https://images.unsplash.com/photo-1509062522246-3755977927d7?q=80&w=800&auto=format&fit=crop",
      ),
      "job": find_and_load_image(
          "job_change.jpg",
          "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800&auto=format&fit=crop",
      ),
      "tot": find_and_load_image(
          "tot.jpg",
          "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=800&auto=format&fit=crop",
      ),
      "ahmed": find_and_load_image(
          "ahmed.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
      ),
      "khaled": find_and_load_image(
          "khaled.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
      ),
      "omar": find_and_load_image(
          "omar.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
      ),
      "amina": find_and_load_image(
          "amina.jpg", "https://cdn-icons-png.flaticon.com/512/3135/3135789.png"
      ),
  }


imgs = get_cached_images()

# 1️⃣ الصفحة الرئيسية
if current_tab == "الرئيسية":
  st.markdown(
      """
        <div class="welcome-marquee-container">
            <div class="welcome-marquee-text">
                ✨ أهلاً وسهلاً بكم بفرع الأكاديمية المهنية للمعلمين بالجيزة ✨
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
            <div class="sub-header-title">البوابة الرقمية للخدمات والتدريبات والاعتماد المهني للمعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      '<div class="section-title">👑 برامج القيادات التربوية</div>',
      unsafe_allow_html=True,
  )
  c1, c2, c3 = st.columns([1, 1, 1])

  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{imgs['leader_school']}" alt="مدير ووكيل إدارة مدرسية"></div>
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer;">التسجيل بالبرنامج</button></a>',
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
                <div class="program-img-box"><img src="{imgs['leader_edu']}" alt="مدير ووكيل إدارة تعليمية"></div>
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer;">التسجيل بالبرنامج</button></a>',
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
                <div class="program-img-box"><img src="{imgs['leader_guidance']}" alt="أساسيات التوجيه الفني"></div>
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer;">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج أساسيات التوجيه الفني</div>',
        unsafe_allow_html=True,
    )

# 2️⃣ عن الفرع
elif current_tab == "عن الفرع":
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">عن فرع الأكاديمية المهنية للمعلمين بالجيزة</div>
            <div class="sub-header-title">مسيرة العطاء، التأسيس، والتطوير الرقمي لخدمة المعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      '<div class="section-title">🏛️ المحطات التاريخية والتأسيسية للفرع</div>',
      unsafe_allow_html=True,
  )

  c1, c2, c3 = st.columns([1, 1, 1])

  with c1:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>🏛️ التأسيس والانطلاقة</h3>
                <p>أُنشئ فرع الأكاديمية المهنية للمعلمين بمحافظة الجيزة في عام <b>2017</b> ليكون الحاضنة الرئيسية لتطوير وتمكين الكوادر التعليمية والتربوية بالمحافظة.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>📜 مرحلة البناء (2017 - 2023)</h3>
                <p>إرساء القواعد التنظيمية والإدارية تحت قيادة الأستاذة / <span class="highlight-name">أمل عبد المقصود</span>، بمعاونة فريق تكنولوجيا المعلومات.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>🚀 التطوير الرقمي (2023 - الآن)</h3>
                <p>انطلاقة الكترونية برئاسة الأستاذ / <span class="highlight-name">أحمد حسني الجنزوري</span> مديراً للفرع لميكنة وتيسير الخدمات.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

# 3️⃣ إدارات الأفراد
elif current_tab == "ادارات الافراد":
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">إدارات الأفراد - الهيكل الإداري</div>
            <div class="sub-header-title">قيادات وكوادر الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  c1, c2, c3, c4 = st.columns([1, 1, 1, 1])

  with c1:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{imgs['ahmed']}" alt="أحمد حسني الجنزوري"></div>
                <div class="staff-name"><span class="highlight-name">أحمد حسني الجنزوري</span></div>
                <div class="staff-role">👔 مدير الفرع</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{imgs['khaled']}" alt="خالد عبدالحكيم هارون"></div>
                <div class="staff-name"><span class="highlight-name">خالد عبدالحكيم هارون</span></div>
                <div class="staff-role">🤝 مسئول الموارد البشرية</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{imgs['omar']}" alt="أحمد محمد عمر"></div>
                <div class="staff-name"><span class="highlight-name">أحمد محمد عمر</span></div>
                <div class="staff-role">🎯 مسئول التنمية المهنية</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c4:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{imgs['amina']}" alt="أمينة فوزي عبدالرحمن"></div>
                <div class="staff-name"><span class="highlight-name">أمينة فوزي عبدالرحمن</span></div>
                <div class="staff-role">🎯 مسئول التنمية المهنية</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

# 4️⃣ الإدارات التعليمية
elif current_tab == "الادارات التعليمية":
  st.markdown(
      f"""
        <div class="hero-banner">
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
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">خدمات الأكاديمية المهنية للمعلمين</div>
            <div class="sub-header-title">دليل الخدمات والتسجيل الرقمي المتاح لجميع أعضاء هيئة التعليم</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="support-form-container" style="text-align: center;">
            <p style="font-size: 1.15rem; line-height: 1.9; color: #ffffff;">
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

# 6️⃣ أحدث التعليمات والقرارات
elif current_tab == "أحدث التعليمات والقرارات":
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">أحدث التعليمات والقرارات التنظيمية</div>
            <div class="sub-header-title">الكتب الوزارية، النشرات الدورية، والقرارات الصادرة عن الأكاديمية</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="info-card-box">
            <h3>📌 التعليمات التنفيذية لملفات الترقي والتسكين</h3>
            <p>تابِع أحدث التعليمات الواردة من الإدارة العامة لصلاحية الترقي بشأن استيفاء ملفات الإنجاز واختبارات التنمية المهنية.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 7️⃣ مجتمعات التعلم
elif current_tab == "مجتمعات التعلم":
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">مجتمعات التعلم المهنية (PLCs)</div>
            <div class="sub-header-title">منصة التعاون المهني وتبادل الخبرات بين المعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )
  st.markdown(
      """
        <div class="info-card-box">
            <h3>🌐 ما هي مجتمعات التعلم المهنية؟</h3>
            <p>بيئة تربوية تفاعلية تجمع المعلمين والموجهين والقيادات في فرق عمل تعاونية منظمة لتطوير مهارات التدريس.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 8️⃣ التواصل مع الدعم
elif current_tab == "التواصل مع الدعم":
  st.markdown(
      f"""
        <div class="hero-banner">
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
          "<br><h4 style='text-align: center; color: #ffffff;'>📲 اضغط على أحد"
          " الأرقام التالية للإرسال الفوري عبر الواتساب:</h4>",
          unsafe_allow_html=True,
      )

      whatsapp_numbers = [
          ("مسؤول الدعم (1)", "201069996245"),
          ("مسؤول الدعم (2)", "201120807631"),
          ("مسؤول الدعم التكنولوجي", "201201109892"),
      ]

      cols_wa = st.columns([1, 1, 1])
      for idx, (label, num) in enumerate(whatsapp_numbers):
        wa_url = f"https://wa.me/{num}?text={encoded_msg}"
        with cols_wa[idx]:
          st.markdown(
              f"""<a href="{wa_url}" target="_blank" class="whatsapp-card">
                            💬 {label}<br>
                            <span style="font-size: 0.85rem; opacity: 0.95;">({num.replace('20', '0')})</span>
                        </a>""",
              unsafe_allow_html=True,
          )

    st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      f"""
        <div class="location-card-container">
            <h3 style="color: #C9A227; margin-top: 0; font-size: 1.45rem; margin-bottom: 14px;">📍 موقع فرع الأكاديمية المهنية للمعلمين بالجيزة</h3>
            <p style="color: #cbd5e1; font-size: 1.02rem; margin-bottom: 20px;">
                يمكنكم زيارة مقر الفرع مباشرة أو فتح الخريطة عبر تطبيق خرائط جوجل من خلال الرابط أدناه:
            </p>
            <a href="{LOCATION_MAP_URL}" target="_blank" class="location-btn">
                🗺️ فتح الموقع في خرائط Google Maps
            </a>
            <div style="margin-top: 10px;">
                <iframe 
                    class="map-frame"
                    src="https://maps.google.com/maps?q=%D8%A7%D9%84%D8%A7%D9%83%D8%A7%D8%AF%D9%8A%D9%85%D9%8A%20%D8%A7%D9%84%D9%85%D9%87%D9%8A%20%D9%84%D9%84%D9%85%D8%B9%D9%84%D9%85%D9%8A%20%D9%81%D8%B1%D8%B9%20%D8%A7%D9%84%D8%AC%D9%8A%20%D8%B2%D8%A9&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

# الختام (Footer)
st.markdown(
    """
    <div class="app-footer">
        تصميم وتنفيذ: <span>أحمد الجنزوري</span> - مدير الفرع
    </div>
""",
    unsafe_allow_html=True,
)
