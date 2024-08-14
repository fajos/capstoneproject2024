from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models, auth
from ..database import get_db

router = APIRouter()

@router.post("/movies/{movie_id}/comments/", response_model=schemas.Comment)
def create_comment(movie_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_comment(db=db, comment=comment, movie_id=movie_id, user_id=current_user.id)

@router.get("/movies/{movie_id}/comments/", response_model=List[schemas.Comment])
def read_comments(movie_id: int, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, movie_id=movie_id)
    return comments
