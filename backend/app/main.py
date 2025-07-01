from fastapi import FastAPI
from elasticsearch import Elasticsearch
from elastic_transport import ConnectionError  # NEW
from pydantic import BaseModel

app = FastAPI()
es = Elasticsearch("http://elasticsearch:9200")
index_name = "documents"

class Document(BaseModel):
    text: str

@app.on_event("startup")
def startup_event():
    try:
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, body={
                "mappings": {
                    "properties": {
                        "text": {"type": "text"}
                    }
                }
            })
            print(f"✅ Created index '{index_name}'")
        else:
            print(f"ℹ️ Index '{index_name}' already exists")
    except ConnectionError as e:
        print(f"❌ Elasticsearch error: {e}")
        raise e  # prevent FastAPI from starting silently if ES fails

@app.get("/search")
async def search(query: str):
    try:
        res = es.search(index=index_name, body={"query": {"match": {"text": query}}})
        hits = res["hits"]["hits"]
        return hits[0]["_source"] if hits else {}
    except Exception as e:
        return {"error": f"Search failed: {e}"}

@app.post("/insert")
async def insert(doc: Document):
    try:
        res = es.index(index=index_name, body={"text": doc.text})
        return {"result": res["result"]}
    except Exception as e:
        return {"error": f"Insertion failed: {e}"}
