import flask
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Представление для всех фильмов
    """
    def get(self):
        """
        Метод для получения всех фильмов
        """
        args = flask.request.args
        if len(args):
            return movie_schema.dump(movie_service.get_by_args(args)), 200
        else:
            return movie_schema.dump(movie_service.get_all()), 200

    def post(self):
        """
        Метод для добавления фильма в базу данных
        """
        req_json = request.json
        if movie_service.create(req_json):
            return "Фильм добавлен", 204
        else:
            return "Ошибка добавления", 500


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Представление для одного фильма
    """
    def get(self, mid):
        """
        Метод для получения одного фильма
        """
        movie = movie_service.get_one(mid)
        if not movie:
            return "Ошибка. Фильм не найден", 404
        return movie_schema.dump([movie]), 200

    def put(self, mid):
        """
        Метод для обновления данных одного фильма
        """
        req_json = request.json
        if movie_service.update(mid, req_json):
            return "Фильм обновлен", 204
        else:
            return "Ошибка обновления", 404

    def delete(self, mid):
        """
        Метод для удаления одного фильма
        """
        if movie_service.delete(mid):
            return "Фильм удален", 204
        else:
            return "Ошибка удаления", 404
