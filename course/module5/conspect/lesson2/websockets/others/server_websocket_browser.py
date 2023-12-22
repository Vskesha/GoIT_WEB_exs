import asyncio
import websockets


async def handler(websocket, path):
    data = await websocket.recv()
    reply = f'Data reseived as: {data}'
    print(reply)
    await websocket.send(reply)


async def main():
    async with websockets.serve(handler, 'localhost', 8000):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())
