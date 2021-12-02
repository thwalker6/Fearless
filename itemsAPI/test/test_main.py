
from unittest import mock
from fastapi import status
from fastapi.testclient import TestClient
from starlette import responses
from api.app import app
import mongomock
from fastapi.encoders import jsonable_encoder

from unittest.mock import patch
client = TestClient(app)
item = {
    "id":"1",
    "name":"thing"
}
c ={'id':"1", 'name':"thing2"}
d ={'id':"97", 'name':"thing2"}
mockdb = mongomock.MongoClient().db.collection
mockdb.insert_one(item)
empty_db = mongomock.MongoClient().db.empty

def test_get_items_fail(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=empty_db) 
    response = client.get("items/GetAllItems")
    assert response.status_code==status.HTTP_404_NOT_FOUND

def test_get_item_by_id_fail(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=empty_db) 
    response = client.get("/GetItemById/0")
    assert response.status_code==status.HTTP_404_NOT_FOUND

def test_add_item(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=mockdb) 
    response = client.post("items/AddItem",json=d)
    assert response.status_code==status.HTTP_200_OK

def test_add_item_fail(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=mockdb) 
    response = client.post("items/AddItem",json=c)
    assert response.status_code==status.HTTP_409_CONFLICT

def test_delete_item_fail(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=empty_db) 
    response = client.delete("items/DeleteItem/1")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_delete_item_success(mocker):
    mocker.patch('api.routes.item_router.get_connection', return_value=mockdb) 
    response = client.delete("items/DeleteItem/1")
    assert response.status_code == status.HTTP_200_OK