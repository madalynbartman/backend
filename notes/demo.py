from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

# Square Brackets []: Used to access elements in lists, tuples, and dictionaries by their index or key.
# Curly Braces {}: Used to define dictionaries and sets.
# We are are using square brackets [] to access values within the inventory dictionary by their keys.

# If we don't specify custom status codes in our FastAPI endpoints, we will still see the default status codes in the API. FastAPI will automatically use appropriate status codes based on the type of request and the outcome of the request. 
# However, without specifying custom status codes, we won't be able to customize the message or the status code itself.

# Run with uvicorn working:app --reload

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

# Using an in memory dictionary as a data store
inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int, name: str = None):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID not found.")
    if name and inventory[item_id].name != name:
        raise HTTPException(status_code=404, detail="Item name not found.")
    
    return inventory[item_id]

# Request body
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    # Adds the item from the item inventory, our data store
    inventory[item_id] = item

    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    # This ensures that any update operation is only performed on items that actually exist in the inventory.
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    # Checks if name is provided, it updates the name field of the inventory item with the new name. And so on..
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    # Deletes the item from the item inventory dictionary, our data store
    del inventory[item_id]
    
    return {"Success": "Item deleted!"}