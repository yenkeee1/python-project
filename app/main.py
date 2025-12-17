import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.db import SessionLocal
from db.crud import get_categories, get_books_by_category

# Остальной код без изменений...

def main():
    db = SessionLocal()
    
    # Получаем категории
    categories = get_categories(db)
    
    print("=== КАТАЛОГ КНИГ ===\n")
    
    for category in categories:
        print(f"Категория: {category.title}")
        print("-" * 30)
        
        books = get_books_by_category(db, category.id)
        
        if books:
            for book in books:
                print(f"  📖 Название: {book.title}")
                print(f"    Описание: {book.description}")
                print(f"    Цена: {book.price} руб.")
                print(f"    Ссылка: {book.url if book.url else 'нет'}")
                print()
        else:
            print("  В этой категории пока нет книг")
        
        print()
    
    db.close()

if __name__ == "__main__":
    main()