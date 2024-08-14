import logging
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = logging.getLogger(__name__)

def get_user(db: Session, username: str):
    logger.info(f"Getting user {username}")
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    logger.info(f"Creating user {user.username}")
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User {db_user} created successfully")
    return db_user

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    logger.info(f"Getting movies with skip={skip} and limit={limit}")
    return db.query(models.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    logger.info(f"Getting movie {movie_id}")
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate, user_id: int):
    logger.info(f"Creating movie by user {user_id}")
    db_movie = models.Movie(**movie.model_dump(), owner_id=user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    logger.info(f"Movie  created successfully by user {user_id}")
    return db_movie

def update_movie(db: Session, movie_id: int, movie: schemas.MovieCreate, user_id: int):
    logger.info(f"Updating movie {movie_id} by user {user_id}")
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id, models.Movie.owner_id == user_id).first()
    if db_movie:
        for key, value in movie.model_dump().items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
    logger.info(f"Movie updated successfully by user {user_id} ")
    return db_movie

def delete_movie(db: Session, movie_id: int, user_id: int):
    logger.info(f"Deleting movie {movie_id} by user {user_id}")
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id, models.Movie.owner_id == user_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    logger.info(f"Movie deleted successfully by user {user_id} ")
    return db_movie

def create_rating(db: Session, rating: schemas.RatingCreate, movie_id: int, user_id: int):
    logger.info(f"Creating rating for movie {movie_id} by user {user_id}")
    db_rating = models.Rating(**rating.model_dump(), movie_id=movie_id, user_id=user_id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    logger.info(f"Rating created successfully for movie {movie_id} by user {user_id}")
    return db_rating

def get_ratings(db: Session, movie_id: int):
    logger.info(f"Getting ratings for movie {movie_id}")
    return db.query(models.Rating).filter(models.Rating.movie_id == movie_id).all()

def create_comment(db: Session, comment: schemas.CommentCreate, movie_id: int, user_id: int):
    logger.info(f"Creating comment for movie {movie_id} by user {user_id}")
    db_comment = models.Comment(**comment.model_dump(), movie_id=movie_id, user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    logger.info(f"Comment created successfully for movie {movie_id} by user {user_id}")
    return db_comment

def get_comments(db: Session, movie_id: int):
    logger.info(f"Getting comments for movie {movie_id}")
    return db.query(models.Comment).filter(models.Comment.movie_id == movie_id).all()