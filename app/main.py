from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.db import engine
from app.db import models
from app.api import categories, books

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    print("Database tables created")
    yield
    print("Shutting down")

app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и категориями",
    version="1.0.0",
    lifespan=lifespan
)

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Bookstore API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}