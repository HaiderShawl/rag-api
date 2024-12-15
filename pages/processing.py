import time
import streamlit as st

st.set_page_config(page_title="WebRAGe")

if not "url" in st.session_state:
  st.switch_page("client.py")

st.title("WebRAGe")
st.write("Transform any docs into a semantically searchable, RAG-ready knowledge base with a single URL")

base_url = st.session_state.url.split('/')[2]
with st.status(f"Indexing {base_url} and all its subpages"):
  time.sleep(5)
  st.switch_page("pages/search.py")

if st.button("Back"):
  st.session_state.url = ""
  st.switch_page("client.py")