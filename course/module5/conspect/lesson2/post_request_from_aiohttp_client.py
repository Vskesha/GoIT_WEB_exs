import aiohttp
import asyncio
from uuid import uuid4

URL = 'http://localhost:5000'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(URL, data={'message': 'Hello World!'}, ssl=False) as response:
            print('Status:', response.status)
            html = await response.text()
            return f'Body: {html}'


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
