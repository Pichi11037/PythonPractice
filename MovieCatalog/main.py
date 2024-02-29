from domain.Movie import Movie
from service.MovieCatalog import MovieCatalog

count = 0

while count == 0:
    option = int(input(
        '''
Menu:
1) Add Movie
2) List Movies
3) Delete movies
4) Exist
'''
    ))
    if option == 1:
        movieName = input('Movie name: ')
        movie = Movie(movieName)
        MovieCatalog().addMovie(movie)
    elif option == 2:
        MovieCatalog().listMovies()
    elif option == 3:
        MovieCatalog().deleteMovies()
    elif option == 4:
        count = 1