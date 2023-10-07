from pydantic import BaseModel

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