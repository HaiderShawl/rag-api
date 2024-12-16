# WebRAGe

Transform any doc into a semantically searchable, RAG-ready knowledge base with a single URL, accessible by web and API

Check out the [demo](https://ragapi.streamlit.app/)


WebRAGe uses Spacy's `en_core_web_lg` model to encode the text into a 300-dimensional vector and 
indexes the vectors into supabase's vector database. The vectors are then queried using cosine similarity to retrieve the most similar documents.
