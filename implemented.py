from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

# Создание DAO и сервиса фильмов
movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

# Создание DAO и сервиса режиссеров
director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

# Создание DAO и сервиса жанров
genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)