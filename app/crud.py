from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: schemas.MovieCreate, user_id: int):
    db_movie = models.Movie(**movie.dict(), owner_id=user_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie