from fastapi import FastAPI, Request
from elasticsearch import Elasticsearch
from pydantic import BaseModel

app = FastAPI()
es = Elasticsearch("http://elasticsearch:9200")

class Document(BaseModel):
    text: str

@app.get("/search")
async def search(query: str):
    res = es.search(index="documents", body={"query": {"match": {"text": query}}})
    hits = res["hits"]["hits"]
    return hits[0]["_source"] if hits else {}

@app.post("/insert")
async def insert(doc: Document):
    res = es.index(index="documents", body={"text": doc.text})
    return {"result": res["result"]}
