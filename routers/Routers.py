from flask_restful import Resource
from models import DataBaseWrapper, Requset
from utils import organizer, check_atr_length, MusicPlayer, SpotifyWorker, get_spotify_tokens
from flask import request


class BaseResource(Resource):
    """
    Родительский роутер.
    """

    def __init__(self) -> None:
        super().__init__()
        self.db_wrapper = DataBaseWrapper(Requset)


class SpotifyController(BaseResource):
    """

    """

    def __init__(self) -> None:
        super().__init__()
        self.sp = SpotifyWorker(get_spotify_tokens())


class MusicController(BaseResource):
    """
    Данный ресурс служит для работы с MusicPlayer
    """

    def __init__(self) -> None:
        super().__init__()

    def post(self) -> str:
        """
        Post запрос.\n
        Выключает музыку.\n
        Пример данных: {"alarm": "stop"}
        """
        json_data = request.get_json(force=True)

        try:
            check_atr_length(json_data, 1)
        except Exception as e:
            return f"{e}"

        mp = MusicPlayer()
        mp.stop()

        return f"Alarm stoped!"


class BasicRoots(BaseResource):

    def __init__(self) -> None:
        super().__init__()

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
        Пример запроса: {"alarm_time": "2021-05-26 10:11:00.940031", "playlist": "https://google.com"}.\n
        В случае ошибки в запросе возращяет Exception.
        """
        json_data = request.get_json(force=True)

        try:
            check_atr_length(json_data, 2)
        except Exception as e:
            return f"{e}"

        try:
            alarm = json_data["alarm_time"]
            playlist = json_data["playlist"]
        except Exception as e:
            return f"Check your request! Missing {e}"

        self.db_wrapper.insert(alarm_time=alarm, playlist=playlist, is_worked=0, downloaded=0)
        return f"Data added to database!"

    def delete(self) -> str:
        """
        Delete запрос.\n
        Удаляет запись из таблицы по id.\n
        Пример запроса: {"id": 0}.\n
        В случае ошибки в запросе возращяет Exception.
        """
        json_data = request.get_json(force=True)

        try:
            check_atr_lenght(json_data, 1)
        except Exception as e:
            return f"{e}"

        try:
            row_id = json_data["id"]
        except Exception as e:
            return f"Check your request! Missing {e}"

        self.db_wrapper.delete_by_id(int(row_id))
        return f"Data removed from database!"

    def put(self) -> str:
        """
        Put запрос.\n
        Обновляет запись в таблице по id.\n
        Пример запроса: {"id": 0, "alarm_time": "2021-05-26 10:11:00.940031", "playlist": "https://google.com", "is_worked": 0, "downloaded": 0}.\n
        В случае ошибки в запросе возращяет Exception.
        """

        json_data = request.get_json(force=True)

        try:
            check_atr_lenght(json_data, 5)
        except Exception as e:
            return f"{e}"

        try:
            row_id = json_data["id"]
            alarm = json_data["alarm_time"]
            playlist = json_data["playlist"]
            is_worked = json_data["is_worked"]
            downloaded = json_data["downloaded"]
        except Exception as e:
            return f"Check your request! Missing {e}"

        self.db_wrapper.update_by_id(row_id, alarm_time=alarm, playlist=playlist, is_worked=is_worked,
                                     downloaded=downloaded)
        return f"Data updated!"
