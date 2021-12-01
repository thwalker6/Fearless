from fastapi import FastAPI, APIRouter, Path, Response, responses,status
from itemsAPI.models.item import Item
from typing import List

router = APIRouter()
inventory: List[Item]=[]

@router.get("/GetAllItems")
async def get_items(response: Response):
    if not inventory:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"Error": "No items in the inventory."}
    return inventory

@router.get("/GetItemById/{item_id}")
async def get_item_by_id(item_id: str, response: Response):
    for item in inventory:
        if item_id == item.id:
            return {"Message": "Item succesffuly found"}
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"Error":"Item not found"}

@router.post("/AddItem")
async def add_item(item: Item, response: Response):
    for it in inventory:
        if item.id == it.id:
            response.status_code= status.HTTP_409_CONFLICT
            return {"Error": "Item with that ID already exist"}
    inventory.append(item)
    return item

@router.delete("/DeleteItems")
async def delete_items(response: Response):
    if not inventory:
        response.status_code= status.HTTP_400_BAD_REQUEST
        return {"Error": "No items in the inventory."}
    inventory.clear()
    return {"Message": "Items deleted successfully!"}

@router.delete("/DeleteItem/{item_id}")
async def delete_item(item_id: str, response: Response):
    for item in inventory:
        if item_id == item.id:
            inventory.remove(item)
            return {"Message": "Item removed successfully"}
    response.status_code=status.HTTP_400_BAD_REQUEST
    return {"Error":"Item not found"}
