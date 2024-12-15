import spacy

nlp = spacy.load("en_core_web_lg")

def encode(chunks):
    embeddings = [nlp(chunk).vector.tolist() for chunk in chunks]
    return embeddings
