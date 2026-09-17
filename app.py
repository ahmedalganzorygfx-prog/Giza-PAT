import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="منصة الفرع التعليمية",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق تنسيقات CSS شاملة للمحاذاة من اليمين إلى اليسار (RTL)
st.markdown("""
    <style>
    /* محاذاة الصفحة بالكامل والأجزاء الداخلية */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* محاذاة الشريط الجانبي Sidebar */
    [data-testid="stSidebar"] {
        direction: rtl;
        text-align: right;
    }
    
    [data-testid="stSidebar"] * {
        text-align: right !important;
    }

    /* تعديل الاتجاه للقوائم المنسدلة والأزرار */
    .stSelectbox, .stRadio, .stButton {
        direction: rtl;
        text-align: right;
    }

    /* عنوان القسم الذهبي (يمين الصفحة) */
    .section-header-container {
        display: flex;
        justify-content: flex-start;
        border-bottom: 2px solid #ccc;
        margin-bottom: 25px;
        direction: rtl;
    }

    .section-title {
        background-color: #937B2B;
        color: white;
        padding: 10px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px 0px 0px 0px;
    }

    /* تصميم بطاقات البرامج */
    .program-card {
        background-color: #1b2631;
        border: 2px solid #937B2B;
        border-radius: 35px 0px 35px 0px;
        padding: 20px;
        color: white;
        text-align: right; /* محاذاة النص داخل البطاقة لليمين */
        direction: rtl;
        min-height: 250px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        margin-bottom: 10px;
    }

    .program-title {
        color: #FFD700;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 12px;
        text-align: right;
    }

    .program-desc {
        font-size: 14px;
        line-height: 1.6;
        color: #e0e0e0;
        text-align: right;
    }

    /* عنوان البطاقة السفي */
    .card-footer {
        background-color: #ffffff;
        color: #937B2B;
        text-align: center;
        padding: 8px;
        font-weight: bold;
        border: 1px solid #937B2B;
        border-radius: 0 0 10px 10px;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- القائمة الجانبية ----------------
st.sidebar.title("📌 القائمة الرئيسية")
main_tab = st.sidebar.radio(
    "الانتقال السريع:",
    ["الرئيسية", "عن الفرع", "الادارات التعليمية", "منصة الفرع"]
)

# ---------------- المحتوى الرئيسي ----------------

if main_tab == "الرئيسية":
    st.title("🏠 الصفحة الرئيسية")
    st.write("أهلاً بك في منصة الفرع التعليمية الرقمية.")

elif main_tab == "عن الفرع":
    st.title("ℹ️ عن الفرع")
    st.write("نبذة تعريفية عن خدمات فرع الأكاديمية المهنية للمعلمين.")

elif main_tab == "الادارات التعليمية":
    st.title("🏢 الإدارات التعليمية")
    st.write("دليل الإدارات التعليمية التابعة لفرع الأكاديمية.")

elif main_tab == "منصة الفرع":
    st.title("💻 منصة الفرع")
    
    # اختيار القائمة الفرعية
    sub_category = st.selectbox(
        "اختر الفئة التدريبية المطلوب عرضها:",
        [
            "برامج القيادات التربوية",
            "برامج التسكين والترقي",
            "برنامج تغيير المسمى الوظيفي",
            "برامج الاعتماد"
        ]
    )

    st.write("")

    # 1. برامج القيادات التربوية
    if sub_category == "برامج القيادات التربوية":
        st.markdown('''
            <div class="section-header-container">
                <div class="section-title">برامج القيادات التربوية</div>
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
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مدير ووكيل إدارة تعليمية</div>
                    <div class="program-desc">برنامج مخصص لتأهيل وإعداد القيادات للإدارات التعليمية وتطوير المهارات القيادية والأداء الإداري.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn2", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

        with col3:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج أساسيات التوجيه الفني</div>
                    <div class="program-desc">يهدف إلى تمكين الموجهين من المهارات الأساسية للإشراف الفني ومتابعة جودة العملية التعليمية.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn3", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    # 2. برامج التسكين والترقي
    elif sub_category == "برامج التسكين والترقي":
        st.markdown('''
            <div class="section-header-container">
                <div class="section-title">برامج التسكين والترقي</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                    <div class="program-desc">برنامج التأهيل التربوي المخصص للمعلمين المساعدين لاستكمال متطلبات التسكين على الكادر.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn4", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">برنامج مهارات عامة في التدريس</div>
                    <div class="program-desc">برنامج موجه لتطوير الكفايات التدريسية الحديثة واستراتيجيات التعلم لدى المعلمين المستحقين للترقية.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn5", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    # 3. تغيير المسمى الوظيفي
    elif sub_category == "برنامج تغيير المسمى الوظيفي":
        st.markdown('''
            <div class="section-header-container">
                <div class="section-title">برنامج تغيير المسمى الوظيفي</div>
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
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    # 4. برامج الاعتماد
    elif sub_category == "برامج الاعتماد":
        st.markdown('''
            <div class="section-header-container">
                <div class="section-title">برامج الاعتماد</div>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div class="program-card">
                    <div class="program-title">البرنامج الرقمي للاعتماد (TOT)</div>
                    <div class="program-desc">البرنامج التدريبي لإعداد وتأهيل المدربين المعتمدين رقمياً وفق معايير الجودة بالأكاديمية المهنية.</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="btn7", use_container_width=True):
                st.success("تم التوجيه لصفحة التسجيل.")
            st.markdown('<div class="card-footer">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)
