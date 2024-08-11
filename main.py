from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
    
# Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Define a synchronous POST endpoint
@app.post("/items/")
def create_item(item: Item):
    # Simulate item creation and processing
    return {"name": item.name, "price": item.price, "description": item.description, "tax": item.tax}

