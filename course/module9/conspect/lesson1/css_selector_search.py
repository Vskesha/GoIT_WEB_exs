import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    separator = "-" * 50
    url = "https://quotes.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    p = soup.select('p')
    print(f"Selector 'p':")
    print(*p, sep='\n')
    print(separator)

    text = soup.select('.text')
    print(f"Selector '.text':")
    print(*text, sep='\n')
    print(separator)

    header = soup.select('#header')
    print(f"Selector '#header':")
    print(*header, sep='\n')
    print(separator)

    a = soup.select("div.container a")
    print(f"Selector 'div.container a':")
    print(*a, sep='\n')
    print(separator)

    href = soup.select("[href^='https://']")
    print(f"Selector '[href^='https://']':")
    print(*href, sep='\n')
    print(separator)

    ctext = soup.select("[class*='text']")
    print(f"Selector '[class*='text']':")
    print(*ctext, sep='\n')
    print(separator)
