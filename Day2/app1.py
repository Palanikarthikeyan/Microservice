from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def f1():
    return "Hello"

@app.get("/data")
def f2():
    return {"code":123,"path":"/var/www/","daemon":"httpd"}

@app.get("/products")
def f3():
    return [{"id":1,"name":"pA","pcost":1000},{"id":2,"name":"pB","pcost":2000}]

@app.get("/products/{product_id}")
def f4(product_id: int):
    return {"product_id":product_id,"message":"product_found"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)
