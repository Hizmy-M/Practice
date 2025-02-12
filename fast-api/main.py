from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")  # Define a GET route
async def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")  # Path parameter
async def greet(name: str):
    return {
        "message1": f"Hello, {name}!",
        "message":"asdasdadsasdasd"
        }
