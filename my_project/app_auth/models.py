from django.shortcuts import render


def home(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()
    context = {
        'authors': authors,
        'quotes': quotes,
    }
    return render(request, 'app_auth/home.html', context)
