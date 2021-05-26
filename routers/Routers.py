from flask_restful import Resource
from models import DataBaseWrapper, Requset
from utils import organizer

class BasicRoots(Resource):
    """
    Базовый роутер (ресурс)
    """
    def get(self):
        """
        Get запрос.\n
        Выводит все доступные запросы(будильники).
        """
        db_wrapper = DataBaseWrapper(Requset)
        return organizer(db_wrapper.select_all())
    
    def post(self):
        """
        Post запрос.\n
        Добовляет запрос(будильник).
        """
        pass
        # TODO доделать пост запрос

    