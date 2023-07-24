import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG", width=400)

with col2:
    st.title("Harishankar Devops Engineer")
    content = """
    As an AWS certified Associate with extensive DevOps knowledge, 
    I possess a wide range of skills and expertise. With proficiency in more than 30 AWS services,
    I have a deep understanding of cloud computing and infrastructure automation. 
    My coding abilities include working with React.js, shell scripting, and Python (basic). 
    Additionally, I excel in maintaining and monitoring both EVM and Non-EVM based chains, 
    ensuring the smooth operation of blockchain infrastructure. Leveraging tools like PagerDuty, 
    I effectively handle alarm calls and incident management. With experience in system device management using 
    Hexnode, I ensure the security and efficiency of mobile devices. 
    I also prioritize data protection through password management with OnePassword. 
    Proficient in utilizing Jira and Slack, I excel in project management and team collaboration. 
    With a comprehensive skill set and a commitment to staying at the forefront of technology, 
    I am well-equipped to tackle complex challenges 
    and drive successful outcomes in the field of cloud computing and DevOps.
    """
    st.info(content)

contact = "Please feel free to contact me to learn Python UI with some functionality."
st.write(contact)
