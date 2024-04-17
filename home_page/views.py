from django.views.generic import ListView
from django.http import HttpResponse
from .models import Author, Genre, BookModel
from django.shortcuts import render


class HomeListView(ListView):
    template_name = 'home/index.html'
    model = Author


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request,'home/index.html', context)


def about(request):
    return HttpResponse('About page')

