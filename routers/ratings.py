from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models, auth
from ..database import get_db

router = APIRouter()

@router.post("/movies/{movie_id}/ratings/", response_model=schemas.Rating)
def create_rating(movie_id: int, rating: schemas.RatingCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_rating(db=db, rating=rating, movie_id=movie_id, user_id=current_user.id)

@router.get("/movies/{movie_id}/ratings/", response_model=List[schemas.Rating])
def read_ratings(movie_id: int, db: Session = Depends(get_db)):
    ratings = crud.get_ratings(db, movie_id=movie_id)
    return ratings
