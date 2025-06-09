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
     /*header container*/
     .button-row {
     display: flex;
     justify-content: center;
     aligh-items: center;
     margin-top:20px
     gap: 3rem;
     }
     /* link style*/
    .stbutton > button {
    text-decoration: none;
    font-size: 1.2 rem;
    font-weight:600;
    color: white;
    background: transparent;
    border:none;
    cursor:pointer;
    transition: color 0.3s ease;
    }

    /* hover effect*/
    .stbutton > button: hover {
    color: #ff89ff;
    
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""
<style>
.header_left{
font-size: 10px;
font-weight:bold;
color: white;
display:flex;
align-items:center;
gap:0.5rem;
}

            
.header_center{
    background-color: transparent;
    bordr:none;
    color:#fff;
    font_size:1.1rem
    cursor:pointer;
}

.header-center button:hover{
color:"ff89ff;
text-decoration:underline
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
     <style>
     html {
            scroll-behavior: smooth;
            }
     </style>
     """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .intro_text{
    color:white;
    font-family: Arial;
    font-size: 18px;
    line-height: 1.5;
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

col1,col2,col3 = st.columns([1,2,3,])

with col1:
    st.markdown('<div class="header-left"> CF🎀 </div>',
                unsafe_allow_html=True)
with col2:
    st.markdown(
    <'div class="button-row">', unsafe_allow_html=True)
    c1,c2,c3,c4= st.columns(4)

    with c1:
         if st.button("About"):
              st.session_state.section="about"
     with c2:
          if st.button("Skills"):
               st.session_state.section="skills"
     with c3:
          if st.button("Projetcs"):
               st.session_state.section="projects"
     with c4:
          if st.button("Contact"):
               st.session_state.section="contact"
          
    st.markdown('</div>', unsafe_allow_html=True)
        
  
section = st.session_state.get("section", "")
if section == "about":
    st.markdown("## 🧠 About")
    st.write("Hi, I'm Chiraze – Junior Data Scientist, passionate about AI & ML.")
elif section == "skills":
    st.markdown("## 🧰 Skills")
    st.write("Python, TensorFlow, Scikit-learn, SQL, Pandas, etc.")
elif section == "projects":
    st.markdown("## 🚀 Projects")
    st.write("• Fraud detection model\n• NLP chatbot\n• Data dashboards")
elif section == "contact":
    st.markdown("## 📬 Contact")
    st.write("Email: chiraze@example.com\nLinkedIn: [link]")
with col3:
    st.markdown(
        """
        <div class=header-left> CF🎀 </div>
        """,unsafe_allow_html=True)
st.markdown('<div id="about"> </div>', unsafe_allow_html=True)
st.markdown("## About")
st.write("about section")


        
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
<div class="intro_text" id="about">

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

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("## Skills")
st.write("skills section")

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("## projects")
st.write(" projects section")

st.markdown('<div id="contact"> </div>', unsafe_allow_html=True)
st.markdown("## contact")
st.write("contact section")

# Your page content




















