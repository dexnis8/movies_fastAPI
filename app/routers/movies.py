# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import crud, schemas, models
# from app.dependencies import get_db, get_current_user
# from typing import List

# router = APIRouter()

# @router.post("/movies/", response_model=schemas.Movie)
# def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     return crud.create_movie(db=db, movie=movie, user_id=current_user.id)

# @router.get("/movies/", response_model=List[schemas.Movie])
# def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     movies = crud.get_movies(db, skip=skip, limit=limit)
#     return movies


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("movies/create", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_movie(db=db, movie=movie, user_id=current_user.id)

@router.get("movies/all", response_model=List[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies