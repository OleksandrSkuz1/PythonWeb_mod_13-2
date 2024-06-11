from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    context = {
        'quotes': quotes_on_page,
        'page_number': page,
    }
    return render(request, 'quotes_by_great_authors/index.html', context)

