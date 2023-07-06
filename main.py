# if we do not know the particular reponse status then we can import status from fast API.
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

# it is an object of fastAPI class.
app = FastAPI()


class Item(BaseModel):  # serializer
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class config:
        orm_mode = True


db = SessionLocal()

# this end point is used to get all the records.


@app.get('/items', response_model=List, status_code=200)
def get_all_items():
    items = db.query(models.Item).all()

    return items

# this end point is used to get particular records.


@app.get('/item/{item_id}')
def get_an_item(item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

# this end point is used to insert the data in postgres database.


@app.post('/items/post')
def create_an_item(item: Item):
    db_item = db.query(models.Item).filter(
        models.Item.name == item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")
    new_item = models.Item(name=item.name, description=item.description,
                           price=item.price, on_offer=item.on_offer)

    db.add(new_item)
    db.commit()

    return new_item

# this end point is used to upsert the data in postgres database.


@app.put('/item/put/{item_id}')
def update_an_item(item_id: int, item: Item):
    item_to_update = db.query(models.Item).filter(
        models.Item.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.description = item.description
    item_to_update.price = item.price
    item_to_update.on_offer = item.on_offer
    db.commit()
    return item_to_update

# this end point is used to delete the data in postgres database.


@app.delete('/item/delete/{item_id}')
def delete_item(item_id: int):
    item_to_delete = db.query(models.Item).filter(
        models.Item.id == item_id).first()
    if item_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete
