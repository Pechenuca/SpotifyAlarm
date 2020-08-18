import asyncio
from Server import Server

sv = Server('localhost')

sv.turnOndemon()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(sv.handle_echo, sv.ipSelector(), 5005, loop=loop)
server = loop.run_until_complete(coro)


print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()



