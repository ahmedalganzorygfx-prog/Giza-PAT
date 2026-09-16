import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO
from PIL import Image
import os
import urllib.request

# ---------------------------------------------------------
# 1. تهيئة وإعدادات الصفحة والتنسيقات المتكيفة مع الوضع الداكن
# ---------------------------------------------------------
st.set_page_config(
    page_title="الأكاديمية المهنية للمعلمين - فرع الجيزة",
    page_icon="🎓",
    layout="wide"
)

# دعم التجاوب مع الوضع الداكن (Dark Mode) والفاتح (Light Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    /* صندوق الترويسة متكيف مع الثيم الداكن والفاتح */
    .header-box {
        background-color: var(--background-secondary-color, rgba(128, 128, 128, 0.1));
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        text-align: center;
    }
    
    /* عناوين متكيفة مع لون النص الافتراضي للنظام */
    .main-header {
        color: var(--text-color, #1E3A8A);
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    .main-subheading {
        color: var(--text-color, #2A5298);
        opacity: 0.85;
        font-size: 16px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0px;
    }

    .section-title {
        color: var(--text-color, #1E3A8A);
        border-bottom: 3px solid #1E3A8A;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-align: right;
    }

    /* تحسين ظهور اللوجو على الخلفية الداكنة */
    .dark-mode-logo img {
        filter: drop-shadow(0px 0px 6px rgba(255, 255, 255, 0.6));
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. الترويسة واللوجو متوافق مع الوضع الداكن
# ---------------------------------------------------------
st.markdown('<div class="header-box">', unsafe_allow_html=True)

col_l, col_logo, col_r = st.columns([2, 1, 2])
with col_logo:
    logo_filename = None
    for fname in ['logo.png', 'logo.jpg', 'logo.jpeg', 'Logo.png']:
        if os.path.exists(fname):
            logo_filename = fname
            break
            
    if logo_filename:
        # إضافة تحسين لتوهج اللوجو في الشاشات الداكنة
        st.markdown('<div class="dark-mode-logo">', unsafe_allow_html=True)
        st.image(logo_filename, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; margin: 0;'>🎓</h1>", unsafe_allow_html=True)

st.markdown('''
    <h1 class="main-header">الأكاديمية المهنية للمعلمين - فرع الجيزة</h1>
    <p class="main-subheading">المنصة الرقمية الموحدة لإصدار وتدقيق شهادات الصلاحية</p>
</div>
''', unsafe_allow_html=True)
