from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

app = FastAPI()

SECRET_key = "mysecret123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Login 
@app.post("/login")
def login(username: str,password: str):
    if username == "karthik" and password == "python123":
        token = jwt.encode({"sub":username},SECRET_key,algorithm=ALGORITHM)
        return {"access_token":token}
    raise HTTPException(status_code=401,detail="Invalid username or password")

# protected API
@app.get("/profile")
def profile(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token,SECRET_key,algorithms=[ALGORITHM])
        return {"message":f"Welcome {data['sub']}"}
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401,detail="Invalid Token")
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8000)



        
