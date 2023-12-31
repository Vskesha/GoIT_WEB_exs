import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    separator = '-' * 50
    url = "https://quotes.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    first_paragraph = soup.find("p")
    print(f"First paragraph:\n{first_paragraph}")
    print(separator)

    all_paragraphs = soup.find_all("p")
    print("All paragraphs:")
    print(*all_paragraphs, sep='\n')
    print(separator)

    first_paragraph_text = first_paragraph.get_text()
    print(f"First paragraph text:\n{first_paragraph_text.encode('utf-8')}")
    print(separator)

    first_link = soup.find("a")
    first_link_href = first_link.get("href")
    print(f"First link:\n{first_link_href}")
    print(separator)

