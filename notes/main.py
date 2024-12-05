from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# What is an API? 
# A web service that provides an interface to applications to manipulate and retrive info
# Rather than writing 5 inventory management services for every app that uses inventory, write one and they can access it via the API.
# A request is sent to the API and the API sends all of that info to the front
# This way you dont need 5 different backends sending the 5 apps inventory info. You have one API that they can all query

# What data does an API exchange?
# JSON: Javascript Object Notation. FastAPI handles jsonifying our info so we can work in python types. FastAPI handles that conversion from JSON to a standard python dictionary for us

# create an app object to initialize our API. Need to do this when starting with FastAPI
app = FastAPI()

# Decorators modify a function without modifying their source code. They're applied in the order that we've called them.

# What is an endpoint?
# The ending path after the main domain
# You go there and something happens

# Before the endpoint, you need to write app dot and then the method that this endpoint is going to accept 

# What is http? 
# Hyper text transfer protocol. Whenever you set up an endpoint you can set it up to be a different method 

# The four core http methods: 
# GET: when you set up a get request or you have an endpoint that has a get method what this means is that this endpoint is going to be returning information
# POST: means that you're going to be sending information to the post endpoint. POST will be creating something new adding something to the database. Maybe posting a new user login or a new user sign up.
# PUT: this is to actually update something that's already existing in the database. Modify information essentially 
# DELETE: getting rid of information

# FastAPI can validate query parameters, path parameters, and headers for all types of requests (GET, POST, PUT, DELETE) using pydantic.
# It automatically validates the data types of the request parameters and body content against the defined models.

# You're going to say @app dot, then the method, then the endpoint
# /: root or your home endpoint
# Make sure the decorator for your endpoint is right above the function that will be triggered when you go to it

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

# Make an endpoint using path and query parameters
# Path parameters: used to identify a specific resource or resource
# Query parameters: used to sort, filter, or represent the current page number in a collection. 
# They are optional parameters that are attached to the end of a URL after a question mark. 
# They are separated by the ampersand (&) symbol if there are multiple parameters.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# {item_id} is a path parameter)
# q ia a query parameter

# Run with uvicorn working:app --reload
# Reloading means when you save a change in python and hit referesh in the browser it reflects that change

# Status codes
# Every time you call an http endpoint it will return to you some status code that indicates what happened. The default is 200 that stands for ok

# # Can optionally add some more status codes in
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     # Return a 400 Bad Request status code if item_id is less than 1
#     if item_id < 1:
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Invalid item_id"})
#     # Default status code 200 OK for valid requests
#     return {"item_id": item_id, "q": q}

# # Define a POST endpoint to create an item with a 201 Created status code
# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# def create_item(item: dict):
#     return {"message": "Item created successfully", "item": item}

# # Define a PUT endpoint to update an item with a 200 OK status code
# @app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
# def update_item(item_id: int, item: dict):
#     return {"message": "Item updated successfully", "item_id": item_id, "item": item}

# # Define a DELETE endpoint to delete an item with a 204 No Content status code
# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_item(item_id: int):
#     return {"message": "Item deleted successfully"}

# # can also add in a request body like this

# What is a Request Body?
# A request body is data sent by the client to your API. This is typically used in POST and PUT requests where the client needs to send data to the server to create or update a resource. In FastAPI, you can easily handle request bodies using Pydantic models.

# from fastapi import FastAPI, status
# from pydantic import BaseModel
# from fastapi.responses import JSONResponse

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the FastAPI application"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     if item_id < 1:
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "Invalid item_id"})
#     return {"item_id": item_id, "q": q}

# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# def create_item(item: Item):
#     return {"message": "Item created successfully", "item": item}

# @app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
# def update_item(item_id: int, item: Item):
#     return {"message": "Item updated successfully", "item_id": item_id, "item": item}

# @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_item(item_id: int):
#     return {"message": "Item deleted successfully"}

# Can use Swagger UI, FastAPI’s built-in interactive documentation, to demo your API endpoints

# GET Method:
# Find the GET /items/{item_id} endpoint
# 2. Try it out
# 3. Enter Parameters: Enter the required path parameter (item_id) and optional query parameter (q)
# Example: item_id = 1, q = "example query"
# 4. Execute

# POST Method:
# 1Find the POST /items/ endpoint
# 2. Try it out
# 3. Enter the JSON payload for the request body
# {
#     "name": "Sample Item",
#     "description": "This is a sample item",
#     "price": 9.99,
#     "tax": 0.5
# }
# 4. Execute

# PUT Method:
# Find the PUT /items/{item_id} endpoint
# 2. Try it out
# 3. Enter Parameters and Request Body: Enter the item_id and the JSON payload for the request body
# Example: item_id = 1
# JSON Payload:
# {
#     "name": "Updated Item",
#     "description": "This is an updated item",
#     "price": 19.99,
#     "tax": 1.0
# }
# 4.Execute

# DELETE Method:
# 1. Find the DELETE /items/{item_id} endpoint
# 2. Try it out
# 3. Enter the item_id
# Example: item_id = 1
# 4. Execute