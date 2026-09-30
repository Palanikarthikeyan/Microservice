from fastapi import FastAPI,HTTPException

app = FastAPI(title="Product service")

products = {
    101: {"id":101,"name":"pA","price":100000},
    102: {"id":102,"name":"pB","price":500},
    103: {"id":103,"name":"pC","price":2000}
}
@app.get("/products")
def get_products():
    return list(products.values())

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = products.get(product_id)
    
    if product is None:
        raise HTTPException(status_code=404,detail="Product Not Found")
    return product


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8002)