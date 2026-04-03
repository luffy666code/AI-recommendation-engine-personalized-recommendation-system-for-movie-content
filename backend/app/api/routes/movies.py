from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.movie import Movie

router = APIRouter(prefix="/api/movies", tags=["movies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).order_by(Movie.id).limit(10).all()
    movie_list = [
        {
            "id": m.id,
            "title": m.title,
            "year": m.year,
            "genres": m.genres,
            "avg_rating": m.avg_rating,
            "rating_count": m.rating_count,
        }
        for m in movies
    ]
    return {"code": 200, "message": "success", "data": {"list": movie_list}}