from fastapi import FastAPI
import asyncio
import time
app = FastAPI()

# Synchronous end point
@app.get("/sync")
def f1():
    time.sleep(5)
    return {"messsage":"Sync task completed"}

# Async end point
@app.get("/async")
async def f2():
    await asyncio.sleep(5)
    return {"message":"Async task completed"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)
    