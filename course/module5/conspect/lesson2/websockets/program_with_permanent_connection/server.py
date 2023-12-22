import asyncio
import websockets
import logging
from websockets.exceptions import ConnectionClosedOK
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connected')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.discard(ws)
        logging.info(f'{ws.remote_address} disconnected')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

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
            await self.send_to_clients(message)


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 4000):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
