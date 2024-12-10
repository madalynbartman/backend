from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

# API: interface that allows us to programatically interface withan application
# Web API: an API that uses Hyptertext Transfer Protocol (HTTP) to transport data

# HTTP: A communication protocol that allows us to exchange different media types over a network
# GET: Returns info about the requested resource
# POST: Creates a new resource
# PUT: Performs a full update by replacing a resource
# DELETE: Removes a resource

# Microservices communicate with each other using APIs 
# The API documentation tells us how to interact with the microservice 

# API documentation: A description of the API 
# Following a standard interface description language such as Open API for REST APIs

# Documentation Driven Development:
# 1. Design and document the API
# 2. Build the API client and the API server following the documentation
# 3. Test both the API client and the API server against the documentation

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message: " "Welcome to the FastAPI app!"}

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

# In-memory data store
inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int, name: Optional[str] = None):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID not found.")
    if name and inventory[item_id].name != name:
        raise HTTPException(status_code=404, detail="Item name not found.")
    
    return inventory[item_id]


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    inventory[item_id] = item

    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.description != None:
        inventory[item_id].description = item.description

    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    # Deletes the item from the item inventory dictionary, our data store
    del inventory[item_id]
    
    return {"Success": "Item deleted!"}

# Starlette: asynchronous server gateway interface (ASGI) web framework
# It runs services as a collection of asynchronous tasks to gain performance in apps
# uvicorn is an asynchronous web server commonly used to run starlette apps
# It handles HTTP requests and passes them to Starlette
# FastAPI is built on top of Starlette 
# It enhances Starlettes routes with data validation (pydantic) & API documentation (Swagger)

# Run with uvicorn file:app --reload
# Hot reloading restarts your server whenever you make changes to your file

# Swagger UI is a data visualization tool for APIs
# Using Swagger UI, we can easily test if our implementation is correct
