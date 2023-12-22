import aiohttp
import asyncio

urls = [
    'https://www.google.com',
    'https://www.python.org/asdf',
    'https://duckduckgo.com',
    'http://test'
]


async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(f'Requesting: {url}')
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        print(f'Response from {url}:\n{html[:150]}')
                    else:
                        print(f'Error status: {response.status} for {url}')
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {url}, {str(err)}')

if __name__ == '__main__':
    asyncio.run(main())
