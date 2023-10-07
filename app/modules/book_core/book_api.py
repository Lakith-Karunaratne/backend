from fastapi import APIRouter
from app.models.model import Book
from app.db.database import SessionManager, paginate
from app.modules.book_core import book_schema

router = APIRouter(tags=["Books"])


# TODO GET BOOKS
@router.get('/books/')
def get_books():
    with SessionManager() as db:
        res = db.query(Book).filter().all()
        return res

@router.get('/books/{uuid}')
def get_book_by_uuid(uuid):
    with SessionManager() as db:
        res = db.query(Book).filter(Book.uuid == uuid).one()
        return res

@router.get('/books/{author}')
def get_books_by_author(author):
    with SessionManager() as db:
        res = db.query(Book).filter(Book.author == author).all()
        return res
    
@router.delete('/books/{uuid}')
def delete_books_by_uuid(uuid):
    with SessionManager() as db:
        return Book.delete_book_by_uuid(uuid)

@router.post('/books/')
def create_book(data: book_schema.BookCreate):
    return Book.create_book(title=data.title, author=data.author, publish_date=data.published_date, isbn=data.ISBN)
    

@router.patch("/books/{book_id}", response_model=str)
def partial_update_book(uuid,data: book_schema.BookUpdate):
    return Book.partial_update_book(uuid=uuid, title=data.title, author=data.author, published_date=data.published_date, ISBN=data.ISBN)


@router.put("/books/{book_id}", response_model=str)
def full_update_book(uuid, data: book_schema.BookUpdate):
    return Book.full_update_book(uuid=uuid, title=data.title, author=data.author, published_date=data.published_date, ISBN=data.ISBN)

