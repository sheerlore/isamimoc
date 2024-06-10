from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/pooling/")
def read_pooling():
    return {"random": random.random()}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}