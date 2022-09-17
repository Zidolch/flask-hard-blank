from dao.model.genre import Genre


class GenreDAO:
    """
    Объект доступа к данным жанров
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод для получения всех жанров
        """
        return self.session.query(Genre).all()

    def get_one(self, gid):
        """
        Метод для получения одного жанра
        """
        return self.session.query(Genre).get(gid)
