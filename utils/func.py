from datetime import datetime
from .Exceptions import *

def is_date_actual(dataBaseDatetime: datetime) -> bool:
    """
    Функция для проверки времяни.
    """
    return dataBaseDatetime > datetime.now()

def organizer(query: str) -> list:
    """
    Функция подготавливает данные из таблицы.
    """
    data = []
    for row in query.dicts():
        strDict = {}
        for key in row:
            strDict[key] = str(row[key])
        data.append(strDict)
    return data

def check_atr_lenght(data: dict, count: int) -> DictTooManyAtrs:
    """
    Функция проверяет колличество поданных аргументов.
    """
    if (len(data.keys()) != count):
        raise DictTooManyAtrs()