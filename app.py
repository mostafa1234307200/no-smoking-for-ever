import streamlit as st
import numpy as np
import cv2
from PIL import Image

# إعداد الصفحة
st.set_page_config(
    page_title="مدرسة الأردن الأساسية المختلطة",
    layout="centered",
    page_icon="🚭",
)

# تنسيق CSS
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        }
        h1, h3 {
            color: #2c3e50;
            text-align: center;
        }
        .small {
            text-align: center;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h1>مدرسة الأردن الأساسية المختلطة</h1>", unsafe_allow_html=True)
st.markdown("<h3>كيف ستبدو بعد 30 سنة من التدخين؟</h3>", unsafe_allow_html=True)
st.markdown("<p class='small'>ارفع صورتك وشاهد التأثيرات السلبية للتدخين على المظهر</p>", unsafe_allow_html=True)

# رفع الصورة
uploaded_file = st.file_uploader("ارفع صورتك (jpg أو png)", type=["jpg", "jpeg", "png"])

# دالة التأثير
def apply_smoking_effect(img):
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # اصفر
