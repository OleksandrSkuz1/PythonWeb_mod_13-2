from django.urls import path, include

from . import views

app_name = 'quotes_by_great_authors'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>/', views.main, name='root_paginate')
]


