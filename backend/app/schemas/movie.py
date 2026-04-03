from pydantic import BaseModel, ConfigDict
from typing import Optional

class MovieSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    year: Optional[int]
    genres: str
    avg_rating: float
    rating_count: int