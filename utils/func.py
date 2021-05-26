from datetime import datetime

def is_date_actual(dataBaseDatetime):
    """
    Функция для проверки времяни.
    """
    return dataBaseDatetime > datetime.now()

def organizer(query):
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
