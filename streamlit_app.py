import streamlit as st
import base64
st.set_page_config(page_title="Chiraze Portfolio", page_icon="✨", layout="wide",initial_sidebar_state="collapsed")
st.title('🎈 Chiraze Feriani') 

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = "digital brain (2).png"  # your image file
img_base64 = get_base64(img_path)

hide_streamlit_style = """
<style>
#MainMenu {Visibility: hidden;}
footer {Visibility: hidden;}
header {Visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Your page content
intro_text = """ About Me i'am a Junior Data Scientist, newly graduated from research master in intelligent systems
i'am passionate with ai and machine leanring models"""

col1,col2= st.columns(2)
with col1:
    st.markdown(intro_text)
with col2:
    st.image("cyber-security-experts-working-with-tech-devices-neon-lights.jpg", captio="data scientist",use_column_width=True)



















