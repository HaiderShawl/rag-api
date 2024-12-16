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

API_URL = f"{BASE_URL}/query-vectors"

tab1, tab2 = st.tabs(["Web", "API"])

# tab1
def search():
  headers = {"Content-Type": "application/json"}
  data = {"text": query, "url": st.session_state.url}
  response = requests.post(API_URL, headers=headers, json=data)
  results = response.json()["data"]

  for index, result in enumerate(reversed(results)):
    with tab1.expander(f"{result['metadata']['url']}"):
      st.write(f"Cosine Similarity score: {result['score']:.2f}")
      st.write(result['metadata']["chunk"])
      st.write(f"Visit the page [here]({result['metadata']['url']})")        


base_url = st.session_state.url.split('/')[2]
query = tab1.text_input(f"Enter any query to search the indexed website ({base_url})")

if tab1.button("Search"):
  search()


# tab2
tab2.write("API Usage")

tab2.code("""
import requests
API_URL = "https://ragapi-640407272857.us-west1.run.app/query-vectors"
headers = {"Content-Type": "application/json"}
data = {"text": "How to enable custom CSS in Octane AI quizzes", "url": "https://help.octaneai.com/en/collections/9496268-developer-docs"}
response = requests.post(API_URL, headers=headers, json=data)
results = response.json()
""")