import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async(url):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        results = await asyncio.gather(*futures, return_exceptions=True)
        return results


if __name__ == '__main__':
    start = time()
    result = asyncio.run(preview_fetch_async(urls))
    for r in result:
        print(r)
    print(f'Total time: {time() - start}')
