from flask_restful import Resource
from models import DataBaseWrapper, Requset
from utils import organizer
from flask import request, jsonify

class BasicRoots(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.db_wrapper = DataBaseWrapper(Requset)

    """
    Базовый роутер (ресурс)
    """
    def get(self) -> list:
        """
        Get запрос.\n
        Выводит все доступные запросы(будильники).
        """
        return organizer(self.db_wrapper.select_all())
    
    def post(self) -> str:
        """
        Post запрос.\n
        Добовляет запрос(будильник).\n
        Пример запроса: {"alarm_time": "2021-05-26 10:11:00.940031", "playlist": "https://google.com", "is_worked": 0}.\n
        В случае ошибки в запросе возращяет Exception.
        """
        json_data = request.get_json(force=True)
        
        try:
            alarm = json_data["alarm_time"]
            playlist = json_data["playlist"]
            is_worked = json_data["is_worked"]
        except Exception as e:
            return f"Check your request! Missing {e}"

        self.db_wrapper.insert(alarm_time=alarm, playlist=playlist, is_worked=is_worked)
        return f"Data added to database!"
    
    def delete(self) -> str:
        """
        Delete запрос.\n
        Удаляет запись из таблицы по id.
        Пример запроса: {"id": 0}.\n
        В случае ошибки в запросе возращяет Exception.
        """
        json_data = request.get_json(force=True)

        try:
            row_id = json_data["id"]
        except Exception as e:
            return f"Check your request! Missing {e}"
        
        self.db_wrapper.delete_by_id(int(row_id))
        return f"Data removed from database!"
        
        


    