from pymongo import MongoClient
from fastapi import APIRouter, Path, Response, responses,status
from models.item import Item
from typing import List
from fastapi.encoders import jsonable_encoder


router = APIRouter()
def get_connection():
    myclient = MongoClient(host='mongodb',port=27017)    
    mydb = myclient["inventory"]
    return mydb["items"]
@router.get("/GetAllItems")
async def get_items(response: Response):
    items_collection= get_connection()
    output =[]
    for x in items_collection.find({}, {"_id":0}):
        output.append(x)
    if not output:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"Error": "No items in the inventory."}
    return output

@router.get("/GetItemById/{item_id}")
async def get_item_by_id(item_id: str, response: Response):
    items_collection= get_connection()
    item = items_collection.find_one({"id": item_id}, {"_id":0})
    if item:
        return jsonable_encoder(item)
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"Error":"Item not found"}

@router.post("/AddItem")
async def add_item(item: Item, response: Response):
    items_collection= get_connection()
    if items_collection.find_one({"id": item.id}, {"_id":0}):
        response.status_code= status.HTTP_409_CONFLICT
        return {"Error": "Item with that ID already exist"}  
    items_collection.insert_one(jsonable_encoder(item))
    return {"Message": "Added Item"}

@router.delete("/DeleteItems")
async def delete_items(response: Response):
    items_collection= get_connection()
    result = items_collection.delete_many({})
    if result.deleted_count ==0:
        response.status_code= status.HTTP_400_BAD_REQUEST
        return {"Error": "No items in the inventory."}
    return {"Message": "Items deleted successfully!"}

@router.delete("/DeleteItem/{item_id}")
async def delete_item(item_id: str, response: Response):
    items_collection= get_connection()
    result = items_collection.delete_one({"id":item_id})
    if result.deleted_count==0:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {"Error":"Item not found"}
    return {"Message": "Item removed successfully"}  
