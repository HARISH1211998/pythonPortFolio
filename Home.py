import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, emptycol, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.JPG", width=400)

with col2:
    st.title("Harishankar Devops Engineer")
    content = """
    As an AWS certified Associate with extensive DevOps knowledge, 
    I possess a wide range of skills and expertise. With proficiency in more than 30 AWS services 
    I am well-equipped to tackle complex challenges 
    and drive successful outcomes in the field of cloud computing and DevOps.
    """
    st.info(content)

contact = "Please feel free to contact me to learn Python UI with some functionality."
st.write(contact)

df = pandas.read_csv("data.csv", sep=";")

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])



