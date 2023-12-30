from models import Author, Quote
from mongoengine.errors import NotUniqueError

import json


if __name__ == "__main__":
    with open("authors.json", "r", encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(
                    fullname=el.get("fullname"),
                    born_date=el.get("born_date"),
                    born_location=el.get("born_location"),
                    description=el.get("description"),
                )
                author.save()
            except NotUniqueError:
                print(f'Author "{el.get("fullname")}" already exists')

    with open("quotes.json", "r", encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            author = Author.objects(fullname=el.get("author")).first()
            quote = Quote(
                author=author,
                tags=el.get("tags"),
                quote=el.get("quote"),
            )
            quote.save()
