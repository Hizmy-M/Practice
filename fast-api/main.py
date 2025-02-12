from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
async def read_users(user_id : int):
    return {
        "user_id" : user_id,
        "name" : "naming"
        }
