import streamlit as st
import base64
import json

st.set_page_config(page_title="Chiraze Portfolio",
    page_icon="✨", layout="wide",
    initial_sidebar_state="collapsed")

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return b64

st.markdown(
    """
    <style>
    /* تكبير الـscroll bar العمودي */
    ::-webkit-scrollbar {
        width: 10px;
    }
    /* لون الـscroll bar */
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 8px;
    }
   
    </style>
    """,
    unsafe_allow_html=True
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden; height: 0px;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
 
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = "digital brain (2).png"
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

st.markdown("""
<style>
/* لضمان انو المحتوى ما يتغطاش بالـ header الثابت */
.section {
  padding-top: 120px;
  margin-bottom: 40px;
}

/* Navbar Styles */
.block-container {
    padding-top: 0 !important;
    margin-top: 0 !important;
}
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 5px 15px;
    font-size: 18px;
    font-weight: bold;
    z-index: 999;
    background: transparent; 
    box-shadow: 0 2px 12px 0 rgba(0,0,0,0.25);
    backdrop-filter: blur(2px);
}
.logo {
    display: flex;
    align-items: center;
    font-size: 20px;
    font-weight: bold;
    gap: 6px;
    color: pink;
    min-width: 80px;
}
.nav-container {
    flex: 1;
    display: flex;
    justify-content: center;
}
.nav-links {
    display: flex;
    gap: 100px;
}
.nav-links a {
    text-decoration: none;
    color: white;
    transition: color 0.3s ease;
    font-weight: bold;
}
.nav-links a:hover {
    color: pink;
    text-decoration: underline;
    font-size: 1.3rem;
}

/* Media Queries للتكيف مع مختلف أحجام الشاشات */
@media (max-width: 900px) {
    .nav-links {
        gap: 60px;
        font-size: 0.9em;
    }
}
@media (max-width: 600px) {
    .header {
        flex-direction: column;
        align-items: stretch;
        padding: 10px 5px;
        height: auto;
    }
    .logo {
        font-size: 18px;
        margin-bottom: 10px;
    }
    .nav-links {
        flex-direction: column;
        gap: 20px;
        margin-top: 10px;
        background: rgba(0,0,0,0.7);
        border-radius: 8px;
        width: 100vw;
        text-align: center;
        padding: 10px 0;
    }
    /* زيادة المسافة لكل section إذا احتجت */
    .section {
      padding-top: 10px;
    }

}
    .skill-logo-container {
            display: flex;
            flex-direction: column;
            align-itemns: center;
            transition: transform: 0.3s;
            cursor: pointer;
            margin-bottom: 8px;

            }
    .skill-logo-img {
            transition: transform 0.3s;

            
            }
    .skill-logo-name {
            opacity: 0;
            font-size: 14px;
            color: #fff;
            margin-top: 6px;
            transition: opacity 0.3s;
            font-weight: bold;
            letter-spacing: 1px
            
            }

    .skill-logo-container:hover .skill-logo-img {
            transform: scale(1.3);
            }
    .skill-logo-container:hover .skill-logo-name{
            opacity: 1;
            }
    .skills-section {
        display: flex; 
        flex-wrap:wrap;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin-top:20px
            }

    .project-section {
        display: flex;
        flex-wrap: wrap;
        background: #18181b;
        border-radius: 18px;
        box-shadow: 0 4px 24 px 0 rgba(0,0,0,0,18);
        margin: 32px 0;
        overflow: hidden;    
            }

    .project-img-part {
        flex: 1 1 320px;
        min-width: 260px;
        background: #fff;
        display: flex;
        align-items: center; 
        justify-content: center;
        padding: 32px 12px;   
            }
    .project-img-part img {
        max-width: 100%;
        max-height: 220px;
        border-radius: 16px;
        box-shadow: 0 2px 12px 0 rgba(0,0,0,0,10);   
            
            
            }
    .project-desc-part {
        flex: 2 1 400px;
        padding: 0px 32px 36px 32px;
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: center;    
            }
   
    .project-desc {
        font-size: 1.1rem;
        margin-bottom: 18px;
        color: #e0e0e0;    
            
            }
    .project-tags {
        display:flex;
        gap: 10px;
        margin-bottom: 18px;
        flex-wrap: wrap;
            
            }
    .project-tag {
            background: #2d0036;
            color: #f72585;
            border-radius: 12px;
            padding: 4px 14px;
            font-size: 0.95em;
            font-weight: 600;
            letter-spacing: 0.5px;
            
            
            }
    .project-btns {
            display:flex;
            gap: 16px;
            margin-top;
        
            
            }
    .project-btn-pink {
            background: #f72585;
            color: #fff;
            border: none;
            border-radius: 22px;
            padding: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 2px 8px 0 rgba(247, 37, 133, 0.10);
            transition: background 0.2s , transform 0.2s;
            outline: none;
            text-decoration: none;
            display: inline-block;
            }
    .project-btn-pink hover {
            background: #c9184a;
            transform: scale(1.05);
            }
    .project-btn-black {
            background: #18181b;
            color: #fff;
            border: none;
            border-radius: 22px;
            padding: 10px 28px 10px 22px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 2px 8px 0 rgba(0,0,0,0.10);
            transition: background 0.2s, transform 0.2s;
            outline: none;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            }
    .project-btn-black:hover {
            background: #333;
            transform: scale(1.05);
}
    .project-btn-black .arrow {
            font-size: 18px;
            margin-left: 4px;
            display: inline-block;
        }
@media (max-width: 900px) {
    .project-section {
        flex-direction: column;
    }
    .project-desc-part {
        padding: 24px 12px;
    }

}
}   .all_projects_button {
            display:flex;
            justify-content: center;
            margin: 40px 0;
            }

    .all_projects_button a{
            background: #f72585;
            color: white;
            border: none;
            border-radius:22px;
            padding: 16px 40px;
            font-size: 1.3rem;
            cursor: pointer;
            box-shadow: 0 2px 8px 0 rgba(247,37,133,0.10);
            transition: background 0.2s, transform 0.2s;
            outline: none;
            text-decoration: none;
            display: inline-block;
            letter-spacing: 1px;
            
            }
    .all_projects_button a:hover {
            background: #c9184a;
            transform: scale(1.05);
   
</style>
            
<div class="header">
    <div class="logo">
        <span>CF</span> 🎀
    </div>
    <div class="nav-container">
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown(""" 
<style>
.section { padding-top: 50px; margin-bottom: 40px; }
.block-container { padding-top: 0 !important; margin-top: 0 !important; }
.header { position: fixed; top: 0; left: 0; width: 100vw; height: 100px; display: flex; flex-direction: row; 
            align-items: center; justify-content: space-between; padding: 5px 15px; font-size: 18px; font-weight: bold; 
            z-index: 999; background: transparent; box-shadow: 0 2px 12px 0 rgba(0,0,0,0.25); backdrop-filter: blur(2px);}
.logo { 
            display: flex; align-items: center; font-size: 30px; font-weight: bold; gap: 6px; 
            color: pink; min-width: 80px;}
.nav-container { 
            flex: 1; display: flex; justify-content: center;}

@media (max-width: 900px) { .nav-links { gap: 60px; font-size: 0.9em; } }
@media (max-width: 600px) { .header { flex-direction: column; align-items: stretch; padding: 10px 5px; height: auto; }
             
            #.logo { font-size: 18px; margin-bottom: 10px; } 
            
            .nav-links { flex-direction: column; gap: 20px; margin-top: 10px; 

            background: rgba(0,0,0,0.7); border-radius: 8px; width: 100vw; text-align: center; padding: 10px 0; } 
            .section { padding-top: 10px; } }
.project-card{ background: rgba(30,30,40,0.85); border-radius: 20px; padding: 10px 10px 10px 10px; margin: 20px 0 10px 0; 
            color: #fff; box_shadow: 0 4px 12px rgba(0,0,0,0.2); font-family: 'Montserrat', sans-serif; min-height: 350px; 
            dislay: flex; flex-direction: column; align-items: center; justify-content: flex-start; }

.project-card:hover{ transform: scale(1.1); background: rgba(100,0,100,0.85); }
            
.project-card:hover .project-title{ opacity:1; }
            


.project-img { width:320px; height:150px; item-align: 
            center; justify-content: center; 
            object-fit: cover; border-radius: 20px; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.15); background: #fff; 
            padding:5px; display:block; 
            margin-top:10px; margin-left:auto; margin-right: auto; }



.main-title{ color:lightpink; 
            font-size:1.8em;
            item-align: center; 
            margin-top:0px; 
            justify-content: center;
            font-weight: bold; }

.section-title {  
            font-size:1.5rem; 
            font-weight: bold;
            color:#fff; 
            margin-top:10px;}
            
.project-tag { background:#2d0036; color:lightpink; border-radius:12px; padding:4px 14px; font-size:0.95em; font-weight:600;
             letter-spacing:0.5px; margin-top:50px; }
.about-me-card {
            background: rgba(30,30,40,0.85); border-radius: 20px; padding: 10px 10px 10px 10px; margin: 10px 0 10px 0; 
            color: #fff; box_shadow: 0 4px 12px rgba(0,0,0,0.2); font-family: 'Montserrat', sans-serif; min-height: 350px; 
            dislay: flex; flex-direction: column; align-items: center; justify-content: flex-start;
            }
</style>

""", unsafe_allow_html=True)


 
# قسم About
about_section = """
<div id="about" class="section" style="color:#ff5733;" >
</div>
"""
st.markdown(about_section, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class='main-title'>✨ About Me </div>
        <div class='about-me-card'>
                <div class="project-desc"> HI I’m Chiraze Feriani, a passionate Data Scientist with solid experience in building smart 
                solutions using advanced technologies like Python, Machine Learning, Deep Learning, and Data Visualization. I’ve worked 
                on several academic and personal projects, especially in supporting autistic children, where I applied techniques such as 
                3D Pose Estimation, CNN-LSTM, GCN-SAGE, and Explainable AI. 👩‍💻
                I enjoy solving real-world problems with tools like Pandas, NumPy, TensorFlow, PyTorch, and HuggingFace. I’m always eager to 
                learn new things and keep up with the latest trends in AI. My projects reflect my enthusiasm for technology and my desire to 
                make a positive impact, especially in health and education. Feel free to explore my portfolio to discover more about my skills and 
                experience! 🚀 </div>
        </div>        
        """, unsafe_allow_html=True)
    #st.markdown(about_section, unsafe_allow_html=True)
with col2:
    st.image("data_scientist.jpg", width=350)
    st.markdown(f"""
        """,
        unsafe_allow_html=True   
    ) 


# قسم Skills
skills_section = """
<div id="skills">
    <div class="main-title"> 🧠 My Skills</div> 
    <div class="skills-section">
     <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Python</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" alt="Streamlit" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Streamlit</span>
    </div>
     <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="NumPy" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Numpy</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" alt="Pandas" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Pandas</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" alt="Tensorflow" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">TensorFlow</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original.svg" alt="keras" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Keras</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">HTML</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">CSS</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" alt="matplotlib" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Matplotlib</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" width="68" style="background:white; border-radius:8px; padding:4px;"/> 
        <span class="skill-logo-name">Scikit-Learn</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" alt="PyTorch" width="68" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">PyTorch</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn" width="70" style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">Seaborn</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" alt="OpenCV" width="68"style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">OpenCV</span>
    </div>
    <div class="skill-logo-container">
        <img class="skill-logo-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="VS Code" width="68"style="background:white; border-radius:8px; padding:4px;"/>
        <span class="skill-logo-name">VS Code</span>
    </div>
</div>
                    
                    
</div>
"""
st.markdown(skills_section, unsafe_allow_html=True)

# قسم Projects
st.markdown("""
    <style>
        .img-gen-card{
            border-radius:20px;
            margin-top:50px;
            flex-direction:column;
            align-items:center;
            box-shadow: 0 2px 12px 0 rgba(0,0,0,0.10);
            margin-left:auto;
            margin-right:auto;
        }
        .project-title{
            color:lightpink;
            font-weight:bold;
            font-size:1.1rem;}
        .project-desc {
            color:white;}
    </style>
    """,unsafe_allow_html=True)
st.markdown("""
<style>
            .card {
            background: rgba(30,30,40,0.85); border-radius: 20px; padding: 10px 10px 10px 10px; margin: 20px 0 10px 0; 
            color: #fff; box_shadow: 0 4px 12px rgba(0,0,0,0.2); font-family: 'Montserrat', sans-serif; 
            dislay: flex; flex-direction: column; align-items: center; justify-content: flex-start;
            }
            """, unsafe_allow_html=True)
st.markdown("""
<div id ='projects' class='main-title'>🚀 My Projects </div>
<div class='card'>           
<div class='project-desc'> Each project has its own unique story, starting from a simple idea and growing into an exciting challenge.
             Through every project, I’ve explored new technologies, solved real problems, and pushed my skills to the next level.
             Whether academic or personal, every experience has taught me something valuable and helped me make a meaningful impact </div>
            </div>
""", unsafe_allow_html=True)
if "project_details" not in st.session_state: 
    st.session_state.project_details = None

def show_projects():
    st.markdown('<div class="section-title">🎓 Academic Projects</div>',unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        img_b64 = img_to_base64("au.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Mobile Application For Autistic Children</div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="app"/>
            <div class="project-desc"> a mobile application to help autistic children 
            that provides different games such as writting letters and numbers,
            coloring pictures, drag and drop words into correct place to form 
            a correct sentences to help hearing and repeating differnet words
            improve their pronounciation along with their auditory, visual, and sensory perception problems
            </div>""",unsafe_allow_html=True)
    with cols[1]: 
        img_b64 = img_to_base64("arm_flap.gif")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Detecting  Arm Flapping Behavior In 
            Autistic Children Using 3D Pose Estimation And CNN-LSTM Model</div>
            <img src="data:image/gif;base64, {img_b64}" class="project-img" alt="arm-flaping"/>
            <div class="project-desc"> A deep Learning project to detect the stereotypical arm flapping behavior in autistic children using 3D pose estimation and CNN-LSTM Model 
            <span class="project-tag">PYTHON</span>
            <span class="project-tag">MEDIAPIPE</span>
            <span class="project-tag">CNN</span>
            <span class="project-tag">LSTM</span>
            <span class="project-tag">LIME</span>
            <span class="project-tag">SHAP</span>
            </div>""", unsafe_allow_html=True)
    with cols[2]:
        img_b64 = img_to_base64("walk.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Autistic abnormal gait
            detection using 3D pose estimation and GCN-SAGE Model
            </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="gait"/>
            <div class="project-desc"> A deep Learning approach to detect abnormal gait patterns in autistic children using graph convolutional network and SAGE model</div>
            <span class="project-tag"> PYTHON</span>
            <span class="project-tag"> MEDIAPIPE</span>
            <span class="project-tag"> GCN</span>
            <span class="project-tag"> SAGE</span>
            <span class="project-tag"> EXPLAINABLE AI</span>
            </div>""",unsafe_allow_html=True)
    cols1 = st.columns(3)
    with cols1[0]:
        img_b64 = img_to_base64("sensors.jpg")
        st.markdown(f"""
        <div class="project-card">
                    <div class="project-title"> Brain signals processing using mne and graph transformer model </div>
                    <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="sensors"/>
                    <div class="project-desc"> preprocessing brain signals recorded during an experiment to determine the auditory perception
                    problems in autistic children </div>
        <span class="project-tag"> PYTHON</span>
            <span class="project-tag"> MEDIAPIPE</span>
            <span class="project-tag"> GCN</span>
            <span class="project-tag"> transformer </span>
            <span class="project-tag"> EXPLAINABLE AI</span>
        </div>
                    """, unsafe_allow_html=True)
        st.markdown('<div class="section-title"> 💡 Personal Projects</div>',unsafe_allow_html=True)
    cols2 = st.columns(3)
    with cols2[0]:
        img_b64 = img_to_base64("img_gen.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Image Generator </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="img_gen"/>
            <div class="project-desc"> Image generation app using 
            huggingface and LLM models</div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span>
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="img_gen_btn"):
            st.session_state.project_details = "img_gen"
             
    with cols2[1]:
        img_b64 = img_to_base64("sent.jpg")
        st.markdown(f""" 
        <div class="project-card">
            <div class="project-title"> Sentiment Analysis </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="sent_analysis"/>
            <div class="project-desc"> analysis text sentiment using hugging face and llm models</div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span>               
            </div>""", unsafe_allow_html=True)
        if st.button("Check Project", key="sent_analysis_btn"):
            st.session_state.project_details = "sent_analysis"
    with cols2[2]:
        img_b64= img_to_base64("text_sum.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Text Summarization </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="text_sum"/>
            <div class="project-desc"> Text summariaztion app using LLM and HuggingFace </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="text_sum_btn"):
            st.session_state.project_details = "text_sum"
    cols3 = st.columns(3)
    with cols3[0]:
        img_b64= img_to_base64("text_to_audio.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Text To Audio </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="text_audio"/>
            <div class="project-desc"> Text to audio app using LLM and HuggingFace </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="text_audio_btn"):
            st.session_state.project_details = "text_audio"
    with cols3[1]:
        img_b64= img_to_base64("text_gen.png")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Text To Audio </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="text_gen"/>
            <div class="project-desc"> Text generation app using LLM and HuggingFace </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="text_gen_btn"):
            st.session_state.project_details = "text_gen"
    with cols3[2]:
        img_b64= img_to_base64("research_sum.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Text To Audio </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="research"/>
            <div class="project-desc"> research pappers summarization app using LLM and HuggingFace </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="research_sum_btn"):
            st.session_state.project_details = "research_sum"
    cols4 = st.columns(3)
    with cols4[0]:
        img_b64= img_to_base64("diabetese.png")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Diabetese predicition </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="diab"/>
            <div class="project-desc"> diabetese prediction using machine learning </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="diab_btn"):
            st.session_state.project_details = "diabetese"
    with cols4[1]:
        img_b64= img_to_base64("nlp.jpg")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Text classification </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="text_class"/>
            <div class="project-desc"> Text classification app using LLM and HuggingFace </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="text_class_btn"):
            st.session_state.project_details = "text_class"
    with cols4[2]:
        img_b64= img_to_base64("churn.png")
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title"> Churn Customer Prediction </div>
            <img src="data:image/jpg;base64,{img_b64}" class="project-img" alt="churn"/>
            <div class="project-desc"> churn customer prediction app with machine learning and nlp </div>
            <span class="project-tag"> PYTHON </span>
            <span class="project-tag"> HUGGING FACE </span>
            <span class="project-tag"> LLM </span> 
            </div>""",unsafe_allow_html=True)
        if st.button("Check Project", key="churn_btn"):
            st.session_state.project_details = "churn"

    # ... كمل باقي الكارتات بنفس الطريقة
def show_img_gen_details():
    import requests
    from PIL import Image
    from io import BytesIO
    import base64
    import os
    import uuid
    import glob

    st.markdown("""
    <style>
        .img-gen-card{
            border-radius:20px;
            margin-top:50px;
            flex-direction:column;
            align-items:center;
            box-shadow: 0 2px 12px 0 rgba(0,0,0,0.10);
            margin-left:auto;
            margin-right:auto;
        }
        .project-title{
            color:lightpink;
            font-weight:bold;
            font-size:1.8rem;}
        .project-desc {
            color:white;}
    </style>
    """,unsafe_allow_html=True)

    if not os.path.exists("images_history"):
        os.makedirs("images_history")
    HF_TOKEN = "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"
    HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Accept": "image/png"
    }

    col = st.columns(2)
    with col[0]:
        st.markdown("""<div class="img-gen-card">
                            <div class="project-title">AI Image 
                            Generator
                        </div>
                        <div class="project-desc"> Enter a prompt and click to 
                            generate an image using Stable Diffusion
                        </div>
                   """, unsafe_allow_html=True)
        prompt = st.text_input("")
        generate = st.button("Generate")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="project-title"> 🖼️ Generated Images History </div>', unsafe_allow_html=True)
    if "images_history" not in st.session_state:
        st.session_state["images_history"] = []
    with col[1]:
        if generate:
            if prompt:
                with st.spinner("Generating your image ..."):
                    try:
                        response = requests.post(
                            HF_API_URL,
                            headers = headers,
                            json={"inputs":prompt}
                        )
                        if response.status_code==200:
                            image = Image.open(BytesIO(response.content))
                            st.image(image, caption="Generated image", use_container_width=True)
                            img_id = str(uuid.uuid4())
                            img_path = f"images_history/{img_id}.png"
                            image.save(img_path)
                        else:
                            st.error(f"failed to generate the image: {response.text}")
                    except Exception as e:
                        st.error(f" an error has occired: {e}")
            else:
                st.warning("Please Enter Your Prompt")

    img_files = sorted(glob.glob("images_history/*.png"), reverse=True)
    if img_files:
        cols = st.columns(4)
        for idx, img_path in enumerate(img_files):
            with cols[idx % 4]:
                st.image(img_path)
    else:
        st.info("No Generated Images Yet")

    # زر الرجوع
    if st.button("🔙 back"):
        st.session_state.project_details = None

# switching بين الكارتات والتفاصيل
if st.session_state.project_details == "img_gen":
    show_img_gen_details()
elif st.session_state.project_details =="sent_analysis":
    pass
else:
    show_projects()


# قسم Contact
contact_section = """
<div id="contact" class="section">
    <div class='main-title'>Contact</div>
</div>
"""
st.markdown(contact_section, unsafe_allow_html=True)
import streamlit as st
import smtplib
from email.mime.text import MIMEText
 
st.title("Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send"):
    if name and email and message:
        # إعدادات الإيميل
        sender = "chiraze.fer@gmail.com"
        password = "YOUR_APP_PASSWORD"  # استعمل app password مش كلمة السر العادية
        receiver = "chiraze.fer@gmail.com"

        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg["Subject"] = "New Portfolio Message"
        msg["From"] = sender
        msg["To"] = receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, msg.as_string())
            st.success("Message sent successfully! ✅")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill all the fields.")
    


# مثال على استعمال الأعمدة في قسم About 
 
