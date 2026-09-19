import base64
import os
import urllib.parse
import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


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


# قائمة الإدارات والوظائف
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

# تحضير اللوجو ورابط الفيسبوك
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

# تطبيق التنسيقات (CSS)
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

# إدارة حالة التبويبات
if "current_tab" not in st.session_state:
  st.session_state["current_tab"] = "الرئيسية"

# الشريط العلوي
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

for idx, name in enumerate(tabs_names):
  with cols[idx]:
    if st.button(name, key=f"tab_btn_{idx}", use_container_width=True):
      st.session_state["current_tab"] = name

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

# 📸 تحميل صورة لكل برنامج بشكل منفصل
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
  c1, c2, c3 = st.columns(3)

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
  c1, c2 = st.columns(2)
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
  c1, c2 = st.columns(2)
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

# الختام
st.markdown(
    """
    <div class="app-footer">
        تصميم وتنفيذ: <span>أحمد الجنزوري</span> - مدير الفرع
    </div>
""",
    unsafe_allow_html=True,
)
