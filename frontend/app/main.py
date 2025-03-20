from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BACKEND_URL = "http://backend:9567"

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/get")
def get_document(request: Request, query: str = Form(...)):
    res = requests.get(f"{BACKEND_URL}/search", params={"query": query})
    result = res.json()
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.post("/insert")
def insert_document(request: Request, text: str = Form(...)):
    res = requests.post(f"{BACKEND_URL}/insert", json={"text": text})
    result = res.json()
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
