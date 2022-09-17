class Config:
    """
    Конфигурация приложения
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lesson_18.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
