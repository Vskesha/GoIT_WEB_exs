import asyncio
import random
from time import sleep


async def random_value():
    print('Start task')
    await asyncio.sleep(1)
    print('Task finished')
    return random.random()


async def main():
    task = asyncio.create_task(random_value())
    sleep(2)
    print('Task shceduled')
    await task
    print(f'result: {task.result()}')


if __name__ == '__main__':
    asyncio.run(main())
