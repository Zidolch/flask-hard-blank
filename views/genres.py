from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    Представление для всех жанров
    """
    def get(self):
        """
        Метод для получения всех жанров
        """
        return genre_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    Представление для одного жанра
    """
    def get(self, gid):
        """
        Метод для получения одного жанра
        """
        genre = genre_service.get_one(gid)
        if not genre:
            return "Ошибка", 404
        return genre_schema.dump([genre]), 200
