from ComandManager import ComandManager
from ComandManager import AlarmChecker
import socket
import asyncio

class Server(object):
    """
    Функция для работы с сервером
    """

    def __init__(self, ip=''):
        self.ip = ip

    def turnOndemon(self):
        """
        Запускает демона для проверки будильника
        """
        thread = AlarmChecker(daemon=True)
        thread.start()
    
    def cWork(self, c):
        """
        Отпровляет запрос на обработку
        """
        com = ComandManager(c)
        coman = com.commandSelect()
        self.turnOndemon()
        return coman

    def ipSelector(self):
        """
        Выбор ip адреса
        """
        if (self.ip == ''):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            localIp = s.getsockname()[0]
            s.close()
            return localIp
        elif(self.ip == 'localhost' or self.ip == '127.0.0.1'):
            return '127.0.0.1'


    async def handle_echo(self, reader, writer):
        """
        Главный метод сервера, принимает и отпровляет запросы
        """
        data = await reader.read(100)
        message = data.decode("utf-8").split(' ')
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))
        
        print("Send: %r" % self.cWork(message))
        writer.write(bytes(self.cWork(message), encoding='UTF-8'))
        await writer.drain()

        print("Close the client socket")
        writer.close()