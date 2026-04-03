from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class RatingCreate(BaseModel):
    user_id: int = Field(..., gt=0)
    movie_id: int = Field(..., gt=0)
    rating: float = Field(..., ge=0.5, le=5.0)

class RatingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    movie_id: int
    rating: float
    timestamp: Optional[datetime]

class UserRatingsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    ratings: list[RatingResponse]