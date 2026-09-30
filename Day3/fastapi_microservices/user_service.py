from fastapi import FastAPI,HTTPException

app = FastAPI(title="User service")

# let we fetched from DB
users = {
    1: {"id":1,"name":"arun"},
    2: {"id":2,"name":"vijay"},
    3: {"id":3,"name":"theeb"}
}

@app.get("/users")
def get_users():
    return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,port=8001)
   