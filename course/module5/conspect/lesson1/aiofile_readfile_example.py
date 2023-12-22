from aiofile import async_open
import asyncio


async def await_afp_read():
    async with async_open('hello.txt', 'r') as afp:
        res = await afp.read()
        print(res)


async def async_for_read():
    async with async_open('hello.txt', 'r') as afp:
        async for line in afp:
            print(line)


if __name__ == '__main__':
    asyncio.run(await_afp_read())
    asyncio.run(async_for_read())
