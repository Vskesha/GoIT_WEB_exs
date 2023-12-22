import aiohttp
import asyncio
from time import perf_counter


url = 'https://python.org'


async def index_with_session(session):
    async with session.get(url) as response:
        print('Status: ', response.status)
        print('Content-Type: ', response.headers.get('content-type'))
        html = await response.text()
        return f'Body: {html[:15]}...'


async def index_without_session():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Status: ', response.status)
            print('Content-Type: ', response.headers.get('content-type'))
            html = await response.text()
            return f'Body: {html[:15]}...'


async def doc_with_session(session):
    async with session.get(url) as response:
        print('Status: ', response.status)
        print('Content-Type: ', response.headers.get('content-type'))
        html = await response.text()
        return f'Body: {html[:15]}...'


async def doc_without_session():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Status: ', response.status)
            print('Content-Type: ', response.headers.get('content-type'))
            html = await response.text()
            return f'Body: {html[:15]}...'


async def with_session():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(index_with_session(session), doc_with_session(session))
        return result


async def without_session():
    result = await asyncio.gather(index_without_session(), doc_without_session())
    return result


if __name__ == '__main__':
    start = perf_counter()
    r = asyncio.run(with_session())
    print(f'Result: {r}\nTime: {perf_counter() - start}')

    start = perf_counter()
    r = asyncio.run(without_session())
    print(f'Result: {r}\nTime: {perf_counter() - start}')
