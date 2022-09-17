from dao.director import DirectorDAO


class DirectorService:
    """
    Сервис для работы с режиссерами
    """
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all(self):
        """
        Метод для получения всех режиссеров
        """
        return self.director_dao.get_all()

    def get_one(self, did):
        """
        Метод для получения одного режиссеров
        """
        return self.director_dao.get_one(did)
