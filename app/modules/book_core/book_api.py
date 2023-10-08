from fastapi import APIRouter
from app.models.model import Book
from app.db.database import SessionManager, paginate
from app.modules.book_core import book_schema
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

router = APIRouter(tags=["Books"])

# @router.get('/books/', response_class=book_schema.BookListResponse)
@router.get('/books/')
def get_books():
    with SessionManager() as db:
        res = db.query(Book).filter().all()
        return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)

# @router.get('/books/{uuid}', response_class=book_schema.BookResponse)
@router.get('/books/{uuid}')
def get_book_by_uuid(uuid):
    with SessionManager() as db:
        res = db.query(Book).filter(Book.uuid == uuid).one()
        return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)

# @router.get('/books/{author}', response_class=book_schema.BookListResponse)
@router.get('/books/{author}')
def get_books_by_author(author):
    with SessionManager() as db:
        res = db.query(Book).filter(Book.author == author).all()
        return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)
    
@router.delete('/books/{uuid}')
def delete_books_by_uuid(uuid):
    with SessionManager() as db:
        res = Book.delete_book_by_uuid(uuid)
        return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)

        

@router.post('/books/')
def create_book(data: book_schema.BookCreate):
    res = Book.create_book(title=data.title, author=data.author, publish_date=data.published_date, isbn=data.ISBN)
    return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)


@router.patch("/books/{book_id}", response_model=str)
def partial_update_book(uuid,data: book_schema.BookUpdate):
    res = Book.partial_update_book(uuid=uuid, title=data.title, author=data.author, published_date=data.published_date, ISBN=data.ISBN)
    return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)


@router.put("/books/{book_id}", response_model=str)
def full_update_book(uuid, data: book_schema.BookUpdate):
    res = Book.full_update_book(uuid=uuid, title=data.title, author=data.author, published_date=data.published_date, ISBN=data.ISBN)
    return JSONResponse(content=jsonable_encoder(res), status_code=status.HTTP_200_OK)

