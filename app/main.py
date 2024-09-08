from fastapi import FastAPI
from app.routers import movies, users, comments, ratings
from app.database import engine
from app import models

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(comments.router)
app.include_router(ratings.router)