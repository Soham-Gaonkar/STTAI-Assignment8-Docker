from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
import uvicorn

app = FastAPI()

# Load templates for rendering HTML
templates = Jinja2Templates(directory="templates")

# Backend URL (modify with VM 2 internal IP later)
BACKEND_URL = "http://backend:9567"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get")
async def get_best_match():
    response = requests.get(f"{BACKEND_URL}/search")
    return response.json()

@app.post("/insert")
async def insert_data():
    response = requests.post(f"{BACKEND_URL}/insert")
    return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9567)
