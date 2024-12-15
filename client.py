import re
import requests
import streamlit as st
from constants import BASE_URL

st.set_page_config(
    page_title="WebRAGe",
    initial_sidebar_state="collapsed"
)

if not "url" in st.session_state:
  st.session_state.url = ""

st.title("WebRAGe")
st.write("Transform any docs into a semantically searchable, RAG-ready knowledge base with a single URL")

API_URL = f"{BASE_URL}/index-website"

def submit():
  try:
    pattern = r'^https?:\/\/[\w\.-]+\.[a-z]{2,}'
    if not re.match(pattern, url):
      st.write("Invalid URL")
      return

    headers = {"Content-Type": "application/json"}
    data = {"url": url}
    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()

    if not result or "status" not in result or not result["status"]:
      raise Exception("Invalid response")

    st.session_state.url = url

    if result["already_indexed"]:
      st.switch_page("pages/search.py")
    else:
      st.switch_page("pages/processing.py")
  except Exception as e:
    st.write("Something went wrong. Please try again later")


url = st.text_input("Enter the URL of the website you want to index")
if st.button("Submit"):
  submit()
