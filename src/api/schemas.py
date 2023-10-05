"""
Pydantic Model definitions
"""
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    username: str


class UserInDB(UserBase):
    password: str


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorReturn(AuthorBase):
    id: int


class Author(AuthorBase):
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str
    page_numbers: int


class BookCreate(BookBase):
    author_id: int

    class Config:
        orm_mode = True
