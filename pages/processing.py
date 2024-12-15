import time
import requests
import streamlit as st
from constants import BASE_URL

st.set_page_config(
    page_title="WebRAGe",
    initial_sidebar_state="collapsed"
)

if not "url" in st.session_state:
  st.switch_page("client.py")

st.title("WebRAGe")
st.write("Transform any docs into a semantically searchable, RAG-ready knowledge base with a single URL")

API_URL = f"{BASE_URL}/index-status"

base_url = st.session_state.url.split('/')[2]
st.status(f"Indexing {base_url} and all its subpages")

if st.button("Back"):
  st.session_state.url = ""
  st.switch_page("client.py")


headers = {"Content-Type": "application/json"}
data = {"url": st.session_state.url}
while True:
  try:
    response = requests.get(API_URL, headers=headers, json=data)
    result = response.json()

    if result["status"]:
      if result["indexed"]:
        st.switch_page("pages/search.py")
        break
      else:
        time.sleep(15)
    else:
      raise Exception()
  except Exception as e:
    st.write("Something went wrong. Please try again later")
    time.sleep(5)
    st.switch_page("client.py")
    break