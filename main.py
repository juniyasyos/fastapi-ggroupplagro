from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

from auth import get_api_key

app = FastAPI()

API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

@app.get("/")
async def read_root():
    return {"message": "Welcome to my API"}

@app.get("/secure-data/")
async def get_secure_data(api_key: APIKey = Depends(get_api_key)):
    return {"message": "This is secured data"}

@app.get("/public-data/")
async def get_public_data():
    return {"message": "This is public data"}
