class Error(Exception):
    """
    Базовый класс всех Exception.
    """
    pass

class DictTooManyAtrs(Error):
    """
    Вызывается когда передано больше аргументов чем нужно.
    """
    def __init__(self, message="Length of atrs more than needed"):
        self.message = message
        super().__init__(self.message)
