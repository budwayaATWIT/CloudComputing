
import unittest
import json
import requests
import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI() 
#root endpoint
@app.get("/")
async def read_root(): 
    return {"message": "Hello from FastAPI"}

#Using query parameters to greet with name and age
@app.get("/Hello")
async def hello(name: str, age: int):
    return f"Hello {name}, you are {age} years old"

#Using path parameters to greet with name and age
@app.get("/hello/{name}/{age}")
async def hello_age_name(name, age):
    return f"Hello {name}, you are {age} years old"

#Using Pydantic to validate input data to greet with name and age
class PersonInput (BaseModel):
    name: str
    age: int
@app.post("/hello_personclass")
async def hello_personclass(input: PersonInput):
     return f"Hello {input.name}, you are {input.age} years old"

#Get current time in ISO format
@app.get("/time")
async def get_time():
    current_time = datetime.datetime.now().isoformat()
    return {"current_time": current_time}

#Greets a person by name and city
@app.get("/greet")
async def greet(name: str, city: str):
    return { f"Hello {name} from {city}!"}

#Calculate the square of a number
@app.get("/Square")
async def square(number: int):
    return {"number": number, "square": number ** 2}

#Reverse a string
@app.get("/reverse")
async def reverse_string(string: str):
    return {"original": string, "reversed": string[::-1]}

#Get current Status Online or Offline
@app.get("/status")
async def status(is_online: bool):
    if is_online==True:
        return {"status": "Online"}
    else:
        return {"status": "Offline"}

#Get user information by user_id
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    users = {
        1: {"name": "Alice", "age": 30},
        2: {"name": "Bob", "age": 25},
        3: {"name": "Charlie", "age": 35}
    }
    user = users.get(user_id, {"error": "User not found"})
    return user

