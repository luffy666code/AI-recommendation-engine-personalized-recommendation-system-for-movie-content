import pandas as pd
from sqlalchemy.orm import Session
from app.models.rating import Rating
from app.models.movie import Movie
from app.recommender.itemcf import get_itemcf_recommendations, get_user_itemcf_recommendations


def item_based_recommendation(db: Session, movie_id: int, top_n: int = 10):
    # 从数据库读取 rating 和 movie 数据
    ratings = db.query(Rating).all()
    movies = db.query(Movie).all()

    if not ratings:
        return {'movie_id': movie_id, 'title': '', 'recommendations': []}

    ratings_df = pd.DataFrame([{
        'userId': r.user_id,
        'movieId': r.movie_id,
        'rating': r.rating,
        'timestamp': r.timestamp
    } for r in ratings])

    movies_df = pd.DataFrame([{
        'id': m.id,
        'title': m.title
    } for m in movies])

    target_movie = movies_df[movies_df['id'] == movie_id]
    if target_movie.empty:
        return {'movie_id': movie_id, 'title': '', 'recommendations': []}

    recommendations = get_itemcf_recommendations(movie_id, top_n, ratings_df, movies_df)

    return {
        'movie_id': movie_id,
        'title': target_movie['title'].iloc[0],
        'recommendations': recommendations
    }


def user_based_recommendation(db: Session, user_id: int, top_n: int = 10):
    ratings = db.query(Rating).all()
    movies = db.query(Movie).all()

    if not ratings:
        return {'user_id': user_id, 'recommendations': []}

    ratings_df = pd.DataFrame([{
        'userId': r.user_id,
        'movieId': r.movie_id,
        'rating': r.rating,
        'timestamp': r.timestamp
    } for r in ratings])

    movies_df = pd.DataFrame([{
        'id': m.id,
        'title': m.title
    } for m in movies])

    recommendations = get_user_itemcf_recommendations(user_id, top_n, ratings_df, movies_df)

    return {
        'user_id': user_id,
        'recommendations': recommendations
    }