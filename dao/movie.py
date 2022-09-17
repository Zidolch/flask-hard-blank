from dao.model.movie import Movie


class MovieDAO:
    """
    Объект доступа к данным фильмов
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Метод для получения всех фильмов
        """
        return self.session.query(Movie).all()

    def get_one(self, mid):
        """
        Метод для получения одного фильма
        """
        return self.session.query(Movie).get(mid)

    def get_by_args(self, **args):
        """
        Метод для получения всех фильмов по выбранным параметрам
        """
        return self.session.query(Movie).filter_by(**args).all()

    def create(self, **data):
        """
        Метод для добавления фильма в базу данных
        """
        try:
            movie = Movie(**data)
            self.session.add(movie)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def update(self, mid, **data):
        """
        Метод для обновления информации о фильме
        """
        try:
            self.session.query(Movie).filter(Movie.id == mid).update(data)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def delete(self, mid):
        """
        Метод для удаления фильма из базы данных
        """
        try:
            movie = self.get_one(mid)
            self.session.delete(movie)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
