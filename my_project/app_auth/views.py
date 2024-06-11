from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login

from .forms import RegisterForm

def home(request):
    return render(request, 'quotes_by_great_authors/index.html')


def upload(request):
    # Логіка для завантаження авторів та цитати
    return render(request, 'app_auth/upload.html')

def upload_authors(request):
    # Логіка для завантаження авторів
    return render(request, 'app_auth/upload_authors.html')


def upload_quotes(request):
    # Логіка для завантаження цитат
    return render(request, 'app_auth/upload_quotes.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app_auth:signin')
    else:
        return render(request, 'app_auth/logout.html')  # Додано для GET запитів

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quotes_by_great_authors:root')
    else:
        form = RegisterForm()
    return render(request, 'app_auth/signup.html', {'form': form})

