import streamlit as st
import base64
st.set_page_config(page_title="Chiraze Portfolio", page_icon="✨", layout="wide",initial_sidebar_state="collapsed")
hide_streamlit_style = """
<style>
#MainMenu {Visibility: hidden;}
footer {Visibility: hidden;}
header {Visibility: hidden;}
</style>
"""
st.markdown("""
<style>
.header_left{
font_size: 2.5rem;
font_weight:bold;
color: #ff89ff;
display:flex;
align_items:center;
gap:0.5rem;
}

.header_center{
    background-color: transparent;
    bordr:none;
    color:#fff;
    font_size:1.1rem
    curser:pointer;
}

.header-center button:hover{
color:"ff89ff;
text_decoration:underline
}

</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .intro_text{
    color:white;
    font_family: Arial;
    font_size: 18px;
    line_height: 1.5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = "digital brain (2).png"  # your image file
img_base64 = get_base64(img_path)

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

intro_text = """ 
<div class="intro_text">

<h2>About Me</h2>
<p>i'am a Junior Data Scientist, newly graduated from research master in intelligent systems
i'am passionate with ai and machine leanring models </p>
</div>
"""

col1,col2= st.columns(2)
with col1:
    st.markdown(intro_text, unsafe_allow_html=True)
with col2:
    st.image("cyber-security-experts-working-with-tech-devices-neon-lights.jpg", caption="data scientist",use_container_width=True)




# Your page content




















