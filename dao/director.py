from dao.model.director import Director


class DirectorDAO:
    """
    Объект доступа к данным режиссеров
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод для получения всех режиссеров
        """
        return self.session.query(Director).all()

    def get_one(self, did):
        """
        Метод для получения одного режиссеров
        """
        return self.session.query(Director).get(did)
