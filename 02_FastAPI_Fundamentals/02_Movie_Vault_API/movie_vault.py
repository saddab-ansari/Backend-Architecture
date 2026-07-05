from fastapi import Body, FastAPI
app = FastAPI()

MOVIES = [
    {'title' : 'The Social Network', 'director' : 'David Fincher', 'genre' : 'Psychological Drama', 'rating' : 7.8},
    {'title' : 'The Pursuit of Happyness', 'director' : 'Gabriele Muccino', 'genre' : 'Psychological Drama', 'rating' : 8.0},
    {'title' : 'Catch Me If You Can', 'director' : 'Steven Spielberg', 'genre' : 'Adventure', 'rating' : 8.1},
    {'title' : 'The Wolf of Wall Street', 'director' : 'Martin Scorsese', 'genre' : 'Dark Comedy', 'rating' : 8.2},
    {'title' : 'Fight Club', 'director' : 'David Fincher', 'genre' : 'Psychological Drama', 'rating' : 8.8}
]

@app.get("/movies")
async def all_movies():
    return MOVIES

@app.get("/movies/{movie_title}")
async def my_movie(movie_title : str):
    for movie in MOVIES:
        if movie.get('title').casefold() == movie_title.casefold():
            return movie
    return {'message' : 'Movie was not found.'}
    
        
@app.get("/movies/genre/{genre}")
async def filter_by_genre(genre : str):
    movies_in_genre = []
    for movie in MOVIES:
        if movie.get('genre').casefold() == genre.casefold():
            movies_in_genre.append(movie)
    if len(movies_in_genre) > 0:
        return movies_in_genre
    else:
        return {'message' : 'No movie in this genre was found'}

@app.get("/movies/search/")
async def search_by_query(director : str):
    movies_by_director = []
    for movie in MOVIES:
        if movie.get('director').casefold() == director.casefold():
            movies_by_director.append(movie)

    if len(movies_by_director) > 0:
        return movies_by_director
    else:
        return {'message' : 'No movie by this director was found'}
    
@app.get("/movies/top-rated/")
async def top_rated(rating : float):
    movies_by_rating_query = []
    for movie in MOVIES:
        if movie.get('rating') >= rating:
            movies_by_rating_query.append(movie)
    
    if len(movies_by_rating_query) > 0:
        return movies_by_rating_query
    else:
        return {'message' : 'No movie above a the rating was found'}
    
@app.post("/movies/create")
async def add_a_movie(create = Body()):
    MOVIES.append(create)
    return {"message" : "New movie was added successfully."}

@app.put("/movies/update")
async def update_a_movie(updated_movie = Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == updated_movie.get('title').casefold():
            MOVIES[i] = updated_movie
            return {'message' : 'The movie was update successfully.'}
        
@app.delete("/movies/delete/{movie_title}")
async def delete_a_movie(movie_title: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == movie_title.casefold():
            MOVIES.pop(i)
            return {'message': 'The movie was successfully deleted.'}
    return {'message': 'Movie was not found.'}
