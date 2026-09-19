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
EDARAT_LIST_AR = [
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

EDARAT_LIST_EN = [
    "Abu Nomros",
    "Atfih",
    "October",
    "Oseem",
    "Al-Badrashein",
    "Al-Hawamdeya",
    "Dokki",
    "General Diwan",
    "Sheikh Zayed",
    "Al-Saff",
    "Agouza",
    "Omrania",
    "Al-Haram",
    "Bahariya Oases",
    "Al-Warrag",
    "Bulaq Dakrour",
    "South Giza",
    "Hadayek October",
    "Directorate Diwan",
    "North Giza",
    "Kerdasa",
    "Monshaat El-Qanater",
]

JOBS_LIST_AR = [
    "معلم مساعد",
    "معلم",
    "معلم أول",
    "معلم أول أ",
    "معلم خبير",
    "كبير معلمين",
]

JOBS_LIST_EN = [
    "Assistant Teacher",
    "Teacher",
    "First Teacher",
    "Senior Teacher A",
    "Expert Teacher",
    "Master Teacher",
]

logo_src = find_and_load_image(
    "Logo.png", "https://via.placeholder.com/220x220?text=PAT+Logo"
)
logo_navbar_tag = (
    f'<img src="{logo_src}" class="navbar-logo-img" alt="Logo">'
    if logo_src
    else ""
)
logo_header_tag = (
    f'<img src="{logo_src}" class="center-main-logo" alt="Academy Logo">'
    if logo_src
    else ""
)
FACEBOOK_PAGE_URL = "https://www.facebook.com/share/18PF695ehm/"
LOCATION_MAP_URL = "https://maps.app.goo.gl/RVpBuBNVfHFnr7qz9"

# 4️⃣ إدارة حالة اللغة الحالية للمنصة
if "language" not in st.session_state:
  st.session_state["language"] = "ar"

lang = st.session_state["language"]
is_ar = lang == "ar"

# نصوص مترجمة ديناميكياً حسب اللغة
TEXTS = {
    "ar": {
        "page_title": "الأكاديمية المهنية للمعلمين - فرع الجيزة",
        "nav_title": "الأكاديمية المهنية للمعلمين - فرع الجيزة",
        "platform_btn": "منصة المعلم 🎓",
        "lang_btn": "🇺🇸 English",
        "tabs": [
            "الرئيسية",
            "عن الفرع",
            "ادارات الافراد",
            "الادارات التعليمية",
            "خدمات الأكاديمية",
            "مجتمعات التعلم",
            "التواصل مع الدعم",
        ],
        "hero_title": "الأكاديمية المهنية للمعلمين - فرع الجيزة",
        "hero_sub": (
            "البوابة الرقمية للخدمات والتدريبات والاعتماد المهني للمعلمين"
        ),
        "sec_leaders": "👑 برامج القيادات التربوية",
        "prog_leader_school": "برنامج مدير ووكيل إدارة مدرسية",
        "prog_leader_school_desc": (
            "أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية"
            " للمعلمين المتاحة للفئات المستهدفة."
        ),
        "prog_leader_edu": "برنامج مدير ووكيل إدارة تعليمية",
        "prog_leader_edu_desc": (
            "إعداد وتأهيل القيادات للإدارات التعليمية لتطوير المهارات القيادية"
            " والإدارية."
        ),
        "prog_leader_guidance": "برنامج أساسيات التوجيه الفني",
        "prog_leader_guidance_desc": (
            "تمكين الموجهين الفنيين من المهارات الأساسية للإشراف ومتابعة الأداء"
            " التعليمي."
        ),
        "register_btn": "التسجيل بالبرنامج",
        "sec_promotion": "📜 برامج التسكين والترقي",
        "prog_teacher_assistant": "برنامج التطبيقات التربوية للمعلم المساعد",
        "prog_teacher_assistant_desc": (
            "تأهيل المعلمين المساعدين لاستكمال متطلبات التسكين على الكادر"
            " الوظيفي."
        ),
        "prog_teacher_skills": "برنامج مهارات عامة في التدريس",
        "prog_teacher_skills_desc": (
            "تطوير مهارات واستراتيجيات التدريس الحديثة للمعلمين المستحقين للترقية."
        ),
        "sec_job_change": "🔄 برامج تغيير المسمى الوظيفي والاعتماد",
        "prog_job_change": "برنامج تغيير المسمى الوظيفي",
        "prog_job_change_desc": (
            "برنامج معتمد لإعادة التأهيل التربوي والتخصصي لمطابقة التخصصات"
            " والتسكين الوظيفي."
        ),
        "prog_tot": "البرنامج الرقمي للاعتماد (TOT)",
        "prog_tot_desc": (
            "دورة تدريب المدربين الرقمية لتأهيل وإعداد مدربين معتمدين وفق معايير"
            " الجودة."
        ),
        "about_title": "عن فرع الأكاديمية المهنية للمعلمين بالجيزة",
        "about_sub": "مسيرة العطاء، التأسيس، والتطوير الرقمي لخدمة المعلمين",
        "about_box1_title": "🏛️ التأسيس والانطلاقة (2017)",
        "about_box1_text": (
            'أُنشئ فرع الأكاديمية المهنية للمعلمين بمحافظة الجيزة في عام <b>2017</b>'
            ' ليكون الحاضنة الرئيسية لتطوير وتمكين الكوادر التعليمية والتربوية'
            ' بالمحافظة، وتقديم الخدمات الاعتمادية والتدريبية وفق أعلى معايير'
            ' الجودة.'
        ),
        "about_box2_title": "📜 مرحلة البناء والتأسيس (2017 – 2023)",
        "about_box2_text": (
            'شهدت الفترة من <b>2017 حتى 2023</b> إرساء القواعد التنظيمية والإدارية'
            ' للفرع تحت قيادة الأستاذة / <span class="highlight-name">أمل عبد'
            ' المقصود</span> (مدير الفرع)، وبمعاونة فريق عمل متميز في قسم تكنولوجيا'
            ' المعلومات (IT) ضم كلاً من:'
        ),
        "about_box3_title": "🚀 مرحلة التطوير والتحول الرقمي (2023 – حتى الآن)",
        "about_box3_text": (
            'مع بداية عام <b>2023</b>، انطلقت مرحلة جديدة ترتكز على <b>الميكنة'
            ' والتحول الرقمي للخدمات</b>، برئاسة الأستاذ / <span'
            ' class="highlight-name">أحمد حسني الجنزوري</span> مديراً للفرع، وفريق'
            ' عمل متميز يتكون من:'
        ),
        "about_box3_footer": (
            "تتضافر الجهود حالياً لتسهيل حصول المعلمين على البرامج الرقمية"
            " للقيادات والترقي وتغيير المسمى الوظيفي والدعم الفني المباشر لجميع"
            " الإدارات التعليمية بمحافظة الجيزة."
        ),
        "staff_title": "إدارات الأفراد - الهيكل الإداري",
        "staff_sub": "قيادات وكوادر الأكاديمية المهنية للمعلمين - فرع الجيزة",
        "staff1_role": "👔 مدير الفرع",
        "staff2_role": "🤝 مسئول الموارد البشرية",
        "staff3_role": "🎯 مسئول التنمية المهنية",
        "staff4_role": "🎯 مسئول التنمية المهنية",
        "edara_title": "الإدارات التعليمية - محافظة الجيزة",
        "edara_sub": "دليل الإدارات التعليمية والديوان التابعة لفرع الجيزة",
        "services_title": "خدمات الأكاديمية المهنية للمعلمين",
        "services_sub": (
            "دليل الخدمات والتسجيل الرقمي المتاح لجميع أعضاء هيئة التعليم"
        ),
        "serv1_title": "🌟 برامج الترقي للكادر الوظيفي",
        "serv1_desc": (
            "تقديم التدريبات الرقمية المعتمدة لاستكمال متطلبات الترقي للمعلمين"
            " المستحقين بالنظام الإلكتروني الحديث، ومتابعة رفع واستيفاء ملفات"
            " الترقي بالتعاون مع الإدارات التعليمية."
        ),
        "serv2_title": "👑 برامج القيادات التربوية",
        "serv2_desc": (
            "تأهيل الكوادر التربوية لشغل وظائف (مدير ووكيل إدارة مدرسية، مدير"
            " ووكيل إدارة تعليمية، أساسيات التوجيه الفني) والحصول على شهادات"
            " التنمية المهنية المعتمدة."
        ),
        "serv3_title": "🔄 تغيير المسمى الوظيفي",
        "serv3_desc": (
            "استقبال وتدقيق أوراق المعلمين الراغبين في تغيير المسمى الوظيفي،"
            " وتوفير برامج إعادة التأهيل التربوي والتخصصي المعتمدة لمطابقة"
            " المؤهلات والتسكين الصحيح."
        ),
        "serv4_title": "💼 اعتماد المدربين والمراكز (TOT)",
        "serv4_desc": (
            "منح شهادات الاعتماد الرقمية للمدربين المعتمدين (TOT)، واعتماد برامج"
            " التنمية المهنية المستمرة والمؤسسات التدريبية وفق معايير الجودة"
            " الشاملة."
        ),
        "serv_paid_title": "📝 التقدم للبرامج مدفوعة الأجر",
        "serv_paid_desc": (
            "تتيح الأكاديمية المهنية للمعلمين بفرع الجيزة إمكانية التقدم والتسجيل"
            " الإلكتروني المباشر للبرامج التدريبية مدفوعة الأجر والخاصة بالترقي"
            " والاعتماد وتطوير المهارات."
        ),
        "serv_paid_btn": (
            "🌐 الانتقال إلى منصة التقديم والتسجيل في البرامج"
        ),
        "plc_title": "مجتمعات التعلم المهنية (PLCs)",
        "plc_sub": (
            "منصة التعاون المهني وتبادل الخبرات بين المعلمين والقيادات التربوية"
            " بفرع الجيزة"
        ),
        "plc_what": "🌐 ما هي مجتمعات التعلم المهنية؟",
        "plc_what_desc": (
            "هي بيئة تربوية تفاعلية تجمع المعلمين والموجهين والقيادات في فرق"
            " عمل تعاونية منظمة، تهدف إلى <b>تطوير مهارات التدريس</b>،"
            " و<b>تبادل الممارسات المتميزة</b>، و<b>حل المشكلات التعليمية</b>"
            " للارتقاء بنواتج تعلم الطلاب والتحول نحو مجتمع المعرفة."
        ),
        "plc_goals": "🎯 الأهداف الرائدة لمجتمعات التعلم",
        "plc_g1": "🤝 تعزيز العمل الجماعي",
        "plc_g1_desc": (
            "بناء ثقافة العمل بروح الفريق الواحد بين المعلمين والموجهين داخل"
            " المدرسة وعلى مستوى الإدارة التعليمية."
        ),
        "plc_g2": "💡 الابتكار وتبادل الخبرات",
        "plc_g2_desc": (
            "نقل وتطبيق أحدث استراتيجيات التدريس وتقنيات التحول الرقمي والتفكير"
            " النقدي في الفصول الدراسية."
        ),
        "plc_g3": "📈 النمو المهني المستمر",
        "plc_g3_desc": (
            "التطوير الذاتي والتنفيذي للكوادر التعليمية من خلال البحوث الإجرائية"
            " وتبادل الملاحظات والتغذية الراجعة."
        ),
        "plc_act": "📚 أوعية وأنشطة مجتمعات التعلم بفرع الجيزة",
        "plc_a1": "🔍 بحث الدرس (Lesson Study) وتدريب الأقران",
        "plc_a1_desc": (
            "التخطيط المشترك للدروس وتجريب التنسيقات الحديثة في مواقف تعليمية"
            " واقعية، يليها جلسات تأمل وتبادل التغذية الراجعة البناءة بين المعلمين"
            " ورؤساء الأقسام."
        ),
        "plc_a2": "🖥️ الشبكات والورش الرقمية التفاعلية",
        "plc_a2_desc": (
            "لقاءات دورية وندوات عبر الإنترنت للربط بين المعلمين والمشرفين عبر"
            " مختلف الإدارات التعليمية بالجيزة لعرض التجارب والحلول المبتكرة"
            " للتحديات الصفية."
        ),
        "support_title": "التواصل مع فريق الدعم الفني",
        "support_sub": (
            "يرجى تسجيل البيانات أدناه لتوجيه طلبك مباشرة إلى فريق الدعم المختص"
            " عبر الواتساب"
        ),
        "form_title": "📋 استمارة تقديم طلب دعم فني",
        "f_name": "👤 الاسم ثلاثي / رباعي *",
        "f_name_ph": "أدخل اسمك بالكامل كما هو بالصحيفة",
        "f_edara": "📍 الإدارة التعليمية *",
        "f_job": "💼 الوظيفة الحالية *",
        "f_phone": "📱 رقم الموبايل (واتس آب للتواصل) *",
        "f_phone_ph": "مثال: 01012345678",
        "f_prob": "📝 شرح المشكلة بالتفصيل *",
        "f_prob_ph": "اكتب تفاصيل المشكلة أو الاستفسار بدقة...",
        "f_file": "📑 إرفاق صحيفة أحوال إلكترونية حديثة (PDF أو صورة) *",
        "f_btn": "🚀 تجهيز الرسالة وتأكيد الطلب",
        "f_err": (
            "⚠️ يرجى استكمال كافة البيانات المطلوبة وإرفاق صحيفة الأحوال"
            " الإلكترونية."
        ),
        "f_succ": (
            "🎉 تم تجهيز طلبك بنجاح! اختر أحد أرقام فريق الدعم بالأسفل للإرسال"
            " المباشر:"
        ),
        "wa_prompt": "📲 اضغط على أحد الأرقام التالية للإرسال الفوري عبر الواتساب:",
        "wa_note": (
            "📌 <b>تنويه هام:</b> بعد فتح الواتساب، يرجى إعادة إرسال ملف صحيفة"
            " الأحوال الإلكترونية داخل شات المحادثة."
        ),
        "loc_title": "📍 موقع فرع الأكاديمية المهنية للمعلمين بالجيزة",
        "loc_desc": (
            "يمكنكم زيارة مقر الفرع مباشرة أو فتح الخريطة عبر تطبيق خرائط جوجل"
            " من خلال الرابط أدناه:"
        ),
        "loc_btn": "🗺️ فتح الموقع في خرائط Google Maps",
        "footer": "تصميم وتنفيذ: <span>أحمد الجنزوري</span> - مدير الفرع",
        "fb_btn": "📘 فيسبوك الفرع",
    },
    "en": {
        "page_title": "Professional Academy for Teachers - Giza Branch",
        "nav_title": "Professional Academy for Teachers - Giza Branch",
        "platform_btn": "Teacher Platform 🎓",
        "lang_btn": "🇸🇦 العربية",
        "tabs": [
            "Home",
            "About Branch",
            "Staff",
            "Educational Admin",
            "Academy Services",
            "Learning Communities",
            "Contact Support",
        ],
        "hero_title": "Professional Academy for Teachers - Giza Branch",
        "hero_sub": (
            "Digital Portal for Services, Training, and Professional"
            " Accreditation for Teachers"
        ),
        "sec_leaders": "👑 Educational Leadership Programs",
        "prog_leader_school": "School Principal & Vice Principal Program",
        "prog_leader_school_desc": (
            "One of the accredited digital programs on the Teacher Platform at"
            " the Professional Academy for Teachers available for target"
            " groups."
        ),
        "prog_leader_edu": (
            "Educational Administration Director & Deputy Program"
        ),
        "prog_leader_edu_desc": (
            "Preparing and qualifying leadership for educational administrations"
            " to develop leadership and managerial skills."
        ),
        "prog_leader_guidance": "Technical Guidance Fundamentals Program",
        "prog_leader_guidance_desc": (
            "Empowering technical supervisors with essential skills for"
            " supervision and tracking educational performance."
        ),
        "register_btn": "Register in Program",
        "sec_promotion": "📜 Placement & Promotion Programs",
        "prog_teacher_assistant": (
            "Educational Applications Program for Assistant Teacher"
        ),
        "prog_teacher_assistant_desc": (
            "Qualifying assistant teachers to complete career framework"
            " placement requirements."
        ),
        "prog_teacher_skills": "General Teaching Skills Program",
        "prog_teacher_skills_desc": (
            "Developing modern teaching skills and strategies for teachers"
            " eligible for promotion."
        ),
        "sec_job_change": "🔄 Job Title Change & Accreditation Programs",
        "prog_job_change": "Job Title Change Program",
        "prog_job_change_desc": (
            "Accredited program for educational and specialized rehabilitation to"
            " match specializations and correct career placement."
        ),
        "prog_tot": "Digital Accreditation Program (TOT)",
        "prog_tot_desc": (
            "Digital trainer training course to qualify and prepare certified"
            " trainers according to quality standards."
        ),
        "about_title": "About Professional Academy for Teachers - Giza Branch",
        "about_sub": (
            "Journey of Giving, Establishment, and Digital Transformation to"
            " Serve Teachers"
        ),
        "about_box1_title": "🏛️ Establishment & Launch (2017)",
        "about_box1_text": (
            "The Giza Branch of the Professional Academy for Teachers was"
            ' established in <b>2017</b> to be the main incubator for'
            " developing and empowering educational and pedagogical cadres in"
            " the governorate, providing accreditation and training services"
            " according to top quality standards."
        ),
        "about_box2_title": "📜 Foundation & Building Phase (2017 – 2023)",
        "about_box2_text": (
            "The period from <b>2017 to 2023</b> witnessed the establishment of"
            " regulatory and administrative rules for the branch under the"
            ' leadership of Ms. / <span class="highlight-name">Amal Abdel'
            " Maksoud</span> (Branch Director), assisted by a distinguished IT"
            " team comprising:"
        ),
        "about_box3_title": (
            "🚀 Development & Digital Transformation Phase (2023 – Present)"
        ),
        "about_box3_text": (
            "At the beginning of <b>2023</b>, a new phase launched focusing on"
            " <b>automation and digital transformation of services</b>, headed"
            ' by Mr. / <span class="highlight-name">Ahmed Hosni'
            " Al-Ganzoury</span> as Branch Director, along with a"
            " distinguished team consisting of:"
        ),
        "about_box3_footer": (
            "Efforts are currently synergizing to facilitate teachers'"
            " acquisition of digital programs for leadership, promotion, job"
            " title change, and direct technical support for all educational"
            " administrations in Giza Governorate."
        ),
        "staff_title": "Staff Administrations - Administrative Structure",
        "staff_sub": (
            "Leadership and Cadres of the Professional Academy for Teachers -"
            " Giza Branch"
        ),
        "staff1_role": "👔 Branch Director",
        "staff2_role": "🤝 Human Resources Officer",
        "staff3_role": "🎯 Professional Development Officer",
        "staff4_role": "🎯 Professional Development Officer",
        "edara_title": "Educational Administrations - Giza Governorate",
        "edara_sub": (
            "Directory of Educational Administrations and Directorate"
            " affiliated with Giza Branch"
        ),
        "services_title": "Professional Academy Services",
        "services_sub": (
            "Directory of Services and Digital Registration available for all"
            " teaching staff members"
        ),
        "serv1_title": "🌟 Career Framework Promotion Programs",
        "serv1_desc": (
            "Providing certified digital training to complete promotion"
            " requirements for eligible teachers via modern electronic systems"
            " and following up on promotion file uploads in cooperation with"
            " educational administrations."
        ),
        "serv2_title": "👑 Educational Leadership Programs",
        "serv2_desc": (
            "Qualifying pedagogical cadres for roles (school principal & vice"
            " principal, educational administration director & deputy,"
            " technical guidance fundamentals) and obtaining certified"
            " professional development certificates."
        ),
        "serv3_title": "🔄 Job Title Change",
        "serv3_desc": (
            "Receiving and auditing papers of teachers wishing to change job"
            " titles, providing certified educational and specialized"
            " rehabilitation programs for matching qualifications and proper"
            " placement."
        ),
        "serv4_title": "💼 Trainer & Center Accreditation (TOT)",
        "serv4_desc": (
            "Granting digital accreditation certificates for certified"
            " trainers (TOT), and accrediting continuous professional"
            " development programs and training institutions according to total"
            " quality standards."
        ),
        "serv_paid_title": "📝 Application for Paid Programs",
        "serv_paid_desc": (
            "The Professional Academy for Teachers - Giza Branch allows direct"
            " electronic application and registration for paid training"
            " programs related to promotion, accreditation, and skill"
            " development."
        ),
        "serv_paid_btn": (
            "🌐 Go to Program Application & Registration Platform"
        ),
        "plc_title": "Professional Learning Communities (PLCs)",
        "plc_sub": (
            "Platform for professional collaboration and experience sharing"
            " among teachers and educational leaders in Giza Branch"
        ),
        "plc_what": "🌐 What are Professional Learning Communities?",
        "plc_what_desc": (
            "An interactive educational environment bringing together teachers,"
            " supervisors, and leaders in organized collaborative teams,"
            " aiming to <b>develop teaching skills</b>, <b>share distinguished"
            " practices</b>, and <b>solve educational problems</b> to enhance"
            " student learning outcomes and transition towards a knowledge"
            " society."
        ),
        "plc_goals": "🎯 Leading Goals of Learning Communities",
        "plc_g1": "🤝 Enhancing Teamwork",
        "plc_g1_desc": (
            "Building a culture of teamwork among teachers and supervisors"
            " within the school and at the educational administration level."
        ),
        "plc_g2": "💡 Innovation & Experience Sharing",
        "plc_g2_desc": (
            "Transferring and applying modern teaching strategies, digital"
            " transformation techniques, and critical thinking in classrooms."
        ),
        "plc_g3": "📈 Continuous Professional Growth",
        "plc_g3_desc": (
            "Self and executive development for educational cadres through"
            " action research and peer observation and feedback."
        ),
        "plc_act": "📚 Vehicles & Activities of Giza Branch PLCs",
        "plc_a1": "🔍 Lesson Study & Peer Coaching",
        "plc_a1_desc": (
            "Joint lesson planning and testing modern formats in realistic"
            " educational situations, followed by reflection sessions and"
            " constructive feedback exchange among teachers and department"
            " heads."
        ),
        "plc_a2": "🖥️ Interactive Digital Networks & Workshops",
        "plc_a2_desc": (
            "Periodic meetings and online seminars connecting teachers and"
            " supervisors across various Giza educational administrations to"
            " showcase innovative experiences and solutions for classroom"
            " challenges."
        ),
        "support_title": "Contact Technical Support Team",
        "support_sub": (
            "Please register your details below to direct your request"
            " straight to the specialized support team via WhatsApp"
        ),
        "form_title": "📋 Technical Support Request Form",
        "f_name": "👤 Full Name (Triple / Quadruple) *",
        "f_name_ph": "Enter your full name as in your personnel sheet",
        "f_edara": "📍 Educational Administration *",
        "f_job": "💼 Current Job Title *",
        "f_phone": "📱 Mobile Number (WhatsApp Contact) *",
        "f_phone_ph": "Example: 01012345678",
        "f_prob": "📝 Problem Description in Detail *",
        "f_prob_ph": "Write problem details or inquiry precisely...",
        "f_file": "📑 Attach Recent Electronic Personnel Sheet (PDF or Image) *",
        "f_btn": "🚀 Prepare Message & Confirm Request",
        "f_err": (
            "⚠️ Please complete all required data and attach the electronic"
            " personnel sheet."
        ),
        "f_succ": (
            "🎉 Your request has been prepared successfully! Choose one of"
            " the support team numbers below for direct sending:"
        ),
        "wa_prompt": (
            "📲 Click on one of the following numbers for instant sending via"
            " WhatsApp:"
        ),
        "wa_note": (
            "📌 <b>Important Note:</b> After opening WhatsApp, please resend"
            " your electronic personnel sheet file inside the chat."
        ),
        "loc_title": (
            "📍 Location of Professional Academy for Teachers - Giza Branch"
        ),
        "loc_desc": (
            "You can visit the branch headquarters directly or open the map via"
            " Google Maps using the link below:"
        ),
        "loc_btn": "🗺️ Open Location in Google Maps",
        "footer": "Designed & Implemented by: <span>Ahmed Al-Ganzoury</span> - Branch Director",
        "fb_btn": "📘 Branch Facebook",
    },
}

t = TEXTS[lang]
edarat_list = EDARAT_LIST_AR if is_ar else EDARAT_LIST_EN
jobs_list = JOBS_LIST_AR if is_ar else JOBS_LIST_EN

# 4️⃣ تصميم الموقع الإلكتروني المطور
st.markdown(
    f"""
    <style>
    footer {{ visibility: hidden !important; display: none !important; }}
    header[data-testid="stHeader"] {{ display: none !important; }}
    [data-testid="stToolbarActions"] {{ display: none !important; }}
    [data-testid="stActionButtonIcon"] {{ display: none !important; }}
    [data-testid="stSidebar"] {{ display: none !important; }}

    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }}

    html, body, [data-testid="stAppViewContainer"] {{
        direction: {'rtl' if is_ar else 'ltr'};
        text-align: {'right' if is_ar else 'left'};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #060d1f !important;
        color: #ffffff !important;
    }}

    .info-card-box {{
        direction: {'rtl' if is_ar else 'ltr'};
        text-align: {'right' if is_ar else 'left'};
        background: linear-gradient(145deg, rgba(15, 32, 67, 0.95) 0%, rgba(8, 18, 41, 0.9) 100%) !important;
        backdrop-filter: blur(12px);
        color: #ffffff !important;
        padding: 30px 28px;
        border-radius: 22px;
        border: 1.5px solid rgba(201, 162, 39, 0.45);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 26px;
        transition: all 0.3s ease;
    }

    .info-card-box:hover {{
        border-color: #FFD700;
        box-shadow: 0 14px 35px rgba(201, 162, 39, 0.3);
    }

    .info-card-box h3 {{
        color: #FFD700 !important;
        font-size: 1.55rem !important;
        font-weight: 800 !important;
        margin-top: 0;
        padding-bottom: 14px;
        border-bottom: 1.5px dashed rgba(201, 162, 39, 0.5);
    }

    .info-card-box p {{
        font-size: 1.18rem !important;
        line-height: 2 !important;
        color: #f1f5f9 !important;
        font-weight: 500 !important;
        margin-bottom: 15px;
    }

    .staff-item-badge {{
        background: rgba(11, 26, 62, 0.8) !important;
        border: 1px solid rgba(201, 162, 39, 0.4) !important;
        border-right: {'5px solid #FFD700' if is_ar else 'none'} !important;
        border-left: {'none' if is_ar else '5px solid #FFD700'} !important;
        border-radius: 12px !important;
        padding: 12px 18px !important;
        margin-bottom: 10px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #ffffff !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.25s ease !important;
    }

    .staff-item-badge:hover {{
        transform: translateY(-2px) !important;
        background: rgba(201, 162, 39, 0.15) !important;
        border-color: #FFD700 !important;
    }

    .highlight-name {{
        color: #FFD700 !important;
        font-weight: 800 !important;
    }}

    label[data-testid="stWidgetLabel"], .stWidgetLabel, label p {{
        color: #ffffff !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
    }}

    div[data-baseweb="input"] input, textarea {{
        color: #ffffff !important;
        font-size: 1rem !important;
        background-color: #0f2043 !important;
    }}

    ::placeholder, ::-webkit-input-placeholder {{
        color: #94a3b8 !important;
        opacity: 1 !important;
    }}

    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {{
        background-color: #0f2043 !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(201, 162, 39, 0.45) !important;
    }

    div[data-baseweb="input"] > div:focus-within, textarea:focus {{
        border-color: #FFD700 !important;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.35) !important;
    }}

    div[data-testid="stFormSubmitButton"] > button {{
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

    div[data-testid="stFormSubmitButton"] > button:hover {{
        background: linear-gradient(135deg, #FFD700 0%, #C9A227 100%) !important;
        color: #000000 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.6) !important;
    }}

    div[data-testid="stFileUploader"] {{
        background-color: #0f2043 !important;
        border-radius: 14px !important;
        border: 1.5px dashed #C9A227 !important;
        padding: 12px !important;
    }}

    div[data-testid="stFileUploaderDropzone"] {{
        background-color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #C9A227 !important;
    }}

    div[data-testid="stFileUploaderDropzone"] span, 
    div[data-testid="stFileUploaderDropzone"] div,
    div[data-testid="stFileUploaderDropzoneInstructions"] {{
        color: #0b1a3e !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
    }}

    div[data-testid="stFileUploaderDropzone"] button {{
        background: linear-gradient(135deg, #0b1a3e 0%, #172a4d 100%) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: 1px solid #C9A227 !important;
        border-radius: 8px !important;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stFileUploaderDropzone"] button:hover {{
        background: #C9A227 !important;
        color: #0b1a3e !important;
    }}

    .top-navbar {{
        background: linear-gradient(180deg, rgba(11, 26, 62, 0.98) 0%, rgba(6, 13, 31, 0.95) 100%) !important;
        backdrop-filter: blur(12px);
        padding: 14px 30px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        direction: {'rtl' if is_ar else 'ltr'};
        box-shadow: 0 4px 25px rgba(0,0,0,0.5);
        margin: 0 -1rem 20px -1rem;
        border-bottom: 2px solid rgba(201, 162, 39, 0.5);
        flex-wrap: wrap;
        gap: 15px;
    }

    .nav-right-container {{ 
        display: flex; 
        align-items: center; 
        gap: 15px; 
    }}

    .nav-left-container {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .nav-logo-text {{
        color: #ffffff !important;
        font-weight: 800;
        font-size: 1.25rem;
        display: flex;
        align-items: center;
        gap: 15px;
        letter-spacing: 0.5px;
    }

    .navbar-logo-img {{
        height: 48px;
        width: auto;
        border-radius: 8px;
        object-fit: contain;
        background: rgba(255, 255, 255, 0.08);
        padding: 4px;
        border: 1px solid rgba(201, 162, 39, 0.5);
    }

    .teacher-platform-btn {{
        background: linear-gradient(135deg, #d32f2f 0%, #9a0007 100%) !important;
        color: #ffffff !important;
        padding: 10px 22px;
        border-radius: 30px;
        font-weight: bold;
        font-size: 0.95rem;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4);
        border: 1.5px solid #FFD700;
        display: inline-block;
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .teacher-platform-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(211, 47, 47, 0.7);
    }}

    .lang-toggle-btn {{
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%) !important;
        color: #FFD700 !important;
        padding: 10px 18px;
        border-radius: 30px;
        font-weight: bold;
        font-size: 0.95rem;
        border: 1.5px solid #C9A227;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(201, 162, 39, 0.3);
        transition: all 0.3s ease;
    }}

    .lang-toggle-btn:hover {{
        background: linear-gradient(135deg, #C9A227 0%, #937B2B 100%) !important;
        color: #0b1a3e !important;
        transform: translateY(-2px);
    }}

    .stButton>button {{
        background: rgba(15, 32, 67, 0.8) !important;
        color: #cbd5e1 !important;
        font-weight: 700 !important;
        font-size: 0.98rem !important;
        border-radius: 12px !important;
        border: 1px solid rgba(201, 162, 39, 0.3) !important;
        padding: 10px 18px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100%;
    }

    .stButton>button:hover {{
        background: linear-gradient(135deg, #C9A227 0%, #937B2B 100%) !important;
        color: #0b1a3e !important;
        border-color: #ffffff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(201, 162, 39, 0.4) !important;
    }

    .facebook-btn-tab {{
        background: linear-gradient(135deg, #1877F2 0%, #0a52b2 100%) !important;
        color: white !important;
        padding: 10px 16px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 0.95rem;
        text-decoration: none;
        display: block;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 12px rgba(24, 119, 242, 0.35);
        transition: all 0.3s ease;
    }

    .facebook-btn-tab:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(24, 119, 242, 0.55);
    }}

    .hero-banner {{
        background: linear-gradient(135deg, rgba(11, 26, 62, 0.9) 0%, rgba(15, 32, 67, 0.7) 100%), 
                    radial-gradient(circle at top right, rgba(201, 162, 39, 0.15), transparent);
        border-radius: 24px;
        padding: 40px 20px;
        text-align: center !important;
        margin: 15px 0 35px 0;
        border: 1.5px solid rgba(201, 162, 39, 0.4);
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
    }

    .center-main-logo {{
        height: 160px;
        width: auto;
        object-fit: contain;
        margin-bottom: 20px;
        display: inline-block;
        filter: drop-shadow(0px 10px 20px rgba(0,0,0,0.5));
    }

    .main-header-title {{
        color: #ffffff !important;
        font-size: 2.4rem;
        font-weight: 900;
        display: inline-block;
        padding-bottom: 12px;
        border-bottom: 4px solid #C9A227;
        text-align: center !important;
        text-shadow: 0 3px 6px rgba(0,0,0,0.4);
    }

    .sub-header-title {{
        color: #94a3b8 !important;
        font-size: 1.2rem;
        margin-top: 15px;
        font-weight: 500;
        text-align: center !important;
    }

    .section-title {{
        text-align: center !important;
        color: #C9A227 !important;
        font-size: 1.75rem;
        font-weight: 800;
        margin-top: 40px;
        margin-bottom: 30px;
        padding-bottom: 10px;
        border-bottom: 2px dashed rgba(201, 162, 39, 0.4);
    }

    .program-card-wrapper {{
        background: rgba(15, 32, 67, 0.6) !important;
        backdrop-filter: blur(8px);
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        transition: all 0.35s ease;
    }

    .program-card-wrapper:hover {{
        transform: translateY(-6px);
        border-color: #C9A227;
        box-shadow: 0 14px 32px rgba(201, 162, 39, 0.3);
    }

    .program-img-box {{
        width: 100%;
        height: 190px;
        overflow: hidden;
        background-color: #0b1a3e;
    }

    .program-img-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }

    .program-card-wrapper:hover .program-img-box img {{
        transform: scale(1.08);
    }

    .program-content-box {{
        padding: 22px 18px;
        text-align: center !important;
    }

    .program-card-title {{
        color: #C9A227 !important;
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .program-card-desc {{
        color: #cbd5e1 !important;
        font-size: 0.96rem;
        line-height: 1.65;
    }

    .card-footer-badge {{
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

    .staff-card {{
        background: linear-gradient(145deg, rgba(15, 32, 67, 0.8) 0%, rgba(6, 13, 31, 0.9) 100%) !important;
        border: 1.5px solid rgba(201, 162, 39, 0.35);
        border-radius: 24px;
        padding: 30px 20px;
        text-align: center !important;
        box-shadow: 0 10px 26px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        transition: all 0.35s ease;
    }

    .staff-card:hover {{
        transform: translateY(-5px);
        border-color: #C9A227;
        box-shadow: 0 14px 32px rgba(201, 162, 39, 0.25);
    }

    .avatar-frame {{
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

    .avatar-frame img {{ width: 100%; height: 100%; object-fit: cover !important; }}
    .staff-name {{ color: #C9A227 !important; font-size: 1.28rem; font-weight: 800; margin-bottom: 8px; }}
    .staff-role {{ color: #e2e8f0 !important; font-size: 1rem; font-weight: 600; margin-bottom: 10px; }}
    .staff-dept {{
        color: #FFD700 !important;
        font-size: 0.88rem;
        font-weight: bold;
        background: rgba(201, 162, 39, 0.18);
        padding: 6px 14px;
        border-radius: 20px;
        display: inline-block;
        border: 1px solid rgba(201, 162, 39, 0.4);
    }

    .edara-card {{
        background: rgba(15, 32, 67, 0.7) !important;
        border: 1px solid rgba(201, 162, 39, 0.25);
        border-right: {'5px solid #C9A227' if is_ar else '1px solid rgba(201, 162, 39, 0.25)'} !important;
        border-left: {'1px solid rgba(201, 162, 39, 0.25)' if is_ar else '5px solid #C9A227'} !important;
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

    .edara-card:hover {{
        transform: scale(1.03);
        border-color: #C9A227;
        background: rgba(201, 162, 39, 0.2) !important;
    }

    .support-form-container {{
        background: rgba(15, 32, 67, 0.85) !important;
        backdrop-filter: blur(12px);
        padding: 32px 28px;
        border-radius: 24px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
        border-top: 5px solid #C9A227;
        border-right: {'1px solid rgba(201, 162, 39, 0.3)' if is_ar else '5px solid #C9A227'};
        border-left: {'5px solid #C9A227' if is_ar else '1px solid rgba(201, 162, 39, 0.3)'};
        max-width: 900px;
        margin: 0 auto;
    }

    .support-form-title {{
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 24px;
        padding-bottom: 12px;
        border-bottom: 2px dashed rgba(201, 162, 39, 0.4);
    }

    .location-card-container {{
        background: rgba(15, 32, 67, 0.8) !important;
        border: 1.5px solid #C9A227;
        border-radius: 24px;
        padding: 28px 20px;
        max-width: 900px;
        margin: 35px auto 0 auto;
        text-align: center !important;
        box-shadow: 0 12px 35px rgba(0,0,0,0.3);
    }

    .location-btn {{
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

    .location-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(201, 162, 39, 0.4);
    }

    .map-frame {{
        width: 100%;
        height: 340px;
        border-radius: 16px;
        border: 2px solid #C9A227;
    }

    .whatsapp-card {{
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

    .whatsapp-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.55);
    }

    .app-footer {{
        margin-top: 50px;
        padding: 22px 0;
        background: linear-gradient(180deg, #0b1a3e 0%, #040915 100%) !important;
        color: #ffffff !important;
        text-align: center !important;
        font-size: 1.05rem;
        font-weight: bold;
        border-top: 3.5px solid #C9A227;
        border-radius: 20px 20px 0 0;
        box-shadow: 0 -6px 20px rgba(0,0,0,0.3);
    }
    
    .app-footer span {{ color: #FFD700; }}

    @media (max-width: 768px) {{
        .top-navbar {{
            flex-direction: column;
            text-align: center;
            justify-content: center;
            padding: 15px 12px;
        }}
        .nav-logo-text {{
            font-size: 1.05rem;
            flex-direction: column;
            gap: 8px;
        }}
        .main-header-title {{
            font-size: 1.7rem;
        }}
        .sub-header-title {{
            font-size: 1rem;
        }}
        .section-title {{
            font-size: 1.4rem;
        }}
        .center-main-logo {{
            height: 130px;
        }}
        .map-frame {{
            height: 270px;
        }}
        .support-form-container {{
            padding: 20px 14px;
        }}
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 5️⃣ إدارة حالة التبويبات
if "current_tab" not in st.session_state:
  st.session_state["current_tab"] = t["tabs"][0]

# الشريط العلوي للهيدر مع زر تبديل اللغة
col_logo, col_actions = st.columns([2.5, 1.5])
with col_logo:
  st.markdown(
      f"""
        <div class="nav-right-container">
            <div class="nav-logo-text">
                {logo_navbar_tag}
                <span>{t["nav_title"]}</span>
            </div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_actions:
  c_btn1, c_btn2 = st.columns([1, 1])
  with c_btn1:
    if st.button(
        "🇺🇸 English" if is_ar else "🇸🇦 العربية",
        key="lang_toggle",
        use_container_width=True,
    ):
      st.session_state["language"] = "en" if is_ar else "ar"
      st.session_state["current_tab"] = (
          TEXTS["en"]["tabs"][0] if is_ar else TEXTS["ar"]["tabs"][0]
      )
      st.rerun()
  with c_btn2:
    st.markdown(
        f"""
            <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="teacher-platform-btn" style="width:100%; display:block; text-align:center;">
                {t["platform_btn"]}
            </a>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    "<hr style='margin-top: 12px; margin-bottom: 25px; border-color:"
    " rgba(201, 162, 39, 0.2);'>",
    unsafe_allow_html=True,
)

# قائمة التبويبات العلوية
cols_tabs = st.columns([1.1, 1, 1.1, 1.2, 1.2, 1.1, 1.4, 1.3])
tabs_names = t["tabs"]

for idx, name in enumerate(tabs_names):
  with cols_tabs[idx]:
    if st.button(name, key=f"tab_btn_{idx}", use_container_width=True):
      st.session_state["current_tab"] = name

with cols_tabs[7]:
  st.markdown(
      f"""
        <a href="{FACEBOOK_PAGE_URL}" target="_blank" class="facebook-btn-tab">
            {t["fb_btn"]}
        </a>
    """,
      unsafe_allow_html=True,
  )

st.markdown(
    "<hr style='margin-top: 8px; margin-bottom: 25px; border-color:"
    " rgba(201, 162, 39, 0.2);'>",
    unsafe_allow_html=True,
)

current_tab = st.session_state["current_tab"]

# تحميل صور البرامج
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
if current_tab == tabs_names[0]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["hero_title"]}</div>
            <div class="sub-header-title">{t["hero_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f'<div class="section-title">{t["sec_leaders"]}</div>',
      unsafe_allow_html=True,
  )
  c1, c2, c3 = st.columns([1, 1, 1])

  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_school}" alt="School Principal"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_leader_school"]}</div>
                    <div class="program-card-desc">{t["prog_leader_school_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_leader_school"]}</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_edu}" alt="Edu Admin"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_leader_edu"]}</div>
                    <div class="program-card-desc">{t["prog_leader_edu_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_leader_edu"]}</div>',
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_leader_guidance}" alt="Guidance"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_leader_guidance"]}</div>
                    <div class="program-card-desc">{t["prog_leader_guidance_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_leader_guidance"]}</div>',
        unsafe_allow_html=True,
    )

  st.markdown(
      f'<div class="section-title">{t["sec_promotion"]}</div>',
      unsafe_allow_html=True,
  )
  c1, c2 = st.columns([1, 1])
  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teacher_assistant}" alt="Teacher Assistant"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_teacher_assistant"]}</div>
                    <div class="program-card-desc">{t["prog_teacher_assistant_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_teacher_assistant"]}</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_teacher_skills}" alt="Teacher Skills"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_teacher_skills"]}</div>
                    <div class="program-card-desc">{t["prog_teacher_skills_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_teacher_skills"]}</div>',
        unsafe_allow_html=True,
    )

  st.markdown(
      f'<div class="section-title">{t["sec_job_change"]}</div>',
      unsafe_allow_html=True,
  )
  c1, c2 = st.columns([1, 1])
  with c1:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_job}" alt="Job Change"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_job_change"]}</div>
                    <div class="program-card-desc">{t["prog_job_change_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_job_change"]}</div>',
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
            <div class="program-card-wrapper">
                <div class="program-img-box"><img src="{img_tot}" alt="TOT"></div>
                <div class="program-content-box">
                    <div class="program-card-title">{t["prog_tot"]}</div>
                    <div class="program-card-desc">{t["prog_tot_desc"]}</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<a href="https://www.pat.edu.eg/platform-programs"'
        ' target="_blank"><button style="width:100%; border-radius:10px;'
        " background: linear-gradient(135deg, #b22222 0%, #8b0000 100%);"
        f' color:white; font-weight:bold; border:none; padding:11px;'
        f' cursor:pointer; box-shadow: 0 4px 12px'
        f' rgba(178,34,34,0.4);">{t["register_btn"]}</button></a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card-footer-badge">{t["prog_tot"]}</div>',
        unsafe_allow_html=True,
    )

# 2️⃣ عن الفرع
elif current_tab == tabs_names[1]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["about_title"]}</div>
            <div class="sub-header-title">{t["about_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="info-card-box">
            <h3>{t["about_box1_title"]}</h3>
            <p>{t["about_box1_text"]}</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="info-card-box">
            <h3>{t["about_box2_title"]}</h3>
            <p>{t["about_box2_text"]}</p>
            <div class="staff-item-badge">💻 <span class="highlight-name">أ . أحمد حسني الجنزوري</span> (عضو تكنولوجيا المعلومات IT)</div>
            <div class="staff-item-badge">💻 <span class="highlight-name">أ . خالد عبد الحكيم هارون</span> (عضو تكنولوجيا المعلومات IT)</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="info-card-box">
            <h3>{t["about_box3_title"]}</h3>
            <p>{t["about_box3_text"]}</p>
            <div class="staff-item-badge">🤝 <span class="highlight-name">أ . خالد عبد الحكيم هارون</span> (مسئول الموارد البشرية وتكنولوجيا المعلومات IT)</div>
            <div class="staff-item-badge">🎯 <span class="highlight-name">أ . أحمد محمد عمر</span> (مسئول التنمية المهنية والاعتماد)</div>
            <div class="staff-item-badge">🎯 <span class="highlight-name">أ . أمينة فوزي عبد الرحمن</span> (مسئول التنمية المهنية والاعتماد)</div>
            <p style="margin-top: 18px;">{t["about_box3_footer"]}</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 3️⃣ إدارات الأفراد
elif current_tab == tabs_names[2]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["staff_title"]}</div>
            <div class="sub-header-title">{t["staff_sub"]}</div>
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
                <div class="avatar-frame"><img src="{img_ahmed}" alt="Ahmed"></div>
                <div class="staff-name"><span class="highlight-name">أحمد حسني الجنزوري</span></div>
                <div class="staff-role" style="margin-top:10px;">{t["staff1_role"]}</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c2:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{img_khaled}" alt="Khaled"></div>
                <div class="staff-name"><span class="highlight-name">خالد عبدالحكيم هارون</span></div>
                <div class="staff-role" style="margin-top:10px;">{t["staff2_role"]}</div>
                <div class="staff-dept">Information Technology</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c3:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{img_omar}" alt="Omar"></div>
                <div class="staff-name"><span class="highlight-name">أحمد محمد عمر</span></div>
                <div class="staff-role" style="margin-top:10px;">{t["staff3_role"]}</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with c4:
    st.markdown(
        f"""
            <div class="staff-card">
                <div class="avatar-frame"><img src="{img_amina}" alt="Amina"></div>
                <div class="staff-name"><span class="highlight-name">أمينة فوزي عبدالرحمن</span></div>
                <div class="staff-role" style="margin-top:10px;">{t["staff4_role"]}</div>
                <div class="staff-dept">التنمية المهنية والاعتماد</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

# 4️⃣ الإدارات التعليمية
elif current_tab == tabs_names[3]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["edara_title"]}</div>
            <div class="sub-header-title">{t["edara_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  col_e1, col_e2, col_e3, col_e4 = st.columns([1, 1, 1, 1])
  for index, edara in enumerate(edarat_list):
    col_target = [col_e1, col_e2, col_e3, col_e4][index % 4]
    with col_target:
      prefix = "📍" if is_ar else "📍"
      st.markdown(
          f'<div class="edara-card">{prefix} {edara}</div>',
          unsafe_allow_html=True,
      )

# 5️⃣ خدمات الأكاديمية
elif current_tab == tabs_names[4]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["services_title"]}</div>
            <div class="sub-header-title">{t["services_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  s1, s2 = st.columns([1, 1])
  with s1:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h3>{t["serv1_title"]}</h3>
                <p>{t["serv1_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with s2:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h3>{t["serv2_title"]}</h3>
                <p>{t["serv2_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  s3, s4 = st.columns([1, 1])
  with s3:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h3>{t["serv3_title"]}</h3>
                <p>{t["serv3_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with s4:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h3>{t["serv4_title"]}</h3>
                <p>{t["serv4_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(
      f"""
        <div class="support-form-container" style="text-align: center; margin-top:30px;">
            <p style="font-size: 1.15rem; line-height: 1.9; color: #ffffff;">{t["serv_paid_desc"]}</p>
            <br>
            <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="location-btn" style="text-decoration: none;">
                {t["serv_paid_btn"]}
            </a>
        </div>
    """,
      unsafe_allow_html=True,
  )

# 6️⃣ مجتمعات التعلم
elif current_tab == tabs_names[5]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["plc_title"]}</div>
            <div class="sub-header-title">{t["plc_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f"""
        <div class="info-card-box">
            <h3>{t["plc_what"]}</h3>
            <p>{t["plc_what_desc"]}</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      f'<div class="section-title">{t["plc_goals"]}</div>',
      unsafe_allow_html=True,
  )
  p1, p2, p3 = st.columns([1, 1, 1])
  with p1:
    st.markdown(
        f"""
            <div class="info-card-box" style="height: 100%;">
                <h4 style="color: #FFD700; margin-top:0;">{t["plc_g1"]}</h4>
                <p style="font-size: 1rem;">{t["plc_g1_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with p2:
    st.markdown(
        f"""
            <div class="info-card-box" style="height: 100%;">
                <h4 style="color: #FFD700; margin-top:0;">{t["plc_g2"]}</h4>
                <p style="font-size: 1rem;">{t["plc_g2_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with p3:
    st.markdown(
        f"""
            <div class="info-card-box" style="height: 100%;">
                <h4 style="color: #FFD700; margin-top:0;">{t["plc_g3"]}</h4>
                <p style="font-size: 1rem;">{t["plc_g3_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(
      f'<div class="section-title">{t["plc_act"]}</div>',
      unsafe_allow_html=True,
  )
  a1, a2 = st.columns([1, 1])
  with a1:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0;">{t["plc_a1"]}</h4>
                <p>{t["plc_a1_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
  with a2:
    st.markdown(
        f"""
            <div class="info-card-box">
                <h4 style="color: #FFD700; margin-top:0;">{t["plc_a2"]}</h4>
                <p>{t["plc_a2_desc"]}</p>
            </div>
        """,
        unsafe_allow_html=True,
    )

# 7️⃣ التواصل مع الدعم
elif current_tab == tabs_names[6]:
  st.markdown(
      f"""
        <div class="hero-banner">
            <div>{logo_header_tag}</div>
            <div class="main-header-title">{t["support_title"]}</div>
            <div class="sub-header-title">{t["support_sub"]}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

  with st.container():
    st.markdown(
        f"""
            <div class="support-form-container">
                <div class="support-form-title">{t["form_title"]}</div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("support_form", clear_on_submit=False):
      name = st.text_input(t["f_name"], placeholder=t["f_name_ph"])
      col_f1, col_f2 = st.columns([1, 1])
      with col_f1:
        edara = st.selectbox(t["f_edara"], edarat_list)
      with col_f2:
        job = st.selectbox(t["f_job"], jobs_list)

      phone = st.text_input(t["f_phone"], placeholder=t["f_phone_ph"])
      problem = st.text_area(t["f_prob"], placeholder=t["f_prob_ph"], height=120)
      file_uploaded = st.file_uploader(t["f_file"], type=["pdf", "png", "jpg", "jpeg"])

      st.markdown("<br>", unsafe_allow_html=True)
      submitted = st.form_submit_button(t["f_btn"], use_container_width=True)

      if submitted:
        if not name or not phone or not problem or file_uploaded is None:
          st.error(t["f_err"])
        else:
          st.session_state["form_data"] = {
              "name": name,
              "edara": edara,
              "job": job,
              "phone": phone,
              "problem": problem,
              "file_name": file_uploaded.name,
          }
          st.success(t["f_succ"])

    if "form_data" in st.session_state and st.session_state["form_data"]:
      data = st.session_state["form_data"]
      msg_text = f"""*Support Request - Giza Branch Platform*
📌 *Name:* {data['name']}
📍 *Admin:* {data['edara']}
💼 *Job:* {data['job']}
📱 *Phone:* {data['phone']}
📑 *Personnel Sheet:* Attached ({data['file_name']})

📝 *Details:*
{data['problem']}"""

      encoded_msg = urllib.parse.quote(msg_text)
      st.markdown(
          f"<br><h4 style='text-align: center; color: #ffffff;'>{t['wa_prompt']}</h4>",
          unsafe_allow_html=True,
      )

      whatsapp_numbers = [
          ("Support (1)", "201069996245"),
          ("Support (2)", "201120807631"),
          ("Support (3)", "201201109892"),
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

      st.info(t["wa_note"])

    st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      f"""
        <div class="location-card-container">
            <h3 style="color: #C9A227; margin-top: 0; font-size: 1.45rem; margin-bottom: 14px;">{t["loc_title"]}</h3>
            <p style="color: #cbd5e1; font-size: 1.02rem; margin-bottom: 20px;">{t["loc_desc"]}</p>
            <a href="{LOCATION_MAP_URL}" target="_blank" class="location-btn">
                {t["loc_btn"]}
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

# Footer
st.markdown(
    f"""
    <div class="app-footer">
        {t["footer"]}
    </div>
""",
    unsafe_allow_html=True,
)
