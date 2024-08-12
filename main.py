from typing import Optional

import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

app = FastAPI()
# Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # List your allowed origins here
#     allow_credentials=True,
#     allow_methods=["*"],  # You can specify allowed methods, or use ["*"] to allow all
#     allow_headers=["*"],  # You can specify allowed headers, or use ["*"] to allow all
# )


CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",  
    "Access-Control-Allow-Methods": "*", 
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Credentials": "true"
}

@app.middleware("http")
async def debug_cors_issue(request: Request, call_next):
    logger.debug("Received request: %s", request.url.path)
    response = await call_next(request)
    
    for header, value in CORS_HEADERS.items():
        response.headers[header] = value
        logger.debug("Append header: %s: %s", header, value)
    
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Define a synchronous POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

