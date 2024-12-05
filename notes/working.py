from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

#not the best way to have an inventory
# inventory = {
#     1: {
#         "name": "Milk",
#         "price": 3.99,
#         "brand": "Regular"
#     }
# }
#better way
inventory = {}


# Path parameters
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int = Path(description="The ID of the item you'd like to view")):
    return inventory[item_id]

#query parameters
# @app.get("/get-by-name")
# def get_item(*, name: Optional[str] = None, test: int):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data": "Not found"}

#combine path and query parameters
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    # return {"Data": "Not found"}
#status codes
    raise HTTPException(status_code=404, detail="Item name not found.")

#Request body
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists."}
        raise HTTPException(status_code=400, detail="Item ID already exists")
    
    #inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price} <- not the best way to insert items
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
