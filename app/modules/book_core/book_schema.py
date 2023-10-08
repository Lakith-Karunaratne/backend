from pydantic import BaseModel
from typing import List


class BookCreate(BaseModel):
    title: str
    author: str
    published_date: str = None
    ISBN: str = None

class BookUpdate(BaseModel):
    title: str = None
    author: str = None
    published_date: str = None
    ISBN: str = None

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    pub_date: str = None 
    isbn: str = None
    cover_image: str = None

    class Config:
        orm_mode = True


class BookListResponse(BaseModel):
    books : List[BookResponse]