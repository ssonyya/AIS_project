import sqlalchemy
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from application.models import dao
from typing import Optional


"""
    Модуль инициализации "Соя Хранения Данных" приложения (Persistence Layer, Repository Layer)
"""


def get_engine(db_url: str, db_sync: str = 'false') -> Optional[Engine]:
    """ Функция создает движок для управления подключениями к БД """
    sqla_engine = sqlalchemy.create_engine(url=db_url)
    # если в конфигурации приложения указан флаг синхронизации БД,
    # то пытаемся сгененрировать таблицы при запуске приложения
    if db_sync == 'true':
        dao.Base.metadata.create_all(bind=sqla_engine)
    return sqla_engine


def get_session_fabric(engine: Engine):
    """ Функция создает фабрику подключений (сессий) к БД """
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
