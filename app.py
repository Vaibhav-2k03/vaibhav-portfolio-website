import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_pdf_viewer import pdf_viewer
import base64
import json,requests



st.set_page_config(page_title="Portfolio Website", page_icon='😊',layout='wide')

def load_lottiefile(filepath: str):
    with open(filepath, 'r',encoding="utf8") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



with st.sidebar:
    selected = option_menu('Vaibhav V',['Profile','Projects','Experience','Resume','Contact Me'],
                           menu_icon='mortarboard',
                           icons=['person','code-slash','clock','file-earmark-break','envelope-at'])

if selected == 'Profile':
    st.title("Hi, I'm Vaibhav :wave:")
    st.subheader('Machine Learning and Data Science Enthusiast 💻')
    st.divider()
    col1 , col2 = st.columns(2)
    with col1:
        with st.container():
            col1, c2, col3 = st.columns(3)
            with c2:
                st.markdown('<h3><u>About me</u></h3>', unsafe_allow_html=True)
           
            st.markdown("""
                <p>
                    Hi there! I'm an college student currently pursuing bachelors in the field of 
                    Artificial Intelligence and Machine Learning.  Fueled by a strong passion for this field, 
                    I'm constantly seeking new ways to leverage the power of data and algorithms to solve problems 
                    and create innovative solutions.
                </p>
                <br>
                <p> 
                    I will be excited to connect with others who share this passion, so feel free to reach out and let's 
                    discuss the exciting possibilities that lie ahead!   
                </p>
                """, unsafe_allow_html=True
            )
                
    with col2:
        load = load_lottiefile('lottiefiles/about.json')
        st_lottie(load,quality='high',speed='2',height=500,width=500)
    
elif selected == 'Projects':
    col1, col2,col3 = st.columns(3)
    with col1:
        st.title("Projects")
    with col2:
        load = load_lottiefile('lottiefiles/projects.json')
        st_lottie(load,quality='high',height=300)
    st.divider()
    with st.container():
        st.subheader("Chat with Multiple PDF's using Gemini Pro [Github]()")
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('images/project1.jpeg')
        with text_column:
            st.markdown("""
            - Developed a Q&A Chatbot that can take multiple PDFs as input and users can ask questions related to information in PDFs.
            - PDFs data was converted into vector embeddings using Google Gemini Pro API call and stored in the FAISS vector database locally.
            - Used Streamlit library to create frontend and Langchain library to create chatbot chain.
            - Libraries Used- Streamlit, Langchain, PyPDF, FAISS, Google-generativeai.
            """)
    st.divider()
    with st.container():
        st.subheader("Detection of Knee Osteoarthritis Disease  [Github]()")
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('images/project2.jpeg')
        with text_column:
            st.markdown("""
            - Created Deep Learning Model using Transfer Learning that detects Knee Osteoarthritis Disease with the help of X-rays of Knee.
            - Used the DenseNet Model to train the dataset which has 1.4M layers. This Model uses TensorFlow.
            - The Model Achieved an Accuracy of 90% with still scope of Improvement.
            - Libraries Used- Scikit Learn, Tensorflow, Keras, Numpy, Pandas and OpenCV.
            """)
    st.divider()
    with st.container():
        st.subheader("Student Management System  [Github]()")
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('images/project3.jpeg')
        with text_column:
            st.markdown("""
            - Created a GUI software where it can store information of Students in particular Organization.
            - The Software had been developed in Python as the front-end for MySQL as the backend forthe database.
            - Libraries Used- Tkinter, mySQL-connector.
            """)
    st.divider()


elif selected == 'Experience':
    col1, col2,col3 = st.columns(3)
    with col1:
        st.title("Experience")
    with col2:
        load = load_lottiefile('lottiefiles/experience.json')
        st_lottie(load,quality='high',height=300,speed=2)
    st.divider()
    with st.container():
        st.subheader("ML Intern, Flatworld Solutions Pvt Ltd.")
        st.write("*October 2023 to November 2023*")

        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('images/flatworld.jpeg')
        with text_column:
            st.markdown("""
            - Implemented Various Natural Language processing techniques for automation of extracting Personally Identifiable Information (PII) details.
            - Used BERT LLM, Microsoft's Presidio, and custom spaCy locally for masking PII details for prompts before feeding it to the LLMs.
            - Employed advanced tools to enhance accuracy, ensuring efficient information extraction and streamlined document processing and hosted a Local Flask API.
            """)
    st.divider()


elif selected == 'Resume':
    # file_path = 'Vaibhav Resume.pdf'
    # binary_data = file_path.getvalue()
    # pdf_viewer(input=binary_data,width=700)
    col1, col2 , col3 = st.columns(3)
    with col2:
        st.title('Resume📃')
    st.divider()
    with open("Files/Vaibhav Resume.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="1100" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)




elif selected == "Contact Me":
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,1))
        with text_column:
            st.header("Contact Form")
            st.write("Let's connect! You may either reach out to me at venuvaibhav6@gmail.com or use the form below!")
            with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                Name=st.text_input(label='Your Name',
                                    max_chars=100, type="default") #Collect user feedback
                Email=st.text_input(label='Your Email', 
                                    max_chars=100,type="default") #Collect user feedback
                Message=st.text_input(label='Your Message',
                                        max_chars=500, type="default") #Collect user feedback
                submitted = st.form_submit_button('Submit')
                if submitted:
                    st.info('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/vaibhav-v-2k3/"
            github_url = "https://github.com/Vaibhav-2k03"
            email_url = "mailto:venuvaibhav6@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
        with mid:
            st.empty()
        with image_column:
            load = load_lottiefile('lottiefiles/contact.json')
            st_lottie(load,quality='high',height=600)
            
st.markdown("*Copyright © 2024 Vaibhav V*")