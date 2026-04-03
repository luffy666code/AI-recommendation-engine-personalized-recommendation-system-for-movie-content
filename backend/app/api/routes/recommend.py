from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.recommendation_service import item_based_recommendation

router = APIRouter(prefix='/api/recommend', tags=['recommend'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/item-based/{movie_id}')
def item_based(movie_id: int, top_n: int = 10, db: Session = Depends(get_db)):
    result = item_based_recommendation(db, movie_id, top_n)
    if not result:
        raise HTTPException(status_code=404, detail='movie not found')
    return {
        'code': 200,
        'message': 'success',
        'data': result
    }

@router.get('/user/{user_id}')
def user_based(user_id: int, top_n: int = 10, db: Session = Depends(get_db)):
    from app.services.recommendation_service import user_based_recommendation

    result = user_based_recommendation(db, user_id, top_n)
    return {
        'code': 200,
        'message': 'success',
        'data': result
    }