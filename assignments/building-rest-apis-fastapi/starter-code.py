from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment API")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


items = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}


# TODO: Add a GET /items endpoint to return all items


# TODO: Add a POST /items endpoint to create and save a new item


# TODO: Add a GET /items/{item_id} endpoint to return one item
