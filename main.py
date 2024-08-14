import logging
from fastapi import FastAPI
from .routers import users, auth, movies, ratings, comments

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Movie API"}
