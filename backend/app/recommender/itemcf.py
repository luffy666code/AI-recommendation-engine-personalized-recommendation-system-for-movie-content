import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_itemcf_recommendations(movie_id: int, top_n: int, ratings_df: pd.DataFrame, movies_df: pd.DataFrame):
    """基于物品的协同过滤推荐：返回与指定电影最相似的 top_n 电影"""
    if movie_id not in ratings_df['movieId'].unique():
        return []

    # 构建用户-电影评分矩阵
    user_movie = ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    if movie_id not in user_movie.columns:
        return []

    # 计算电影间余弦相似度矩阵
    item_matrix = user_movie.T  # 行：电影，列：用户
    similarity_matrix = cosine_similarity(item_matrix)

    movie_index = list(item_matrix.index).index(movie_id)
    similarity_scores = similarity_matrix[movie_index]

    sim_df = pd.DataFrame({
        'movie_id': item_matrix.index,
        'similarity': similarity_scores
    })

    # 排除自己
    sim_df = sim_df[sim_df['movie_id'] != movie_id]

    # 取 top_n
    top_sim = sim_df.sort_values(by='similarity', ascending=False).head(top_n)

    top_movies = movies_df[movies_df['id'].isin(top_sim['movie_id'])][['id', 'title']]

    result = []
    for _, row in top_sim.iterrows():
        movie_info = top_movies[top_movies['id'] == row['movie_id']]
        title = movie_info['title'].iloc[0] if not movie_info.empty else ''
        result.append({
            'movie_id': int(row['movie_id']),
            'title': title,
            'similarity': float(row['similarity'])
        })

    return result


def get_user_itemcf_recommendations(user_id: int, top_n: int, ratings_df: pd.DataFrame, movies_df: pd.DataFrame, min_rating: float = 4.0):
    """基于用户历史高评分电影，汇总 ItemCF 相似电影作为推荐结果"""
    user_ratings = ratings_df[ratings_df['userId'] == user_id]
    if user_ratings.empty:
        return []

    high_rated = user_ratings[user_ratings['rating'] >= min_rating]
    if high_rated.empty:
        return []

    user_movie = ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    item_matrix = user_movie.T
    similarity_matrix = cosine_similarity(item_matrix)

    item_index = list(item_matrix.index)
    similarity_df = pd.DataFrame(similarity_matrix, index=item_index, columns=item_index)

    candidate_scores = {}
    watched_movie_ids = set(user_ratings['movieId'])

    for _, row in high_rated.iterrows():
        mid = row['movieId']
        score_weight = row['rating']

        if mid not in similarity_df.index:
            continue

        similarities = similarity_df.loc[mid]
        for candidate_movie_id, similarity in similarities.items():
            if candidate_movie_id in watched_movie_ids or candidate_movie_id == mid:
                continue
            candidate_scores.setdefault(candidate_movie_id, 0.0)
            candidate_scores[candidate_movie_id] += similarity * score_weight

    if not candidate_scores:
        return []

    candidate_df = pd.DataFrame(
        list(candidate_scores.items()),
        columns=['movie_id', 'score']
    )
    candidate_df = candidate_df.sort_values(by='score', ascending=False).head(top_n)

    movies_map = movies_df.set_index('id')['title'].to_dict()

    result = []
    for _, row in candidate_df.iterrows():
        result.append({
            'movie_id': int(row['movie_id']),
            'title': movies_map.get(row['movie_id'], ''),
            'score': float(row['score'])
        })

    return result