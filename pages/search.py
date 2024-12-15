import time
import requests
import streamlit as st

st.set_page_config(page_title="WebRAGe")

if not "url" in st.session_state:
  st.switch_page("client.py")


st.title("WebRAGe")
st.write("Transform any docs into a semantically searchable, RAG-ready knowledge base with a single URL")

API_URL = "https://ragapi-640407272857.us-west1.run.app/query-vectors"

tab1, tab2 = st.tabs(["Web", "API"])

# tab1
def search():
  headers = {"Content-Type": "application/json"}
  data = {"text": query}
  # response = requests.post(API_URL, headers=headers, json=data)
  # results = response.json()

  results = [{"id":"d5fb5c44-a5dc-40bd-8bec-c9f131ce4cdb","metadata":{"chunk":"Custom CSS Explanation & Class Names | Octane AI Help CenterSkip to main contentEnglish;EnglishEnglish;EnglishTable of contentsAll CollectionsDeveloper DocsGuidesCustom CSS Explanation & Class NamesCustom CSS Explanation & Class Names#custom-css #developer #quizWritten by Mark Baek Updated over a year agoTable of contentsThis document includes explanations of Octane AI's quiz HTML structure, as well as the CSS class names that are assigned when the custom CSS option is enabled for a quiz. This can be done with these quick steps:Open your quiz in the Octane AI quiz editor.In the quiz editor, navigate to Design and click on Custom CSS.Click on 'Enable custom class names'.While CSS class names can be customized or even changed to match existing class names on your website, the ones below will be the default class names present in each Octane AI quiz when custom CSS is enabled.  💡 What you'll learnGlobal wrapper HTML structure (jump to section)Text HTML structure (jump to section)  💡 Prere","url":"https://help.octaneai.com/en/articles/8179591-custom-css-explanation-class-names"},"score":0.167126936930748},{"id":"7bfa2b43-ac48-48ca-abf3-879414bd7510","metadata":{"chunk":" in this document.    How to turn on custom CSS Open your quiz in the Octane AI quiz editor.In the quiz editor, navigate to Design and click on Custom CSS.Click on 'Enable custom class names'.When disabled, many quiz elements will have dynamic class names instead.  💡 What does turning custom CSS on do? When custom CSS is disabled, quizzes will use dynamic classes for most elements.  Enabling custom CSS will set many classes to a set of default class names. These class names can be changed inside of Octane AI's quiz editor and are set per quiz. You can check out a glossary of custom CSS class names, as well as an explanation of Octane AI's HTML structure here.   Editing class namesYou can either use the class names that are generated when custom CSS is enabled, or replace the class names with your own. You can use multiple classes for a specific element as long as each entry is separated by a space. ❓Where do I add my custom CSS code? Custom CSS code should be added to the same environm","url":"https://help.octaneai.com/en/articles/5739305-customizing-css-in-octane-ai-quizzes-enterprise"},"score":0.188943222706159},{"id":"ea9a63ae-e23a-4452-bd61-9b6b691de90f","metadata":{"chunk":" in this document.    How to turn on custom CSS Open your quiz in the Octane AI quiz editor.In the quiz editor, navigate to Design and click on Custom CSS.Click on 'Enable custom class names'.When disabled, many quiz elements will have dynamic class names instead.  💡 What does turning custom CSS on do? When custom CSS is disabled, quizzes will use dynamic classes for most elements.  Enabling custom CSS will set many classes to a set of default class names. These class names can be changed inside of Octane AI's quiz editor and are set per quiz. You can check out a glossary of custom CSS class names, as well as an explanation of Octane AI's HTML structure here.   Editing class namesYou can either use the class names that are generated when custom CSS is enabled, or replace the class names with your own. You can use multiple classes for a specific element as long as each entry is separated by a space. ❓Where do I add my custom CSS code? Custom CSS code should be added to the same environm","url":"https://help.octaneai.com/en/articles/5739305-how-to-enable-custom-css-in-octane-ai-quizzes"},"score":0.188943222706159}]
  for result in results:
    with tab1.expander(f"{result['metadata']['url']}"):
      st.write(f"Cosine Similarity score: {result['score']:.2f}")
      st.write(result["metadata"]["chunk"])


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
data = {"text": "How to enable custom CSS in Octane AI quizzes"}
response = requests.post(API_URL, headers=headers, json=data)
results = response.json()
""")