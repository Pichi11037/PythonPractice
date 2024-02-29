from domain.Movie import Movie
import os

class MovieCatalog:

    filePath = 'movies.txt'
    
    def __enter__(self):
        print('Opening file'.center(30, '-'))
        self._file_path = open(self._file_path, "w+", encoding='utf8')
        return self._file_path
    
    def __exit__(self):
        print('Closing file'.center(30, '-'))
        if self._file_path:
            self._file_path.close()

    @classmethod
    def addMovie(cls, movie:Movie):
        with open(cls.filePath, 'a', encoding='utf8') as f:
            f.write(f'{movie.name}\n')

    @classmethod
    def listMovies(cls):
        with open(cls.filePath, 'r', encoding='utf8') as f:
            for ln in f.readlines():
                print(ln)

    @classmethod
    def deleteMovies(cls):
        os.remove(cls._file_path)
        print('File Deleted'.center(30, '-'))