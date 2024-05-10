from django.views.generic import ListView
from django.http import HttpResponse
from .models import Author, Genre, BookModel
from django.shortcuts import render

from goods.models import Categories


class HomeListView(ListView):
    template_name = 'home/index.html'
    model = Author


def index(request):


    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'home/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Text on page'
    }

    return render(request,'home/about.html', context)

