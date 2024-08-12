from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # List your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # You can specify allowed methods, or use ["*"] to allow all
    allow_headers=["*"],  # You can specify allowed headers, or use ["*"] to allow all
)

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

