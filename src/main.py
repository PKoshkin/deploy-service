from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

load_dotenv()

SERVER_IP = os.environ["SERVER_IP"]
SERVER_PORT = os.environ["SERVER_PORT"]

SERVER = f"{SERVER_IP}:{SERVER_PORT}"

app = FastAPI()


@app.get("/")
def read_root():
    response = requests.get(SERVER)
    return {"response":response.text}

@app.get("/models")
def list_models():
    return {"models": models}
