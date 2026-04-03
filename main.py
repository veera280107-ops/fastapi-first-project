from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, your API is working!"}
@app.get("/add")
def add(x: int, y: int):
    return {"result": x + y}
from pydantic import BaseModel

class Numbers(BaseModel):
    x: int
    y: int

@app.post("/add")
def add_numbers(data: Numbers):
    return {"result": data.x + data.y}
from pydantic import BaseModel

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginData):
    if data.username == "veera" and data.password == "9999":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}