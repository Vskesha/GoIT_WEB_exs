import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    separator = "-" * 50
    url = "https://quotes.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    first_paragraph = soup.find("p")
    print(f"First paragraph:\n{first_paragraph}")
    print(separator)

    body_children = list(first_paragraph.children)
    print(f"First paragraph children:\n{body_children}")
    print(separator)

    first_div = soup.find("div")
    first_div_link = first_div.find("a")
    print(f"First div link:\n{first_div_link}")
    print(separator)

    first_paragraph_parent = first_paragraph.parent
    print(f"First paragraph parent:\n{first_paragraph_parent}")
    print(separator)

    container = soup.find("div", attrs={"class": "quote"}).find_parent('div', class_="col-md-8")
    print(f"Container:\n{container}")
    print(separator)

    first_top_tag = soup.find('span', attrs={"class": 'tag-item'})
    print(f"First top tag:\n{first_top_tag}")
    print(separator)

    next_sibling = first_top_tag.find_next_sibling('span')
    print(f"Next sibling:\n{next_sibling}")
    print(separator)

    previous_sibling = next_sibling.find_previous_sibling('span')
    print(f"Previous sibling:\n{previous_sibling}")
    print(previous_sibling == first_top_tag)
    print(separator)
