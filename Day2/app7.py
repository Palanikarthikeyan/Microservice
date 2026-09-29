from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
def f1():
    return "<h2> Welcome to FastAPI WebPage response</h2>"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)