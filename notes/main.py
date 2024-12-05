from fastapi import FastAPI

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
