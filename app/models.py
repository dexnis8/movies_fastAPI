
# ### `app/models.py`

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

# class Movie(Base):
#     __tablename__ = "movies"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="movies")

# class Comment(Base):
#     __tablename__ = "comments"
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String, index=True)
#     movie_id = Column(Integer, ForeignKey("movies.id"))
#     user_id = Column(Integer, ForeignKey("users.id"))

# class Rating(Base):
#     __tablename__ = "ratings"
#     id = Column(Integer, primary_key=True, index=True)
#     score = Column(Integer)
#     movie_id = Column(Integer, ForeignKey("movies.id"))
#     user_id = Column(Integer, ForeignKey("users.id"))



from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    movies = relationship("Movie", back_populates="owner")

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="movies")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))