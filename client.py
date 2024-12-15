import re
import streamlit as st

st.set_page_config(page_title="WebRAGe")

if not "url" in st.session_state:
  st.session_state.url = ""

def submit():
  pattern = r'^https?:\/\/[\w\.-]+\.[a-z]{2,}'
  if not re.match(pattern, url):
    st.write("Invalid URL")
    return

  st.session_state.url = url
  st.switch_page("pages/processing.py")


st.title("WebRAGe")
st.write("Transform any docs into a semantically searchable, RAG-ready knowledge base with a single URL")


url = st.text_input("Enter the URL of the website you want to index")
if st.button("Submit"):
  submit()
