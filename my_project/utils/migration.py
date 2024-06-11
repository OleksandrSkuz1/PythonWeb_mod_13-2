import os
import django
from dateutil import parser  # модуль для обробки дати з різними форматами
from pymongo import MongoClient


client = MongoClient("mongodb://localhost")
db = client.hw_10

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
django.setup()

from quotes_by_great_authors.models import Quote, Tag, Author   # noqa

authors = db.authors.find()

for author in authors:
    # Перетворюємо дату з формату "March 14, 1879" у формат, який Django розуміє
    born_date = parser.parse(author['born_date'])

    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=born_date,
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(quote=quote['quote'], author=a)

        for tag in tags:
            q.tags.add(tag)