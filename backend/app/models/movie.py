from sqlalchemy import Column, Integer, String, Text, Float
from app.db.session import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer)
    genres = Column(Text, nullable=False)
    avg_rating = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)