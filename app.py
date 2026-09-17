# 5️⃣ نموذج التواصل مع فريق الدعم
elif current_tab == "التواصل مع الدعم":
    st.markdown("""
        <div class="centered-header">
            <div class="main-header-title">التواصل مع فريق الدعم الفني</div>
            <div class="sub-header-title">قم بملء النموذج التالي وإرساله عبر الواتساب إلى أحد أرقام الدعم الفني</div>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="support-form-container">', unsafe_allow_html=True)
        
        with st.form("support_form", clear_on_submit=False):
            name = st.text_input("الاسم ثلاثي / رباعي *", placeholder="أدخل اسمك بالكامل")
            
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                edara = st.selectbox("الإدارة التعليمية *", EDARAT_LIST)
            with col_f2:
                job = st.selectbox("الوظيفة الحالية *", JOBS_LIST)
                
            phone = st.text_input("رقم الموبايل (واتس آب للتواصل) *", placeholder="مثال: 01012345678")
            
            problem = st.text_area("شرح المشكلة *", placeholder="اكتب تفاصيل المشكلة التي تواجهك هنا...", height=120)
            
            file_uploaded = st.file_uploader(
                "إرفاق صحيفة أحوال إلكترونية حديثة (PDF أو صورة) *", 
                type=["pdf", "png", "jpg", "jpeg"]
            )
            
            submitted = st.form_submit_button("تجهيز رسالة الواتساب", use_container_width=True)
            
            if submitted:
                if not name or not phone or not problem or file_uploaded is None:
                    st.error("⚠️ يرجى ملء كافة الحقول المطلوبة وإرفاق صحيفة الأحوال الإلكترونية.")
                else:
                    st.session_state['form_data'] = {
                        'name': name,
                        'edara': edara,
                        'job': job,
                        'phone': phone,
                        'problem': problem,
                        'file_name': file_uploaded.name
                    }
                    st.success("✅ تم تجهيز بيانات النموذج! اختر أحد أرقام الدعم الفني أدناه للإرسال المباشر عبر الواتساب:")

        # إظهار أرقام التواصل عند اكتمال النموذج
        if 'form_data' in st.session_state and st.session_state['form_data']:
            data = st.session_state['form_data']
            
            # صياغة نص الرسالة
            msg_text = f"""*طلب دعم فني - منصة فرع الجيزة*
📌 *الاسم:* {data['name']}
📍 *الإدارة التعليمية:* {data['edara']}
💼 *الوظيفة الحالية:* {data['job']}
📱 *رقم التواصل:* {data['phone']}
📑 *صحيفة الأحوال:* مرفقة ({data['file_name']})

📝 *تفاصيل المشكلة:*
{data['problem']}"""
            
            import urllib.parse
            encoded_msg = urllib.parse.quote(msg_text)

            st.markdown("### 📲 اختر رقم الدعم الفني للإرسال:")
            
            whatsapp_numbers = [
                ("فريق الدعم الفني (1)", "201069996245"),
                ("فريق الدعم الفني (2)", "201120807631"),
                ("فريق الدعم الفني (3)", "201201109892")
            ]

            cols_wa = st.columns(3)
            for idx, (label, num) in enumerate(whatsapp_numbers):
                wa_url = f"https://wa.me/{num}?text={encoded_msg}"
                with cols_wa[idx]:
                    st.markdown(
                        f'''<a href="{wa_url}" target="_blank" style="
                            display: block;
                            text-align: center;
                            background-color: #25D366;
                            color: white;
                            font-weight: bold;
                            padding: 12px;
                            border-radius: 8px;
                            text-decoration: none;
                            box-shadow: 0 3px 6px rgba(0,0,0,0.16);
                        ">💬 إرسال إلى {label}<br><small>{num.replace('20', '0')}</small></a>''', 
                        unsafe_allow_html=True
                    )
            
            st.info("💡 **تنبيه:** بعد الضغط على زر الواتساب، يرجى إرفاق ملف صحيفة الأحوال الإلكترونية داخل المحادثة.")
            
        st.markdown('</div>', unsafe_allow_html=True)
