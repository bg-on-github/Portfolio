import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Biprajit Ghoshal')
    content = """
    Hi, I am Biprajit! I am a Python programmer with a passion for problem-solving. I am currently studying in KIIT-DU
    and am an ex-student of DBPC.
    """
    st.info(content)
