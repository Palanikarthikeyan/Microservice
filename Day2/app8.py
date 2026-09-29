from fastapi import FastAPI,HTTPException

app = FastAPI()

products = {
    1: "Laptop",
    2: "Mobile",
    3: "Computer"
}
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(
            status_code = 404,
            detail = 'Product Not found'
        )
    return {"id":product_id,"name":products[product_id]}

@app.post("/payment")
def make_payment(amount: float):
    if amount <= 0:
        raise HTTPException(
            status_code = 400,
            detail="Payment amount must be greater than zero"
        )
    return {
        "message":"Payment successful",
        "amount": amount
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)