import socket

class Connector(object):

    def __init__(self, address, port):
        self.address = str(address)
        self.port = int(port)

    def sendCommand(self, command, sbuffer):
        address_to_server = (self.address, self.port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address_to_server)
        s.send(bytes(command, encoding='UTF-8'))
        data = s.recv(int(sbuffer))
        s.close()
        return data