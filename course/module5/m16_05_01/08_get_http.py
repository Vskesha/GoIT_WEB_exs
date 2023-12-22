import requests
from requests.exceptions import InvalidSchema, MissingSchema, SSLError
import asyncio
from concurrent.futures import ThreadPoolExecutor

from timing import async_timed, sync_timed


urls = [
    "https://github.com",
    "https://www.codewars.com",
    "https://rezka.cc/",
    "https://hltv.org/",
    "https://app.amplitude.com/",
    "https://www.youtube.com/",
    "https://tabletki.ua",
    "asdf",
    "ws://test.com",
    "https://stackoverflow.com/",
]


def get_preview(url: str) -> tuple[str, str]:
    res = requests.get(url)
    return url, res.text[:25]


@sync_timed()
def main_sync():
    results = []
    for url in urls:
        try:
            results.append(get_preview(url))
        except (SSLError, InvalidSchema, MissingSchema) as err:
            print(err)

    return results


@async_timed()
async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = [loop.run_in_executor(pool, get_preview, url) for url in urls]
        results = await asyncio.gather(*futures, return_exceptions=True)

    return results


if __name__ == "__main__":
    print(main_sync())
    r = [el for el in asyncio.run(main()) if not (isinstance(el, Exception) and isinstance(el, IOError))]
    print(r)
