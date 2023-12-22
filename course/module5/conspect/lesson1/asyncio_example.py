import asyncio


async def baz() -> str:
    print('Before sleep')
    await asyncio.sleep(2)
    print('After sleep')
    return 'Hello world!'


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
