import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
st.set_page_config(page_title="Mohamed Mahmoud portfolio")

load_css()
st.write("[![Watch](https://komarev.com/ghpvc/?username=thesnak&label=Profile%20views&color=0e75b6&style=flat)](https://gitHub.com/thesnak)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('pp.png'))

st.header('''Mohamed Mahmoud Ali
 Ai Engineer | Data Scientist | Bioinformatics Engineer.''')

st.info('''I am a fresh graduate of Computer Science. I am seeking to have a job as a software engineer or data
scientist as I have good knowledge in these fields, good programming skills (Python - C++ - Java),
algorithms, data structure, databases, object-oriented programming, deep learning, machine learning,
and data analysis. I'm looking forward to learning more.''')

icon_size = 20
cv="/mohamed_mahmoud_cv.pdf"

st_button('youtube', 'https://youtube.com/@thesnak', 'My YouTube channel', icon_size)
st_button('youtube', 'https://youtube.com/@aitronix8705', 'Aitronix YouTube channel', icon_size)
st_button('medium', 'https://medium.com/@thesnak', 'Read my Blogs', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/mohamed-thesnak/', 'Follow me on LinkedIn', icon_size)
st_button('facebook', 'https://www.facebook.com/mohamed.thesnak.official1/', 'Follow me on Facebook', icon_size)

with open(cv[1:], "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download My Cv",data=PDFbyte,file_name="mohamed_mahmoud_cv.pdf",mime='application/octet-stream')