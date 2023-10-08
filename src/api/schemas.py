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


class UserOut(UserBase):
    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorPatch(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str
    page_numbers: int


class BookIn(BookBase):
    author_id: int

    class Config:
        orm_mode = True


class BookOut(BookBase):
    class Config:
        orm_mode = True


class BookWithAuthorName(BookBase):
    author_name: str

    class Config:
        orm_mode = True
