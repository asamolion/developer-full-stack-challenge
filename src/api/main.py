"""
main FastAPI application
"""
from typing import Annotated

from fastapi import (
    FastAPI,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql.operators import ilike_op

from database import SessionLocal, engine
from auth import (
    oauth2_scheme,
    get_current_user,
    login_user,
)

import crud
import models
import schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/me")
async def read_users_me(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
) -> schemas.UserOut:
    return await get_current_user(db, token)


@app.post("/token")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    return login_user(db=db, username=form_data.username, password=form_data.password)


@app.get("/")
def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Homepage
    """
    return {"Hello": "World"}


@app.get("/authors")
def list_authors(
    skip: int,
    limit: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
    search: str | None = "",
):
    """
    Authors page
    """
    result = (
        db.query(models.Author.id, models.Author.name, func.count(models.Book.id).label("book_count"))
        .join(models.Book, isouter=True)
        .group_by(models.Author.id)
        .order_by(models.Author.id.asc())
        .filter(models.Author.name.ilike("%{}%".format(search)))
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result


@app.post("/authors")
def add_author(
    author: schemas.AuthorIn,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
):
    return crud.create_author(db, author)


@app.get("/books")
def list_books(
    skip: int,
    limit: int,
    search: str,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
):
    """
    Books page
    """
    result = (
        db.query(models.Book.id, models.Book.name, models.Book.page_numbers, models.Author.name.label("author_name"))
        .join(models.Author)
        .filter(models.Book.name.ilike("%{}%".format(search)))
        .offset(skip)
        .limit(limit)
        .all()
    )

    return result


@app.post("/books")
def add_book(
    book: schemas.BookIn,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
):
    return crud.create_book(db, book=book)
