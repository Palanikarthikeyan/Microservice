from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product":product
    }
    
@app.put("/products/{product_id}")
def update_product(product_id: int,product: Product):
    return {
        "product_id": product_id,
        "message": "Product-updated",
        "product":product
    }

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return {
        "product_id": product_id,
        "message": "Product-deleted"
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)