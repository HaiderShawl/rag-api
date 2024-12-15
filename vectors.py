import os
import uuid
import vecs
from model import encode
from dotenv import load_dotenv

load_dotenv()
DB_CONNECTION = os.getenv("DB_CONNECTION")

CHUNK_SIZE = 1000
DIMENSION_SIZE = 300

vx = vecs.create_client(DB_CONNECTION)
docs = vx.get_or_create_collection(
    name="docs",
    dimension=DIMENSION_SIZE,
)
status_docs = vx.get_or_create_collection(
    name="status",
    dimension=1,
)

docs.create_index(
    method=vecs.IndexMethod.auto,
    measure=vecs.IndexMeasure.cosine_distance,
)
status_docs.create_index(
    method=vecs.IndexMethod.auto,
    measure=vecs.IndexMeasure.cosine_distance,
)


def upsert(text, url):
    chunks = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    embeddings = encode(chunks)
    base_url = url.split('/')[2]

    records = [
        (
            str(uuid.uuid4()),
            embedding,
            {
                "url": url,
                "chunk": chunks[i],
                "base_url": base_url,
            }
        )
        for i, embedding in enumerate(embeddings)
    ]
    docs.upsert(records=records)


def query(text, filters={}):
    embeddings = encode([text])
    results = docs.query(
        data=embeddings[0],
        measure="cosine_distance",
        limit=5,
        filters=filters,
        include_value=True,
        include_metadata=True,
    )
    data = [{
        "id": result[0],
        "score": result[1],
        "metadata": result[2],
    } for result in results]

    return data


def update_indexing_status(url, status):
    base_url = url.split('/')[2]
    status_docs.upsert(
        records=[
            (
                base_url,
                [0],
                {
                    "status": status,
                    "base_url": base_url,
                },
            )
        ]
    )


def get_indexing_status(url):
    base_url = url.split('/')[2]
    filters = {"base_url": {"$eq": base_url}}
    result = status_docs.query(
        data=[0],
        limit=1,
        filters=filters,
        include_value=True,
        include_metadata=True,
    )
    return result
