from ComandManager import ComandManager
from ComandManager import AlarmChecker
import socket
import asyncio

def turnOndemon():
    thread = AlarmChecker(daemon=True)
    thread.start()

turnOndemon()

def cWork(c):
    com = ComandManager(c)
    coman = com.commandSelect()
    turnOndemon()
    return coman

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode("utf-8").split(' ')
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))
    
    print("Send: %r" % message)
    writer.write(bytes(cWork(message), encoding='UTF-8'))
    await writer.drain()

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, socket.gethostbyname(socket.gethostname()), 5005, loop=loop)
server = loop.run_until_complete(coro)


print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()



