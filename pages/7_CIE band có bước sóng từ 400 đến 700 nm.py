
import streamlit as st
import colour
import matplotlib.pyplot as plt

st.title("🌈 CIE Band (400–700 nm)")

# Lấy phổ D65 và giới hạn từ 400–700 nm
spd = colour.SDS_ILLUMINANTS['D65'].copy()
spd = spd.align(colour.SpectralShape(400, 700, 1))

# Vẽ phổ dưới dạng band bằng matplotlib
fig, ax = plt.subplots()
colour.plotting.plot_single_sd(spd, ax=ax, title="CIE Band (400–700 nm)", y_label="Relative Power", standalone=False)

# Hiển thị biểu đồ lên web
st.pyplot(fig)
