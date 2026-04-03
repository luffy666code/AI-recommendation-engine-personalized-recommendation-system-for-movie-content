from fastapi import FastAPI
from app.api.routes.movies import router as movies_router
from app.api.routes.ratings import router as ratings_router
from app.api.routes.recommend import router as recommend_router
from app.api.routes.stats import router as stats_router

app = FastAPI()
app.include_router(movies_router)
app.include_router(ratings_router)
app.include_router(recommend_router)
app.include_router(stats_router)

@app.get("/")
def read_root():
    return {"message": "Movie Recommendation System API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}