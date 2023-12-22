import aiohttp
import asyncio
from uuid import uuid4


url = 'https://python.org'


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(headers={'Request-Id': str(uuid4())}, timeout=timeout) as session:
        async with session.get(url) as response:
            print('Status: ', response.status)
            print('Content-Type: ', response.headers.get('content-type'))
            html = await response.text()
            return f'Body: {html[:15]}...'


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
