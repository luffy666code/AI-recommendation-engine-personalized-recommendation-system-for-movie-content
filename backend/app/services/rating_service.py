from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingResponse, UserRatingsResponse
from datetime import datetime

def add_or_update_rating(db: Session, rating_data: RatingCreate) -> RatingResponse:
    # 检查是否已有评分
    existing_rating = db.query(Rating).filter(
        and_(Rating.user_id == rating_data.user_id, Rating.movie_id == rating_data.movie_id)
    ).first()

    if existing_rating:
        # 更新评分
        existing_rating.rating = rating_data.rating
        existing_rating.timestamp = datetime.utcnow()
        db.commit()
        db.refresh(existing_rating)
        return RatingResponse.model_validate(existing_rating)

    # 新增评分
    new_rating = Rating(
        user_id=rating_data.user_id,
        movie_id=rating_data.movie_id,
        rating=rating_data.rating,
        timestamp=datetime.utcnow()
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return RatingResponse.model_validate(new_rating)

def get_user_ratings(db: Session, user_id: int) -> UserRatingsResponse:
    ratings = db.query(Rating).filter(Rating.user_id == user_id).all()
    rating_responses = [RatingResponse.model_validate(r) for r in ratings]
    return UserRatingsResponse(user_id=user_id, ratings=rating_responses)