from fastapi import FastAPI
from elasticsearch import Elasticsearch
import uvicorn

app = FastAPI()

# Connect to Elasticsearch container
es = Elasticsearch(["http://elasticsearch:9200"])

@app.get("/search")
async def search():
    query = {"query": {"match_all": {}}}
    response = es.search(index="documents", body=query)
    return response["hits"]["hits"]

@app.post("/insert")
async def insert():
    data = {
        "id": "1",
        "text": "First paragraph from Wikipedia page on India"
    }
    es.index(index="documents", id=1, body=data)
    return {"message": "Document inserted"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9567)
