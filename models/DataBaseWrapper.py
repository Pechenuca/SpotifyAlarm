from peewee import *


class DataBaseWrapper():
    """
    Класс обертка вокруг peewee.
    """

    def __init__(self, model: Model) -> None:
        """
        Входной аргумент класс модели с которым мы будем работать.
        """
        self.model = model

    def insert(self, **data: str) -> None:
        """
        Добавление стоки в таблицу.
        """
        self.model.insert(data).execute()

    def select_all(self) -> None:
        """
        Выборка всех данных из таблицы.
        """
        return (self.model
                .select()
                )

    def delete_by_id(self, id: int) -> None:
        """
        Удаление строки из таблицы по id (первичный ключ).
        """
        self.model.delete().where(self.model.id == id).execute()

    def update_by_id(self, id: int, **data: str) -> None:
        """
        Обновление строки в таблице по id (первичный ключ).
        """
        (self.model
         .update(**data)
         .where(self.model.id == id)
         .execute()
         )
