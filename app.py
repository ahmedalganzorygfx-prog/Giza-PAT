import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="منصة الفرع التعليمية",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق تنسيقات CSS لتشبه التصميم المطلوب وتدعم اللغة العربية (RTL)
st.markdown("""
    <style>
    /* محاذاة النص من اليمين لليسار */
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* تصميم رأس القسم */
    .section-header {
        background-color: #937B2B;
        color: white;
        padding: 10px 25px;
        border-radius: 15px 0px 0px 0px;
        font-size: 22px;
        font-weight: bold;
        display: inline-block;
        float: right;
        margin-bottom: 20px;
    }

    /* تصميم بطاقات البرامج */
    .program-card {
        background-color: #1a252f;
        border: 3px solid #937B2B;
        border-radius: 30px 0px 30px 0px;
        padding: 25px;
        color: white;
        text-align: center;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    
    .program-title {
        color: #FFD700;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .program-desc {
        font-size: 14px;
        line-height: 1.6;
        color: #e0e0e0;
        margin-bottom: 20px;
    }

    .card-footer {
        background-color: #f4f4f4;
        color: #937B2B;
        text-align: center;
        padding: 8px;
        font-weight: bold;
        border-radius: 0 0 10px 10px;
        margin-top: 10px;
        border: 1px solid #937B2B;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- القائمة الجانبية (الشريط العلوي للتنقل) ----------------
st.sidebar.title("📌 القائمة الرئيسية")
main_tab = st.sidebar.radio(
    "انتقل إلى:",
    ["الرئيسية", "عن الفرع", "الادارات التعليمية", "منصة الفرع"]
)

# ---------------- محتوى التبويبات ----------------

if main_tab == "الرئيسية":
    st.title("🏠 الصفحة الرئيسية")
    st.write("أهلاً بك في منصة الفرع التعليمية الرقمية.")

elif main_tab == "عن الفرع":
    st.title("ℹ️ عن الفرع")
    st.write("نبذة تعريفية عن فرع الأكاديمية والخدمات المقدمة للمعلمين والمعلمات.")

elif main_tab == "الادارات التعليمية":
    st.title("🏢 الادارات التعليمية")
    st.write("دليل وتفاصيل الإدارات التعليمية التابعة للفرع.")

elif main_tab == "منصة الفرع":
    st.title("💻 منصة الفرع")
    
    # القائمة الفرعية لبرامج منصة الفرع
    sub_category = st.selectbox(
        "اختر الفئة التدريبية:",
        [
            "برامج القيادات التربوية",
            "برامج التسكين والترقي",
            "برنامج تغيير المسمى الوظيفي",
            "برامج الاعتماد"
        ]
    )

    st.markdown("---")

    # 1. قسم برامج القيادات التربوية
    if sub_category == "برامج القيادات التربوية":
        st.markdown('<div class="section-header">برامج القيادات التربوية</div><div style="clear:both;"></div>', unsafe_allow_html=True)
        st.write("")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
                <div class="program-card">
                    <div>
                        <div class="program-title">برنامج مدير ووكيل إدارة مدرسية</div>
                        <div class="program-desc">أحد البرامج الرقمية المعتمدة على منصة المعلم في الأكاديمية المهنية للمعلمين المتاحة للفئات المستهدفة من أعضاء هيئة التعليم في مصر.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="p1"):
                st.success("تم التوجيه لصفحة التسجيل لبرنامج مدير ووكيل إدارة مدرسية")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة مدرسية</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div>
                        <div class="program-title">برنامج مدير ووكيل إدارة تعليمية</div>
                        <div class="program-desc">برنامج تدريبي متخصص لإعداد وتأهيل القيادات للإدارات التعليمية بأساليب إدارية حديثة.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="p2"):
                st.success("تم التوجيه لصفحة التسجيل لبرنامج مدير ووكيل إدارة تعليمية")
            st.markdown('<div class="card-footer">برنامج مدير ووكيل إدارة تعليمية</div>', unsafe_allow_html=True)

        with col3:
            st.markdown("""
                <div class="program-card">
                    <div>
                        <div class="program-title">برنامج أساسيات التوجيه الفني</div>
                        <div class="program-desc">يركز على المهارات الأساسية للتوجيه الفني وكيفية تقديم الدعم والتقييم للعملية التعليمية.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="p3"):
                st.success("تم التوجيه لصفحة التسجيل لبرنامج أساسيات التوجيه الفني")
            st.markdown('<div class="card-footer">برنامج أساسيات التوجيه الفني</div>', unsafe_allow_html=True)

    # 2. قسم برامج التسكين والترقي
    elif sub_category == "برامج التسكين والترقي":
        st.markdown('<div class="section-header">برامج التسكين والترقي</div><div style="clear:both;"></div>', unsafe_allow_html=True)
        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                <div class="program-card">
                    <div>
                        <div class="program-title">برنامج التطبيقات التربوية للمعلم المساعد</div>
                        <div class="program-desc">برنامج موجه للمعلمين المساعدين للتأهيل والتسكين على الكادر الوظيفي.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="p4"):
                st.success("تم التوجيه لبرنامج التطبيقات التربوية")
            st.markdown('<div class="card-footer">برنامج التطبيقات التربوية للمعلم المساعد</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="program-card">
                    <div>
                        <div class="program-title">برنامج مهارات عامة في التدريس</div>
                        <div class="program-desc">يهدف لتطوير مهارات التدريس والأساليب التربوية الحديثة للمعلمين المستحقين للترقية.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("التسجيل بالبرنامج", key="p5"):
                st.success("تم التوجيه لبرنامج مهارات التدريس")
            st.markdown('<div class="card-footer">برنامج مهارات عامة في التدريس</div>', unsafe_allow_html=True)

    # 3. قسم تغيير المسمى الوظيفي
    elif sub_category == "برنامج تغيير المسمى الوظيفي":
        st.markdown('<div class="section-header">برنامج تغيير المسمى الوظيفي</div><div style="clear:both;"></div>', unsafe_allow_html=True)
        st.write("")

        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div>
                    <div class="program-title">برنامج تغيير المسمى الوظيفي</div>
                    <div class="program-desc">البرنامج المعتمد لمطابقة التخصصات وتغيير المسمى الوظيفي للكادر التعليمي.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
        with col_btn2:
            if st.button("التسجيل بالبرنامج", key="p6", use_container_width=True):
                st.success("تم التوجيه لبرنامج تغيير المسمى الوظيفي")
            st.markdown('<div class="card-footer">برنامج تغيير المسمى الوظيفي</div>', unsafe_allow_html=True)

    # 4. قسم برامج الاعتماد
    elif sub_category == "برامج الاعتماد":
        st.markdown('<div class="section-header">برامج الاعتماد</div><div style="clear:both;"></div>', unsafe_allow_html=True)
        st.write("")

        st.markdown("""
            <div class="program-card" style="max-width: 500px; margin: auto;">
                <div>
                    <div class="program-title">البرنامج الرقمي للاعتماد (TOT)</div>
                    <div class="program-desc">دورة تدريب المدربين الرقمية لإعداد مدربين معتمدين وفق معايير الأكاديمية.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
        with col_btn2:
            if st.button("التسجيل بالبرنامج", key="p7", use_container_width=True):
                st.success("تم التوجيه لبرنامج TOT")
            st.markdown('<div class="card-footer">البرنامج الرقمي للاعتماد TOT</div>', unsafe_allow_html=True)
