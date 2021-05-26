from . import database

class DataBaseAssistant():
    """
    Класс для работы с 'физическим' вооплощением базы данных
    """
    def __init__(self) -> None:
        self.database = database

    def create_tables(self, tables: list) -> None:
        """
        Создает базу данных с указыанми таблицами
        """
        with self.database:
            self.database.create_tables(tables)
    
    #TODO Нужно добавить функцию для удаления файла sqlite3