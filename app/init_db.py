import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.db import engine
from db import models
from db.crud import create_category, create_book
from db.db import SessionLocal

# Остальной код без изменений...

def init_db():
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    category1 = create_category(db, title="Художественная литература")
    category2 = create_category(db, title="Научная фантастика")
    
    create_book(db, title="Мастер и Маргарита", description="Роман Михаила Булгакова", price=450.0, url="", category_id=category1.id)
    create_book(db, title="Преступление и наказание", description="Роман Фёдора Достоевского", price=380.0, url="", category_id=category1.id)
    create_book(db, title="Дюна", description="Фантастический роман Фрэнка Герберта", price=670.0, url="", category_id=category2.id)
    create_book(db, title="Основание", description="Цикл романов Айзека Азимова", price=590.0, url="", category_id=category2.id)
    
    print("База данных инициализирована, добавлены категории и книги.")
    db.close()

if __name__ == "__main__":
    init_db()