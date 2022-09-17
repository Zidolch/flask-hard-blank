from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Представление для всех режиссеров
    """
    def get(self):
        """
        Метод для получения всех режиссеров
        """
        return director_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    Представление для одного режиссера
    """
    def get(self, did):
        """
        Метод для получения одного режиссера
        """
        director = director_service.get_one(did)
        if not director:
            return "Ошибка", 404
        return director_schema.dump([director]), 200
