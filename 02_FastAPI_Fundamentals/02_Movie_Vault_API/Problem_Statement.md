# Problem Statement: Movie Vault API

## Objective

The developer is required to build a REST API using FastAPI that manages a personal 
movie collection. This project serves as an independent practice build to consolidate 
CRUD operations, parameter handling, and float-based filtering without instructor guidance.

## Requirements

### Data Structure

Each movie entry must contain four fields: `title`, `director`, `genre`, and `rating` 
(float, 0.0 to 10.0). The collection must be pre-populated with at least 5 real movies.

### Endpoints

| Method | Path | Behaviour |
|--------|------|-----------|
| GET | `/movies` | Return all movies |
| GET | `/movies/{movie_title}` | Return a single movie by title, or a not-found message |
| GET | `/movies/genre/{genre}` | Filter movies by genre |
| GET | `/movies/search/` | Filter by director via query parameter |
| GET | `/movies/top-rated/` | Return movies at or above a minimum rating via query parameter |
| POST | `/movies/create` | Add a new movie via request body |
| PUT | `/movies/update` | Update an existing movie by title via request body |
| DELETE | `/movies/delete/{movie_title}` | Delete a movie by title |

## Constraints

- All string comparisons must be case-insensitive using `casefold()`
- Every endpoint must return a meaningful message when the requested resource is not found
- No database — in-memory storage only
