from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud, models
from app.schemas import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[Book])
def get_books(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    db: Session = Depends(get_db)
):
    if category_id:
        books = crud.get_books_by_category(db, category_id, skip=skip, limit=limit)
    else:
        books = crud.get_books(db, skip=skip, limit=limit)
    return books

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Проверка существования категории
    category = crud.get_category_by_id(db, book.category_id)
    if category is None:
        raise HTTPException(status_code=400, detail="Category does not exist")
    return crud.create_book(
        db, 
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Проверка существования категории
    category = crud.get_category_by_id(db, book.category_id)
    if category is None:
        raise HTTPException(status_code=400, detail="Category does not exist")
    
    return crud.update_book(
        db, 
        book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return None