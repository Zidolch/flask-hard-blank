from dao.genre import GenreDAO


class GenreService:
    """
    Сервис для работы с жанрами
    """
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self):
        """
        Метод для получения всех жанров
        """
        return self.genre_dao.get_all()

    def get_one(self, gid):
        """
        Метод для получения одного жанра
        """
        return self.genre_dao.get_one(gid)
