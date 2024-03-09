import requests
import streamlit as st

headers = {"Authorization": f"Bearer {st.secrets.API_TOKEN}"}
        # [{"Context":"Please summarize this into a job description."}]
API_URL = f"https://api-inference.huggingface.co/models/{st.secrets.MODEL}"

@st.cache_data
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Add title and subtitle to the main interface of the app
st.title("Jibr-Jobr: turn the jibberish into a job description, and more!")
st.subheader("Job Description Synthesis, at the Click of a Button!")
st.markdown(":blue[Generate job descriptions that attract top talent!]")

# Add sidebar to the app
st.sidebar.markdown("### Competitive Intelligence Solutions for your Business!")
st.sidebar.markdown("#### :blue[Developed @ AgentC Laboratories by R.W. Schell]")
st.sidebar.markdown("##### :gray[Copyright 2024. Artificial Intelligentsia, LLC.      All rights reserved.]")
st.sidebar.markdown("###### :gray[AgentC Laboratories is a subsidiary of Artificial Intelligentsia, LLC.... blah blah blah...]")

col1, col2 = st.columns(2)
with col1:
    text_input = st.text_area("HEY [PROPPER-SPORTS-PERSONALITY], paste some sports questions here...", height=200)
    text_input = text_input + "\n\nPlease find the answer to this question and provide references, as able."
with col2:
    submit = st.button("Synthesize")
    if text_input and submit:
        ans = query({"inputs": text_input})
        ans = st.write(ans, height=200, label="Does this answer your question?")