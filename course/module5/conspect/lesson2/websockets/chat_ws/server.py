import asyncio
import websockets
import logging
import names
from websockets.exceptions import ConnectionClosedOK
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)


class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.name}:{ws.remote_address} connected')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.discard(ws)
        logging.info(f'{ws.name}:{ws.remote_address} disconnected')

    async def send_to_clients(self, message: str):
        for client in self.clients:
            await client.send(message)
            logging.info(f'Message: {message} was sent to {client.name}:{client.remote_address}')

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distribute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            await self.send_to_clients(f'{ws.name}: {message}')


async def main():
    server = Server('localhost', 8080)
    async with websockets.serve(server.ws_handler, server.host, server.port):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
