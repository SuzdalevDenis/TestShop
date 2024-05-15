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


def info(request):

    context = {
        'title': 'Home - Контактная инофрмация',
        'content': 'Контактная информация',
        'text_on_page': 'Информация',
    }

    return render(request,'home/info.html', context)


def payment(request):

    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'Доставка и оплата',
    }

    return render(request,'home/info.html', context)
