import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="emailform"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    message = "Subject: Contact Mail from " + user_email + "\n\nFrom: "+user_email+"\n" + message
    button = st.form_submit_button("Mail")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
