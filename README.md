# Movie Listing API

This is a movie listing API built with FastAPI. The API allows users to list movies, view listed movies, rate them, and add comments. The application is secured using JWT (JSON Web Tokens).

## Features

- User Authentication
  - User registration
  - User login
  - JWT token generation
- Movie Listing
  - View a movie added (public access)
  - Add a movie (authenticated access)
  - View all movies (public access)
  - Edit a movie (only by the user who listed it)
  - Delete a movie (only by the user who listed it)
- Movie Rating
  - Rate a movie (authenticated access)
  - Get ratings for a movie (public access)
- Comments
  - Add a comment to a movie (authenticated access)
  - View comments for a movie (public access)
  - Add comment to a comment i.e., nested comments (authenticated access)

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn app.main:app --reload`

## Deployment

Deploy the application on a cloud server of your choice.
