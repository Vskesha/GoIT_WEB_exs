import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') as response:
            print('Status: ', response.status)
            print('Content-Type: ', response.headers.get('content-type'))
            print('Cookie: ', response.cookies)
            print(response.ok)
            result = await response.json()
            return result


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
