from peewee import *

database = SqliteDatabase('database.sqlite')


class BaseModel(Model):
    """
    Базовая модель.
    """

    class Meta:
        database = database


class Requset(BaseModel):
    """
    Основная модель в базе данных.\n
    Хранит в себе:\n
        дату когда должен сработать будильник.\n
        ссылку на плей-лист.\n
        сработал ли запрос.\n
        скачен ли плейлист.\n
    """
    alarm_time = DateTimeField()
    playlist = CharField()
    is_worked = BooleanField()
    downloaded = BooleanField()
