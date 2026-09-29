from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    age: int
    dept: str

@app.post("/employees")
def f1(emp: Employee):
    return {"message":"Employee enrollment is done","employee":emp}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)