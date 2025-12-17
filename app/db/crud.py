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