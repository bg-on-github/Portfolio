import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', width=46 0)

with col2:
    st.title('Biprajit Ghoshal')
    content = """
    Hi, I am Biprajit! I'm currently a CSE undergraduate at Kalinga Institute of Industrial Technology with a key interest in deep learning.

My interest in Computer Science has accompanied me through my school life, fuelled by a desire to finding solutions to every hurdle I come across. I am constantly looking for ways to broaden my knowledge and experience in this field through certifications, courses and participations in events.

Currently my skills include knowledge in the following programming languages: C, C++, Java, HTML, Python; creating and implementing RNNs, CNNs and deep generative networks using PyTorch and Tensorflow. I'm currently learning more about GANs.

An avid and innovative mind eager to deliver on my responsibilities, I am dependable as a team-member and creative in solving problems.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built using Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for i, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for i, row in df[10:].iterrows():
        st.header(row["title"])