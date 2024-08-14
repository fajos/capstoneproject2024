from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    movies: List['Movie'] = []

    class Config:
        from_attributes = True

class MovieBase(BaseModel):
    title: str
    description: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    owner_id: int
    ratings: List['Rating'] = []
    comments: List['Comment'] = []

    class Config:
        from_attributes = True

class RatingBase(BaseModel):
    rating: float

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    movie_id: int
    user_id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    parent_id: Optional[int] = None

class Comment(CommentBase):
    id: int
    movie_id: int
    user_id: int
    parent_id: Optional[int] = None
    replies: List['Comment'] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None