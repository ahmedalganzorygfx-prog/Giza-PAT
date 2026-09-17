import streamlit as st
import os

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="منصة الفرع التعليمية",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق تنسيقات CSS المتقدمة وتوسيط العناوين وتحسين RTL
st.markdown("""
    <style>
    /* محاذاة الصفحة العامة والخطوط */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f8f9fa;
    }

    /* محاذاة الشريط الجانبي Sidebar */
    [data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
        background-color: #ffffff;
        border-left: 1px solid #e0e0e0;
    }
    
    [data-testid="stSidebar"] * {
        text-align: right !important;
    }

    /* 🌟 تنسيق وتوسيط العناوين الرئيسية 🌟 */
    .centered-title-container {
        text-align: center;
        margin: 20px 0 35px 0;
    }

    .main-title {
        color: #937B2B;
        font-size: 2.5rem;
        font-weight: 800;
        display: inline-block;
        padding-bottom: 10px;
        border-bottom: 4px solid #937B2B;
        border-radius: 2px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
    }

    .sub-title {
        color: #555555;
        font-size: 1.2rem;
        margin-top: 10px;
    }

    /* 🌟 عنوان القسم الذهبي المؤطر في منتصف الصفحة 🌟 */
    .section-header-centered {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 30px 0 25px 0;
    }

    .section-title-badge {
        background: linear-gradient(135deg, #937B2B 0%, #b89c3f 100%);
        color: white;
        padding: 12px 40px;
        font-size: 1.4rem;
        font-weight: bold;
        border-radius: 25px 0px 25px 0px;
        box-shadow: 0 4px 10px rgba(147, 123, 43, 0.3);
        text-align: center;
    }

    /* 🌟 تصميم شعار الصفحة الرئيسية 🌟 */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }

    /* 🌟 تصميم بطاقات البرامج 🌟 */
    .program-card {
        background-color: #1b2631;
        border: 2px solid #937B2B;
        border-radius: 30px 0px 30px 0px;
        padding: 25px 20px;
        color: white;
        text-align: right;
        direction: rtl;
        min-height: 240px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }

    .program-card:hover {
        transform: translateY(-5px);
    }

    .program-title {
        color: #FFD700;
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 12px;
        text-align: right;
    }

    .program-desc {
        font-size: 0.95rem;
        line-height: 1.7;
        color: #e0e0e0;
        text-align: right;
    }

    /* عنوان البطاقة السفلي */
    .card-footer {
        background-color: #ffffff;
        color: #937B2B;
        text-align: center;
        padding: 8px 15px;
        font-weight: bold;
        border: 1.5px solid #937B2B;
        border-radius: 0 0 12px 12px;
        margin-top: 8px;
        font-size: 0.95rem;
    }

    /* تخصيص أزرار Streamlit لتشبه تصميم المنصة */
    .stButton>button {
        background-color: #b22222 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 8px 20px !important;
        transition: background-color 0.3s !important;
    }

    .stButton>button:hover {
        background-color: #8b0000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- القائمة الجانبية (الشريط العلوي للتنقل) ----------------
st.sidebar.markdown("### 📌 التبويبات الرئيسية")
main_tab = st.sidebar.radio(
    "انتقل إلى:",
    ["الرئيسية", "عن الفرع", "الادارات التعليمية", "منصة الفرع"]
)

# ---------------- المحتوى الرئيسي حسب التبويب ----------------

# 1️⃣ الصفحة الرئيسية
if main_tab == "الرئيسية":
    st.markdown("""
        <div class="centered-title-container">
            <div class="main-title">منصة الفرع التعليمية الرقمية</div>
            <div class="sub-title">أهلاً بكم في البوابة الرقمية المعتمدة للبرامج والتدريبات التربوية</div>
        </div>
    """, unsafe_allow_html=True)

    # عرض اللوجو في منتصف الصفحة الرئيسية
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        image_path = "image_526f40.jpg"
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True, caption="شعار الأكاديمية المهنية للمعلمين - منصة الفرع")
        else:
            # لوحة تعويضية في حال عدم وجود ملف الصورة
            st.markdown("""
                <div style="background-color:#937B2B; color:white; padding:40px; text-align:center; border-radius:20px; font-size:1.5rem; font-weight:bold;">
                    🎓 شعار منصة الفرع التعليمية
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 تقدم المنصة مجموعة متكاملة من البرامج التدريبية المعتمدة للقيادات التربوية، المعلمين المساعدين، والراغبين في الترقي وتغيير المسمى الوظيفي.")

# 2️⃣ عن الفرع
elif main_tab == "عن الفرع":
    st.markdown("""
        <div class="centered-title-container">
            <div class="main-title">عن الفرع</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background-color:white; padding:30px; border-radius:15px; border-right:5px solid #937B2B; box-shadow:0 2px 8px rgba(0,0,0,0.05); font-size:1.1rem; line-height:1.8;">
            يسعى فرع الأكاديمية إلى تقديم أحدث البرامج التدريبية الرقمية المعتمدة للارتقاء بمستوى الأداء التربوي والإداري لأعضاء هيئة التعليم. 
            كما يهدف إلى تمكين المعلمين والقيادات التعليمية من مواكبة المعايير الحديثة في الجودة والاعتماد والتوجيه الفني.
        </div>
    """, unsafe_allow_html=True)

# 3️⃣ الإدارات التعليمية
elif main_tab == "الادارات التعليمية":
    st.markdown("""
        <div class="centered-title-container">
            <div class="main-title">الإدارات التعليمية</div>
            <div class="sub-title">دليل وخريطة الإدارات التعليمية التابعة لفرع الأكاديمية</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color:white; padding:25px; border-radius:15px; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
            <p style="font-size:1.1rem;">يمكنك التواصل مع الإدارات التعليمية التابعة للفرع لمتابعة خطط التدريب والاعتماد:</p>
            <ul>
                <li><strong>إدارة التوجيه والإشراف الفني</strong></li>
                <li><strong>إدارة التدريب وتنمية المهارات</strong></li>
                <li><strong>إدارة القيادات التربوية والاعتماد</strong></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# 4️⃣ منصة الفرع
elif main_tab == "منصة الفرع":
    st.markdown("""
        <div class="centered-title-container">
            <div class="main-title">منصة الفرع الرقمية</div>
            <div class="sub-title">استعراض البرامج التدريبية المتاحة للتسجيل</div>
        </div>
    """, unsafe_allow_html=True)

    # اختيارات البرامج
    sub_category = st.selectbox(
        "اختر الفئة التدريبية المطلوبة:",
        [
            "برامج القيادات التربوية",
            "برامج التسكين والترقي",
            "برنامج تغيير المسمى الوظيفي",
            "برامج الاعتماد"
        ]
    )

    # 🔹 1. برامج القيادات التربوية
    if sub_category == "برامج القيادات التربوية":
        st.markdown('''
            <div class="section-header-centered">
                <div class="section-title-badge">برامج القيادات التربوية</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة مدرسية</div>
                    <div class="program-desc">أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية للمعلمين المتاحة للفئات المستهدفة من أعضاء هيئة التعليم في مصر.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn1", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج مدير ووكيل إدارة مدرسية")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-desc">برنامج مخصص لتأهيل وإعداد القيادات للإدارات التعليمية وتطوير المهارات القيادية والأداء الإداري.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn2", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج مدير ووكيل إدارة تعليمية")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

        with col3:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-desc">يهدف إلى تمكين الموجهين من المهارات الأساسية للإشراف الفني ومتابعة جودة العملية التعليمية.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn3", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج أساسيات التوجيه الفني")
            st.markdown('<div class="card-footer">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    # 🔹 2. برامج التسكين والترقي
    elif sub_category == "برامج التسكين والترقي":
        st.markdown('''
            <div class="section-header-centered">
                <div class="section-title-badge">برامج التسكين والترقي</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-desc">برنامج التأهيل التربوي المخصص للمعلمين المساعدين لاستكمال متطلبات التسكين على الكادر الوظيفي.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn4", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج التطبيقات التربوية")
            st.markdown('<div class="card-footer">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-desc">برنامج موجه لتطوير الكفايات التدريسية الحديثة واستراتيجيات التعلم لدى المعلمين المستحقين للترقية.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn5", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج مهارات التدريس")
            st.markdown('<div class="card-footer">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    # 🔹 3. برنامج تغيير المسمى الوظيفي
    elif sub_category == "برنامج تغيير المسمى الوظيفي":
        st.markdown('''
            <div class="section-header-centered">
                <div class="section-title-badge">برنامج تغيير المسمى الوظيفي</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج تغيير المسمى الوظيفي</div>
                    <div class="program-desc">برنامج معتمد يهدف لإعادة التأهيل التربوي والتخصصي للمعلمين الراغبين في إعادة التسكين وتغيير المسمى الوظيفي.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn6", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج تغيير المسمى الوظيفي")
            st.markdown('<div class="card-footer">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    # 🔹 4. برامج الاعتماد
    elif sub_category == "برامج الاعتماد":
        st.markdown('''
            <div class="section-header-centered">
                <div class="section-title-badge">برامج الاعتماد</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">البرنامج الرقمي للاعتماد (TOT)</div>
                    <div class="program-desc">البرنامج التدريبي لإعداد وتأهيل المدربين المعتمدين رقمياً وفق معايير الجودة بالأكاديمية المهنية للمعلمين.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn7", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل ببرنامج TOT")
            st.markdown('<div class="card-footer">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)
```eof

### التعديلات التي تم إضافتها:
1. **توسيط العناوين وتجميلها**: تم وضع خط ذهبي أنيق تحت العنوان الرئيسي وجعله في منتصف الصفحة دائماً.
2. **إظهار شعار الفرع**: تم إدراج الشعار المرفق (`image_526f40.jpg`) بوسط الصفحة الرئيسية.
3. **تحديث شريط التنقل الفرعي والقوائم**: محاذاة من اليمين إلى اليسار مع تنسيق الأزرار الحمراء والألوان المعتمدة في التصميم الأصلي.لإظهار الصفحة الرئيسية وتجميل العناوين وتوسيطها مع إضافة شعار (لوجو) الفرع، يمكنك استخدام الكود التالي بلغة **HTML & CSS**. 

هذا الكود منظم ومصمم بشكل عصري ومتجاوب، ويضم القائمة الرئيسية وشعار الفرع وتوسيط جميع العناوين بشكل أنيق:

```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الصفحة الرئيسية للفرع</title>
    <style>
        /* إعدادات عامة */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f6f9;
            color: #333;
        }

        /* رأس الصفحة والتصميم */
        header {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            padding: 30px 20px;
            text-align: center; /* توسيط محتوى الهيدر */
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }

        /* تنسيق اللوجو */
        .logo {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #ffffff;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        /* تجميل وتوسيط العناوين */
        h1, h2, h3 {
            text-align: center; /* توسيط العنوان */
            margin-top: 10px;
            margin-bottom: 15px;
        }

        .main-title {
            font-size: 2.2rem;
            font-weight: bold;
            color: #ffffff;
            letter-spacing: 1px;
        }

        /* قائمة التنقل */
        nav {
            background-color: #ffffff;
            border-bottom: 2px solid #e0e0e0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: center; /* توسيط روابط التنقل */
            flex-wrap: wrap;
        }

        nav ul li {
            margin: 0;
        }

        nav ul li a {
            display: block;
            padding: 15px 25px;
            color: #2a5298;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }

        nav ul li a:hover {
            background-color: #2a5298;
            color: #ffffff;
        }

        /* محتوى الصفحة الرئيسية */
        .container {
            max-width: 1000px;
            margin: 40px auto;
            padding: 20px;
        }

        .section-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }

        /* تجميل العناوين الفرعية خط سفلي أنيق */
        .decorated-header {
            position: relative;
            color: #1e3c72;
            padding-bottom: 10px;
        }

        .decorated-header::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background-color: #2a5298;
            border-radius: 2px;
        }
    </style>
</head>
<body>

    <!-- الهيدر مع اللوجو والعنوان الرئيسي -->
    <header>
        <!-- استبدل logo.png برابط صورة الشعار الخاص بك -->
        <img src="https://via.placeholder.com/120" alt="لوجو الفرع" class="logo">
        <h1 class="main-title">الصفحة الرئيسية لفرع التعليم</h1>
    </header>

    <!-- شريط التنقل العلوي -->
    <nav>
        <ul>
            <li><a href="#home">الصفحة الرئيسية</a></li>
            <li><a href="#about">عن الفرع</a></li>
            <li><a href="#administrations">الإدارات التعليمية</a></li>
            <li><a href="#platform">منصة الفرع</a></li>
        </ul>
    </nav>

    <!-- المحتوى الرئيسي -->
    <div class="container">
        
        <div class="section-card" id="about">
            <h2 class="decorated-header">عن الفرع</h2>
            <p style="text-align: center; line-height: 1.8; margin-top: 20px;">
                مرحباً بكم في المنصة الرسمية. يهدف الفرع إلى تقديم أفضل الخدمات التعليمية والتنظيمية للإدارات والطلاب.
            </p>
        </div>

        <div class="section-card" id="administrations">
            <h2 class="decorated-header">الإدارات التعليمية</h2>
            <p style="text-align: center; line-height: 1.8; margin-top: 20px;">
                يمكنك من خلال هذا القسم المتابعة والاطلاع على كافة الإدارات التعليمية التابعة للفرع.
            </p>
        </div>

        <div class="section-card" id="platform">
            <h2 class="decorated-header">منصة الفرع</h2>
            <p style="text-align: center; line-height: 1.8; margin-top: 20px;">
                بوابة معلوماتية متكاملة لتقديم الخدمات الإلكترونية للجميع بسرعة وكفاءة.
            </p>
        </div>

    </div>

</body>
</html>
