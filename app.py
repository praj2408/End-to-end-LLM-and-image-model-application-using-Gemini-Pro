from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## function to load gemini pro model and get responses


model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    
    return response.text



## initialize out streamlit app

st.set_page_config(page_title="Q&A Demo")

st.title("Gemini LLM Application")

input = st.text_input("input: ",key="input")

submit = st.button("Ask the Question")

## when submmit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is: ")
    st.write(response)