from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import SessionLocal
from app.models.movie import Movie
from app.models.rating import Rating

router = APIRouter(prefix="/api/stats", tags=["stats"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/overview")
def get_stats_overview(db: Session = Depends(get_db)):
    movie_count = db.query(Movie).count()
    rating_count = db.query(Rating).count()
    avg_rating = db.query(func.avg(Rating.rating)).scalar() or 0.0

    top_movies_query = (
        db.query(Movie)
        .order_by(Movie.rating_count.desc())
        .limit(10)
        .all()
    )
    top_movies = [
        {
            "id": m.id,
            "title": m.title,
            "year": m.year,
            "genres": m.genres,
            "avg_rating": m.avg_rating,
            "rating_count": m.rating_count,
        }
        for m in top_movies_query
    ]

    return {
        "code": 200,
        "message": "success",
        "data": {
            "movie_count": movie_count,
            "rating_count": rating_count,
            "avg_rating": float(round(avg_rating, 3)),
            "top_movies": top_movies,
        },
    }