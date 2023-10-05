from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from database import SessionLocal, engine
import models
import schemas
import crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_hash_password(password: str):
    return "fakehashed" + password


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def decode_token(token):
    return schemas.User(username="firstuser")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user


@app.get("/me")
async def read_users_me(current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # user_data = crud.get_user(username=form_data.username)
    user_data = {"username": "osama", "hashed_password": "fakehashedLahore22"}

    if not user_data:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = schemas.UserInDB(**user_data)
    hashed_password = fake_hash_password(form_data.password)

    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/")
def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
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
