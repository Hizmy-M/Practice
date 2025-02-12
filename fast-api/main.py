from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a data model for input validation
class NameRequest(BaseModel):
    name: str

@app.post("/greet/")
async def greet(request: NameRequest):
    return {"message": f"Hello, {request.name}!"}
