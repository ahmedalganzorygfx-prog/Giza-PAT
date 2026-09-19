# ⏱️ تحديث الساعة والتاريخ بشكل حي وفوري ودقيق
st.markdown(
    f"""
    <div class="top-navbar">
        <div class="nav-right-container">
            <div class="nav-logo-text">
                {logo_navbar_tag}
                <span>الأكاديمية المهنية للمعلمين - فرع الجيزة</span>
            </div>
        </div>
        <div class="nav-left-actions">
            <div id="live-clock" class="live-clock-badge">
                🕒 جاري تحميل الوقت...
            </div>
            <a href="https://www.pat.edu.eg/platform-programs" target="_blank" class="teacher-platform-btn">
                منصة المٌعلم 🎓
            </a>
        </div>
    </div>

    <script>
    function updateClock() {{
        const now = new Date();
        
        // تنسيق التاريخ والوقت باللغة العربية مع ضبط الاتجاه ليظهر بشكل صحيح ومنتظم
        const optionsDate = {{ weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }};
        const dateStr = now.toLocaleDateString('ar-EG', optionsDate);
        
        const timeStr = now.toLocaleTimeString('ar-EG', {{ hour: '2-digit', minute: '2-digit', second: '2-digit' }});
        
        const clockElement = document.getElementById('live-clock');
        if (clockElement) {{
            clockElement.style.direction = "ltr";
            clockElement.style.textAlign = "left";
            clockElement.innerHTML = `${{dateStr}} &nbsp;|&nbsp; 🕒 ${{timeStr}}`;
        }}
    }}
    updateClock();
    setInterval(updateClock, 1000);
    </script>
""",
    unsafe_allow_html=True,
)
