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

hide_treamlit_style = """
<style>
#MainMenu {Visibility: hidden;}
footer {Visibility: hidden;}
header {Visibility: hidden;}
</style>
st.markdow(hide_streamlit_style, unsafe_allow_html=True)
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
st.title("Hello, I'm Chiraze!")
st.write("And I'am a Data Scientist.")

