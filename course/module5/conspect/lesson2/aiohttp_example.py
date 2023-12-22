import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.python.org') as response:
            print('Status: ', response.status)
            print('Content-Type: ', response.headers.get('content-type'))
            html = await response.text()
            print('Body: ', html[:15], '...')


if __name__ == '__main__':
    asyncio.run(main())
