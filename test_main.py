from fastapi import status
from fastapi.testclient import TestClient
from itemsAPI.api.app import app 

client = TestClient(app)

item = {
    "id":"1",
    "name":"thing"
}

def test_get_items_fail():
    response = client.get("items/GetAllItems")
    assert response.status_code==status.HTTP_404_NOT_FOUND
def test_get_item_by_id_fail():
    response = client.get("items/GetItemById/1")
    assert response.status_code==status.HTTP_404_NOT_FOUND
def test_add_item():
    response = client.post("items/AddItem",json=item)
    assert response.status_code==status.HTTP_200_OK

def test_get_items():
    response = client.get("items/GetAllItems")
    assert response.status_code==status.HTTP_200_OK
def test_get_item_by_id_success():
    response = client.get("items/GetItemById/1")
    assert response.status_code==status.HTTP_200_OK
def test_remove_item_fail():
    response = client.delete("items/DeleteItem/2")
    assert response.status_code==status.HTTP_400_BAD_REQUEST
def test_remove_item():
    response = client.delete("items/DeleteItem/1")
    assert response.status_code==status.HTTP_200_OK