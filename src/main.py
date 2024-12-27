from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()


@app.get("/")
def read_root():
    return {"message": "Hello there"}

@app.get("/models")
def list_models():
    return {"models": models}
