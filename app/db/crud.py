from sqlalchemy.orm import Session
from . import models

# CRUD для Category
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

# CRUD для Book
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = models.Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Book).filter(models.Book.category_id == category_id).offset(skip).limit(limit).all()

# CRUD для Category
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

# CRUD для Book
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = models.Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Book).filter(models.Book.category_id == category_id).offset(skip).limit(limit).all()
# CRUD для Category
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

# CRUD для Book
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = models.Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Book).filter(models.Book.category_id == category_id).offset(skip).limit(limit).all()
# CRUD для Category
def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

# CRUD для Book
def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = models.Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Book).filter(models.Book.category_id == category_id).offset(skip).limit(limit).all()
    # Дополнительные функции для работы с API
def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_category(db: Session, category_id: int, title: str):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category

def update_book(db: Session, book_id: int, title: str, description: str, price: float, url: str, category_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.title = title
        db_book.description = description
        db_book.price = price
        db_book.url = url
        db_book.category_id = category_id
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False