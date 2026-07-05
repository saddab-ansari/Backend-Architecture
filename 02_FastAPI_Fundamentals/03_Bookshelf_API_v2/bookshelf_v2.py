from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel , Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    description : str
    rating : int
    published_year : int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_year : int) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year

class BookRequest(BaseModel):
    id: Optional[int] = Field( description= 'ID is not needed on create', default=None) 
    title : str = Field(min_length=3)
    author : str =  Field(min_length=3)
    description : str =  Field(min_length=4)
    rating : int = Field (gt=-1 , lt=6)
    published_year : int = Field(gt=1000, lt=2026)

    model_config = {
        "json_schema_extra" : {
            "example" : {
                'title' : 'New Book',
                'author' : 'Author Name',
                'description' : 'It is a good Book!',
                'rating' : 5,
                'published_year' : 2020
            }
        }
    }
    

def find_book_id(book : Book) -> Book:
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book



BOOKS = [
    Book(1, "Atomic Habits", "James Clear", "Build better habits", 5, 2018),
    Book(2, "The Alchemist", "Paulo Coelho", "Follow your dreams", 5, 1988),
    Book(3, "Deep Work", "Cal Newport", "Master focused productivity", 4, 2016),
    Book(4, "The Pragmatic Programmer", "Andrew Hunt & David Thomas", "Essential programming wisdom", 5, 1999),
    Book(5, "Clean Code", "Robert C. Martin", "Write cleaner code", 5, 2008),
    Book(6, "The Psychology of Money", "Morgan Housel", "Smart money lessons", 5, 2020)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def find_by_id(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Book not found')

@app.get("/books/")
async def get_by_rating(filter_rating : int = Query(gt=0, lt= 6)):
    books_by_rating = []
    for book in BOOKS:
        if book.rating >= filter_rating:
            books_by_rating.append(book)
    return books_by_rating

@app.get("/books/year/")
async def get_by_published_year(year : int):
    books_by_year = []
    for book in BOOKS:
        if book.published_year == year:
            books_by_year.append(book)
    if len(books_by_year) > 0: 
        return books_by_year
    else:
        raise HTTPException(status_code=404, detail='Book not found')

@app.post("/books/create-book", status_code= status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return {'message' : 'Book was added Successfully.'}

@app.put("/books/update_book", status_code=status.HTTP_200_OK)
async def update_book(update_request : BookRequest):
    book_changed = False
    updated_book = Book(**update_request.model_dump())
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == updated_book.title.casefold():
            updated_book.id = BOOKS[i].id
            BOOKS[i] = updated_book
            book_changed = True
            return {'message' : 'Book was successfully updated'}
    if not book_changed:    
        raise HTTPException(status_code=404, detail='Book not found')

@app.delete("/books/delete/", status_code=status.HTTP_200_OK)
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].title.casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {'message' : 'Book deleted successfully'}
    raise HTTPException(status_code=404, detail='Book not found')
