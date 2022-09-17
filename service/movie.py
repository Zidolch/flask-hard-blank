from dao.movie import MovieDAO


class MovieService:
    """
    Сервис для работы с фильмами
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self):
        """
        Метод для получения всех фильмов
        """
        return self.movie_dao.get_all()

    def get_one(self, mid):
        """
        Метод для получения одного фильма
        """
        return self.movie_dao.get_one(mid)

    def create(self, data):
        """
        Метод для добавления фильма в базу данных
        """
        return self.movie_dao.create(**data)

    def update(self, mid, data):
        """
        Метод для обновления информации о фильме
        """
        return self.movie_dao.update(mid, **data)

    def get_by_args(self, args):
        """
        Метод для получения всех фильмов по выбранным параметрам
        """
        return self.movie_dao.get_by_args(**args)

    def delete(self, mid):
        """
        Метод для удаления фильма из базы данных
        """
        return self.movie_dao.delete(mid)
