import base64
import datetime
import os
import urllib.parse
import streamlit as st


# دالة قراءة وتحميل الصور المباشرة
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

# 4️⃣ تصميم الأنماط (CSS) مع تحديث شكل الشريط العلوي والتبويبات المطابقة للصورة
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
        transition: all 0.3s ease;
        height: 100% !important;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .info-card-box:hover {
        border-color: #FFD700;
        box-shadow: 0 14px 35px rgba(201, 162, 39, 0.3);
        transform: translateY(-4px);
    }

    .info-card-box h3 {
        color: #FFD700 !important;
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        margin-top: 0;
        padding-bottom: 14px;
        border-bottom: 1.5px dashed rgba(201, 162, 39, 0.5);
        white-space: nowrap !important;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .info-card-box p {
        font-size: 1.05rem !important;
        line-height: 1.85 !important;
        color: #f1f5f9 !important;
        font-weight: 500 !important;
        margin-bottom: 15px;
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
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.25s ease !important;
        white-space: nowrap !important;
    }

    .staff-item-badge:hover {
        transform: translateX(-4px) !important;
        background: rgba(201, 162, 39, 0.15) !important;
        border-color: #FFD700 !important;
    }

    .highlight-name {
        color: #FFD700 !important;
        font-weight: 800 !important;
    }

    label[data-testid="stWidgetLabel"], .stWidgetLabel, label p {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
    }

    div[data-baseweb="input"] input, textarea {
        color: #ffffff !important;
        font-size: 1rem !important;
        background-color: #0f2043 !important;
    }

    ::placeholder, ::-webkit-input-placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }

    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {
        background-color: #0f2043 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(201, 162, 39, 0.45) !important;
    }

    div[data-baseweb="input"] > div:focus-within, textarea:focus {
        border-color: #FFD700 !important;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.35) !important;
    }

    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #C9A227 0%, #937B2B 100%) !important;
        color: #0b1a3e !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        border-radius: 12px !important;
        border: 1px solid #ffffff !important;
        padding: 12px 20px !important;
        box-shadow: 0 6px 20px rgba(201, 162, 39, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #FFD700 0%, #C9A227 100%) !important;
        color: #000000 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.6) !important;
    }

    div[data-testid="stFileUploader"] {
        background-color: #0f2043 !important;
        border-radius: 14px !important;
        border: 1.5px dashed #C9A227 !important;
        padding: 12px !important;
    }

    div[data-testid="stFileUploaderDropzone"] {
        background-color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #C9A227 !important;
    }

    div[data-testid="stFileUploaderDropzone"] span, 
    div[data-testid="stFileUploaderDropzone"] div,
    div[data-testid="stFileUploaderDropzoneInstructions"] {
        color: #0b1a3e !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }

    div[data-testid="stFileUploaderDropzone"] button {
        background: linear-gradient(135deg, #0b1a3e 0%, #172a4d 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: 1px solid #C9A227 !important;
        border-radius: 8px !important;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stFileUploaderDropzone"] button:hover {
        background: #C9A227 !important;
        color: #0b1a3e !important;
    }

    /* تصميم شريط التنقل العلوي المطابق للصورة */
    .top-navbar {
        background: linear-gradient(135deg, #0b1a3e 0%, #101c38 100%) !important;
        backdrop-filter: blur(12px);
        padding: 14px 22px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: rtl;
        box-shadow: 0 6px 25px rgba(0,0,0,0.6);
        margin: 0 -1rem 20px -1rem;
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
        gap: 18px;
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
        transition: all 0.3s ease;
        white-space: nowrap !important;
    }
    
    .teacher-platform-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(183, 28, 28, 0.7);
    }

    .welcome-marquee-container {
        background: rgba(11, 26, 62, 0.7);
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-radius: 14px;
        padding: 10px 15px;
        margin-bottom: 20px;
        overflow: hidden;
        white-space: nowrap;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.4);
    }

    .welcome-marquee-text {
        display: inline-block;
        color: #FFD700;
        font-weight: 800;
        font-size: 1.15rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
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
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
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
        text-align: center !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.4);
        margin-bottom: 8px;
    }

    .sub-header-title {
        color: #94a3b8 !important;
        font-size: 1.02rem;
        font-weight: 500;
        text-align: center !important;
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
        backdrop-filter: blur(8px);
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        transition: all 0.35s ease;
    }

    .program-card-wrapper:hover {
        transform: translateY(-6px);
        border-color: #C9A227;
        box-shadow: 0 14px 32px rgba(201, 162, 39, 0.3);
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
        transition: transform 0.6s ease;
    }

    .program-card-wrapper:hover .program-img-box img {
        transform: scale(1.08);
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
        font-size: 0.92rem;
    }

    .staff-card {
        background: linear-gradient(145deg, rgba(15, 32, 67, 0.8) 0%, rgba(6, 13, 31, 0.9) 100%) !important;
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 24px;
        padding: 30px 20px;
        text-align: center !important;
        box-shadow: 0 10px 26px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        transition: all 0.35s ease;
    }

    .staff-card:hover {
        transform: translateY(-5px);
        border-color: #C9A227;
        box-shadow: 0 14px 32px rgba(201, 162, 39, 0.25);
    }

    .avatar-frame {
        width: 140px;
        height: 140px;
        margin: 0 auto 18px auto;
        border-radius: 50%;
        border: 3.5px solid #C9A227;
        box-shadow: 0 0 20px rgba(201, 162, 39, 0.4);
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
        border: 1px solid rgba(201, 162, 39, 0.4);
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
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 14px;
        font-size: 0.98rem;
        transition: all 0.25s ease;
    }

    .edara-card:hover {
        transform: scale(1.03);
        border-color: #C9A227;
        background: rgba(201, 162, 39, 0.2) !important;
    }

    .support-form-container {
        background: rgba(15, 32, 67, 0.85) !important;
        backdrop-filter: blur(12px);
        padding: 32px 28px;
        border-radius: 24px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
        border-top: 5px solid #C9A227;
        border-right: 1px solid rgba(201, 162, 39, 0.3);
        border-left: 1px solid rgba(201, 162, 39, 0.3);
        max-width: 900px;
        margin: 0 auto;
    }

    .support-form-title {
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 24px;
        padding-bottom: 12px;
        border-bottom: 2px dashed rgba(201, 162, 39, 0.4);
    }

    .location-card-container {
        background: rgba(15, 32, 67, 0.8) !important;
        border: 1.5px solid #C9A227;
        border-radius: 24px;
        padding: 28px 20px;
        max-width: 900px;
        margin: 35px auto 0 auto;
        text-align: center !important;
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
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
        box-shadow: 0 4px 16px rgba(0,0,0,0.25);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }

    .location-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(201, 162, 39, 0.4);
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
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.35);
        transition: all 0.3s ease;
    }

    .whatsapp-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.55);
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
        box-shadow: 0 -8px 25px rgba(0,0,0,0.4);
    }
    
    .app-footer span { color: #FFD700; }

    @media (max-width: 992px) {
        .top-navbar {
            flex-direction: column;
            align-items: stretch;
            gap: 12px;
        }
        .nav-center-tabs {
            justify-content: flex-start;
            overflow-x: auto;
            padding-bottom: 5px;
        }
        .nav-left-actions {
            justify-content: space-between;
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 5️⃣ إدارة حالة التبويبات ونظام استقبال التغيير عبر Query Parameters لتعمل بسلاسة داخل نفس الصفحة
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

# بناء روابط التبويبات الأفقية المطابقة للصورة تماماً
tabs_html_links = ""
for t_name in tabs_list:
  active_class = " active" if current_tab == t_name else ""
  tabs_html_links += (
      f'<a href="?tab={urllib.parse.quote(t_name)}" class="nav-tab-link'
      f'{active_class}">{t_name}</a>'
  )

# شريط التنقل العلوي المتكامل (اللوجو يميناً، الروابط في المنتصف، زر منصة المعلم يساراً)
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

# تحميل صور البرامج المخصصة
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج أساسيات التوجيه الفني</div>',
        unsafe_allow_html=True,
    )

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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card-footer-badge">برنامج مهارات عامة في التدريس</div>',
        unsafe_allow_html=True,
    )

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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
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
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        ' color:white; font-weight:bold; border:none; padding:11px;'
        ' cursor:pointer; box-shadow: 0 4px 12px'
        ' rgba(178,34,34,0.4);">التسجيل بالبرنامج</button></a>',
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
                <p>
                    أُنشئ فرع الأكاديمية المهنية للمعلمين بمحافظة الجيزة في عام <b>2017</b> ليكون الحاضنة الرئيسية لتطوير وتمكين الكوادر التعليمية والتربوية بالمحافظة، وتقديم الخدمات الاعتمادية والتدريبية وفق أعلى معايير الجودة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>📜 مرحلة البناء (2017 - 2023)</h3>
                <p>
                    شهدت إرساء القواعد التنظيمية والإدارية للفرع تحت قيادة الأستاذة / <span class="highlight-name">أمل عبد المقصود</span> (مدير الفرع)، بمعاونة فريق تكنولوجيا المعلومات:
                </p>
                <div class="staff-item-badge">
                    💻 <span class="highlight-name">أ . أحمد حسني الجنزوري</span> (IT)
                </div>
                <div class="staff-item-badge">
                    💻 <span class="highlight-name">أ . خالد عبد الحكيم هارون</span> (IT)
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>🚀 التطوير الرقمي (2023 - الآن)</h3>
                <p>
                    انطلاقة الكترونية برئاسة الأستاذ / <span class="highlight-name">أحمد حسني الجنزوري</span> مديراً للفرع، لميكنة الخدمات وتيسير البرامج بالتعاون مع فريق العمل:
                </p>
                <div class="staff-item-badge">
                    🤝 <span class="highlight-name">أ . خالد عبد الحكيم</span> (موارد بشرية و IT)
                </div>
                <div class="staff-item-badge">
                    🎯 <span class="highlight-name">أ . أحمد محمد عمر</span> (التنمية المهنية)
                </div>
                <div class="staff-item-badge">
                    🎯 <span class="highlight-name">أ . أمينة فوزي</span> (التنمية المهنية)
                </div>
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
      '<div class="section-title">🎓 البرامج الاعتمادية والتأهيلية</div>',
      unsafe_allow_html=True,
  )
  s1, s2 = st.columns([1, 1])
  with s1:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>🌟 برامج الترقي للكادر الوظيفي</h3>
                <p>
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
                <h3>👑 برامج القيادات التربوية</h3>
                <p>
                    تأهيل الكوادر التربوية لشغل وظائف (مدير ووكيل إدارة مدرسية، مدير ووكيل إدارة تعليمية، أساسيات التوجيه الفني) والحصول على شهادات التنمية المهنية المعتمدة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(
      '<div class="section-title">📜 الاعتماد وتغيير المسمى الوظيفي</div>',
      unsafe_allow_html=True,
  )
  s3, s4 = st.columns([1, 1])
  with s3:
    st.markdown(
        """
            <div class="info-card-box">
                <h3>🔄 تغيير المسمى الوظيفي</h3>
                <p>
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
                <h3>💼 اعتماد المدربين والمراكز (TOT)</h3>
                <p>
                    منح شهادات الاعتماد الرقمية للمدربين المعتمدين (TOT)، واعتماد برامج التنمية المهنية المستمرة والمؤسسات التدريبية وفق معايير الجودة الشاملة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(
      '<div class="section-title">📝 التقدم للبرامج مدفوعة الأجر</div>',
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
            <div class="sub-header-title">الكتب الوزارية، النشرات الدورية، والقرارات الصادرة عن الأكاديمية المهنية للمعلمين</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="info-card-box">
            <h3>📌 التعليمات التنفيذية لملفات الترقي والتسكين</h3>
            <p>
                تابِع أحدث التعليمات الواردة من الإدارة العامة لصلاحية الترقي بشأن استيفاء ملفات الإنجاز، واختبارات التنمية المهنية، والمدد البينية اللازمة للترقي على الكادر الوظيفي لجميع الإدارات التعليمية بالجيزة.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="info-card-box">
            <h3>📜 ضوابط شروط التقدم لبرامج القيادات التربوية</h3>
            <p>
                تم اعتماد الشروط والخطوات التنفيذية للتقدم لبرامج (مدير ووكيل إدارة مدرسية، مدير ووكيل إدارة تعليمية، والتوجيه الفني) عبر منصة المعلم الرقمية وفقاً للكتب الدوريّة المنظمة.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="info-card-box">
            <h3>🔄 شروط وإجراءات تغيير المسمى الوظيفي</h3>
            <p>
                التعليمات الخاصة بالمؤهلات الحاصل عليها أعضاء هيئة التعليم الراغبين في تعديل المسمى الوظيفي وفقاً للقانون رقم 155 لسنة 2007 وتعديلاته.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="support-form-container" style="text-align: center;">
            <p style="font-size: 1.15rem; line-height: 1.9; color: #ffffff;">
                للاطلاع على النصوص الكاملة للقرارات والتعاميم الرسمية وتنزيل النشرات بصيغة PDF، يرجى زيارة الموقع الرسمي أو متابعة صفحة الفيسبوك الرسمية لفرع الأكاديمية المهنية للمعلمين.
            </p>
            <br>
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <a href="https://www.pat.edu.eg" target="_blank" class="location-btn" style="text-decoration: none; margin-bottom: 0;">
                    🌐 زيارة الموقع الرسمي للأكاديمية
                </a>
                <a href="{FACEBOOK_PAGE_URL}" target="_blank" class="location-btn" style="text-decoration: none; background: linear-gradient(135deg, #1877F2 0%, #0a52b2 100%) !important; color: white !important; border-color: #1877F2 !important; margin-bottom: 0;">
                    📘 زيارة صفحة فيسبوك الفرع
                </a>
            </div>
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
            <div class="sub-header-title">منصة التعاون المهني وتبادل الخبرات بين المعلمين والقيادات التربوية بفرع الجيزة</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="info-card-box">
            <h3>🌐 ما هي مجتمعات التعلم المهنية؟</h3>
            <p>
                هي بيئة تربوية تفاعلية تجمع المعلمين والموجهين والقيادات في فرق عمل تعاونية منظمة، تهدف إلى <b>تطوير مهارات التدريس</b>، و<b>تبادل الممارسات المتميزة</b>، و<b>حل المشكلات التعليمية</b> للارتقاء بنواتج تعلم الطلاب والتحول نحو مجتمع المعرفة.
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      '<div class="section-title">🎯 الأهداف الرائدة لمجتمعات التعلم</div>',
      unsafe_allow_html=True,
  )
  p1, p2, p3 = st.columns([1, 1, 1])

  with p1:
    st.markdown(
        """
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0; white-space: nowrap;">🤝 تعزيز العمل الجماعي</h4>
                <p style="font-size: 1rem;">
                    بناء ثقافة العمل بروح الفريق الواحد بين المعلمين والموجهين داخل المدرسة وعلى مستوى الإدارة التعليمية.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with p2:
    st.markdown(
        """
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0; white-space: nowrap;">💡 الابتكار وتبادل الخبرات</h4>
                <p style="font-size: 1rem;">
                    نقل وتطبيق أحدث استراتيجيات التدريس وتقنيات التحول الرقمي والتفكير النقدي في الفصول الدراسية.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with p3:
    st.markdown(
        """
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0; white-space: nowrap;">📈 النمو المهني المستمر</h4>
                <p style="font-size: 1rem;">
                    التطوير الذاتي والتنفيذي للكوادر التعليمية من خلال البحوث الإجرائية وتبادل الملاحظات والتغذية الراجعة.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(
      '<div class="section-title">📚 أوعية وأنشطة مجتمعات التعلم بفرع الجيزة</div>',
      unsafe_allow_html=True,
  )
  a1, a2 = st.columns([1, 1])

  with a1:
    st.markdown(
        """
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0; white-space: nowrap;">🔍 بحث الدرس (Lesson Study) وتدريب الأقران</h4>
                <p>
                    التخطيط المشترك للدروس وتجريب التنسيقات الحديثة في مواقف تعليمية واقعية، يليها جلسات تأمل وتبادل التغذية الراجعة البناءة بين المعلمين ورؤساء الأقسام.
                </p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  with a2:
    st.markdown(
        """
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0; white-space: nowrap;">🖥️ الشبكات والورش الرقمية التفاعلية</h4>
                <p>
                    لقاءات دورية وندوات عبر الإنترنت للربط بين المعلمين والمشرفين عبر مختلف الإدارات التعليمية بالجيزة لعرض التجارب والحلول المبتكرة للتحديات الصفية.
                </p>
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
          ("مسؤول الدعم (3)", "201201109892"),
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

      st.info(
          "📌 **تنويه هام:** بعد فتح الواتساب، يرجى إعادة إرسال ملف صحيفة الأحوال"
          " الإلكترونية داخل شات المحادثة."
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
                    src="https://maps.google.com/maps?q=%D8%A7%D9%84%D8%A7%D9%83%D8%A7%D8%AF%D9%8A%D9%85%D9%8A%20%D8%A7%D9%84%D9%85%D9%87%D9%8A%20%D9%84%D9%84%D9%85%D8%B9%D9%84%D9%85%D9%8A%D9%8BD%20%D9%81%D8%B1%D8%B9%20%D8%A7%D9%84%D8%AC%D9%8A%D8%B2%D8%A9&t=&z=16&ie=UTF8&iwloc=&output=embed" 
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
