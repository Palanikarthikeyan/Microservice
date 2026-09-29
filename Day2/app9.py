from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()

# this is not api endpoint 
def verify_api_key(api_key: str):
    if api_key != "ABC123":
        raise HTTPException(status_code=401,detail="Invalid API Key")
    return api_key

# api - end point
@app.get("/products")
def get_product(api_key: str = Depends(verify_api_key)):
    return {"message":"Products returned"}

'''
@app.get("/orders")
def orders(api_key:Depends(verify_api_key)):
     ...
     
     
@app.get("/customers")
def customer(api_key:Depends(verify_api_key)):
...
'''


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)