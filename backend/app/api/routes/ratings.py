from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingResponse, UserRatingsResponse
from app.services.rating_service import add_or_update_rating, get_user_ratings

router = APIRouter(prefix="/api/ratings", tags=["ratings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("")
def create_or_update_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    try:
        result = add_or_update_rating(db, rating)
        return {
            "code": 200,
            "message": "success",
            "data": {
                "user_id": result.user_id,
                "movie_id": result.movie_id,
                "rating": result.rating
            }
        }
    except Exception as e:
        db.rollback()
        return {
            "code": 500,
            "message": f"error: {str(e)}",
            "data": None
        }

@router.get("/user/{user_id}")
def get_user_ratings_endpoint(user_id: int, db: Session = Depends(get_db)):
    try:
        result = get_user_ratings(db, user_id)
        # 强制将datetime转为ISO字符串，避免FastAPI默认序列化问题
        history = [
            {
                "user_id": r.user_id,
                "movie_id": r.movie_id,
                "rating": r.rating,
                "timestamp": r.timestamp.isoformat() if r.timestamp else None
            }
            for r in db.query(Rating).filter(Rating.user_id == user_id).all()
        ]
        return {
            "code": 200,
            "message": "success",
            "data": {
                "user_id": user_id,
                "ratings": history
            }
        }
    except Exception as e:
        return {
            "code": 500,
            "message": f"error: {str(e)}",
            "data": None
        }

@router.get("/test")
def test_ratings(db: Session = Depends(get_db)):
    ratings = db.query(Rating).order_by(Rating.id).limit(10).all()
    rating_list = [
        {
            "id": r.id,
            "user_id": r.user_id,
            "movie_id": r.movie_id,
            "rating": r.rating,
            "timestamp": r.timestamp.isoformat() if r.timestamp else None,
        }
        for r in ratings
    ]
    return {"code": 200, "message": "success", "data": {"list": rating_list}}