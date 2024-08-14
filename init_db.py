from .database import engine, Base
from .models import User, Movie, Rating, Comment

def init_db():
    Base.metadata.create_all(bind=engine)