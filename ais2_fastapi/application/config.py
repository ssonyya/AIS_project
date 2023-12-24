from configparser import RawConfigParser, ExtendedInterpolation
from .repository import get_engine, get_session_fabric

"""
    Данный модуль отвечает за конфигурирование приложения
"""


# Читаем файл конфигурации приложения (в результате будет получен dict-подобный объект)
app_config = RawConfigParser(interpolation=ExtendedInterpolation())

app_config.read('application.ini')

db_config = app_config['Database']      # получаем значения раздела "Database"

# Инициализируем драйвер соединения с БД используя параметры конфигурации 'database_url' (строка подключения к БД)
# и 'database_sync' - флаг автоматической генерации таблиц БД при запуске приложения
engine = get_engine(db_url=db_config['database_url'], db_sync=db_config['database_sync'])

SessionLocal = get_session_fabric(engine)
