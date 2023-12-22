import aiohttp
import asyncio


async def main():
    session = aiohttp.ClientSession()
    response = await session.get('https://python.org')
    print('Status: ', response.status)
    print('Content-Type: ', response.headers.get('content-type'))
    html = await response.text()
    response.close()
    await session.close()
    return f'Body: {html[:150]}...'


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)