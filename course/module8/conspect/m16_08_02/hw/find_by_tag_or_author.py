from colorama import init as init_colorama, Fore, Style
import redis
from redis_lru import RedisLRU

from models import Author, Quote

client = redis.Redis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

init_colorama()


@cache
def find_by_tag(tag: str) -> list[str | None]:
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


@cache
def find_by_author(author: str) -> dict:
    authors = Author.objects(fullname__iregex=author)
    result = {author.fullname: q.quote for author in authors for q in Quote.objects(author=author)}
    return result


def main():
    while True:
        inp = input(
            f"Enter part of tag or author (for example "
            f"{Fore.BLUE}tag:<tag>{Style.RESET_ALL} or "
            f"{Fore.BLUE}author:<author>{Style.RESET_ALL})\n>>> "
        )
        args = inp.split(":", 1)
        if len(args) == 1:
            print(f"{Fore.RED}Values must be separated with colon ':'{Style.RESET_ALL}")

        elif args[0] == "tag":
            tag = args[1]
            result = find_by_tag(tag)
            if result:
                print(f"{Fore.YELLOW}Found by tag: {tag}{Style.RESET_ALL}")
                [print(q) for q in result]
            else:
                print(f"{Fore.YELLOW}Nothing found by tag: {tag}{Style.RESET_ALL}")

        elif args[0] == "author":
            author = args[1]
            result = find_by_author(author)
            if result:
                print(f"{Fore.YELLOW}Found by author: {author}{Style.RESET_ALL}")
                [print(f'{Fore.GREEN}{a}: {Style.RESET_ALL}{q}') for a, q in result.items()]
            else:
                print(f"{Fore.YELLOW}Nothing found by author: {author}{Style.RESET_ALL}")

        else:
            print(
                f"{Fore.RED}Only 'tag' or 'author' are supported before colon{Style.RESET_ALL}"
            )
        print("-" * 50, "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.GREEN}Exiting the program...{Style.RESET_ALL}")
