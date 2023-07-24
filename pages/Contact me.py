import streamlit as st
import time
from sentemail import sentmail


st.header("Contact Me")

with st.form(key="ContactMe"):
    userEmail = st.text_input("Enter Your Email Id") 
    message = st.text_area("Please Enter The Message")
    message = f"""RawMesaage: {message} + "\n" + UserEmail: {userEmail}"""
    button = st.form_submit_button("Submit")
    if button:
         sentmail(message)
         st.info("Thank You Contact Me")
         time.sleep(3)
         st.experimental_rerun()  