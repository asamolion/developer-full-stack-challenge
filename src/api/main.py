from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Author:
    pass


class Book:
    pass


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/login")
def login():
    return {"Login": "Page"}


@app.get("/authors")
def get_authors():
    return {"Authors": "Page"}


@app.get("/books")
def get_books():
    return {"Books": "Page"}
