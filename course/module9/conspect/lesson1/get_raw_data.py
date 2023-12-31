import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)

    quotes = soup.find_all("span", class_="text")
    # [print(quote.text) for quote in quotes]

    authors = soup.find_all("small", class_="author")
    # [print(author.text) for author in authors]

    tags = soup.find_all("div", class_="tags")
    # print(*tags, sep='\n\n')

    for i, t in enumerate(tags):
        print(quotes[i].text)
        print("--" + authors[i].text)
        tags_for_quote = t.find_all("a", class_="tag")
        [print(tag.text) for tag in tags_for_quote]
        print("-" * 50)
