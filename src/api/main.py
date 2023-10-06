"""
main FastAPI application
"""
from typing import Annotated

from fastapi import (
    FastAPI,
    Depends,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from auth import (
    oauth2_scheme,
    get_current_user,
    login_user,
)

import models
import schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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
def render_authors_page():
    """
    Authors page
    """
    return {"Authors": "Page"}


@app.get("/books")
def render_books_page():
    """
    Books page
    """
    return {"Books": "Page"}
