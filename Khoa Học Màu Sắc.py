import streamlit as st
from PIL import Image

# Cấu hình trang
st.set_page_config(page_title="Khoa học màu sắc", layout="wide")

# Giao diện chia cột: để logo bên phải
col1, col2 = st.columns([10, 1])
with col2:
    st.image("Logo.png", width=30)
    


# Nội dung chính
st.write("# 👋 chào mừng bạn đến với khoa học màu sắc")
st.write("## Welcome to the Liems, i'm the LLiems God, sbd 001")

