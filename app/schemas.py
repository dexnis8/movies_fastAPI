from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    movie_id: int
    user_id: int

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    score: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int
    movie_id: int
    user_id: int

    class Config:
        orm_mode = True

# Add the Token schema here
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None