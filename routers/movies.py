from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models, auth
from ..database import get_db

router = APIRouter()

@router.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_movie(db=db, movie=movie, user_id=current_user.id)

@router.get("/movies/", response_model=List[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.put("/movies/{movie_id}", response_model=schemas.Movie)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_movie = crud.update_movie(db=db, movie_id=movie_id, movie=movie, user_id=current_user.id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found or not authorized to update")
    return db_movie

@router.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_movie = crud.delete_movie(db=db, movie_id=movie_id, user_id=current_user.id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found or not authorized to delete")
    return db_movie