from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

# What is an API? 
# A web service that provides an interface to applications to manipulate and retrive info
# Rather than writing 5 inventory management services for every app that uses inventory, write one and they can access it via the api.
# A request is sent to the API and the API sends all of that info to the front
# This way you dont need 5 different backends sending th e5 apps inventory info. You have one API that they can all query

# Waht data does an API exchange?
# JSON: Javascript Object Notation. FastAPI handles jsonifying our info so we can work in python types. FastAPI handles that conversion from JSON to a standard python dictionary for us

# create an app object to initialize our API. Need to do this when starting with FastAPI
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# not the best way to have an inventory
# inventory = {
#     1: {
#         "name": "Milk",
#         "price": 3.99,
#         "brand": "Regular"
#     }
# }
# better way
inventory = {}

# Decorators modify a function without modifying their source code. They're applied in the order that we've called them.

# What is an endpoint?
# the ending path after the main domain
# you go there and something happens

# Before the endpoint, you need to write app dot and then the method that this endpoint is going to accept 

# What is http? 
# hyper text transfer protocol. whenever you set up an endpoint you can set it up to be a different method 

# The four core http methods: 
# GET: when you set up a get request or you have an endpoint that has a get method what this means is that this endpoint is going to be returning information
# POST: means that you're going to be sending information to the post endpoint. POST will be creating something new adding something to the database. maybe posting a new user login or a new user sign up.
# PUT: this is to actually update something that's already existing in the database.  modify information essentially 
# DELETE: getting rid of information

# you're going to say @app dot, then the method, then the endpoint
# /: root or your home endpoint
# make sure that your endpoint is right above the function that will be triggered when you go to it

# Path parameters: used to identify a specific resource or resource
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int = Path(description="The ID of the item you'd like to view")):
    return inventory[item_id]

# query parameters: used to sort, filter, or represent the current page number in a collection. 
# They are optional parameters that are attached to the end of a URL after a question mark. 
# They are separated by the ampersand (&) symbol if there are multiple parameters.
# @app.get("/get-by-name")
# def get_item(*, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not found"}

# combine path and query parameters
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    # return {"Data": "Not found"}
# status codes
# every time you call an http endpoint it will return to you some status code that indicates what happened. the default is 200 that stands for ok
    raise HTTPException(status_code=404, detail="Item name not found.")

# Request body
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists."}
        raise HTTPException(status_code=400, detail="Item ID already exists")
    
    # inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price} <- not the best way to insert items
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        # return {"Error": "Item ID does not exist."}
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete ")):
    if item_id not in inventory:
        # return {"Error": "ID does not exist"}
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    
    del inventory[item_id]
    return {"Success": "Item deleted!"}

# run with uvicorn working:app --reload
# reloading means when you save a change in python and hit referesh in the browser it reflects that change