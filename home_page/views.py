from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Главная'
        context['content'] = 'Магазин мебели HOME'
        return context


# def index(request):
#
#     context = {
#         'title': 'Home - Главная',
#         'content': 'Магазин мебели HOME',
#     }
#
#     return render(request, 'home/index.html', context)


class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Text on page'
        return context

# def about(request):
#
#     context = {
#         'title': 'Home - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Text on page'
#     }
#
#     return render(request,'home/about.html', context)


class InfoView(TemplateView):
    template_name = 'home/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Контактная инофрмация'
        context['content'] = 'Контактная информация'
        context['text_on_page'] = 'Информация'
        return context


# def info(request):
#
#     context = {
#         'title': 'Home - Контактная инофрмация',
#         'content': 'Контактная информация',
#         'text_on_page': 'Информация',
#     }
#
#     return render(request, 'home/info.html', context)


class PaymentView(TemplateView):
    template_name = 'home/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Доставка и оплата'
        context['content'] = 'Доставка и оплата'
        context['text_on_page'] = 'Доставка и оплата'
        return context


# def payment(request):
#
#     context = {
#         'title': 'Home - Доставка и оплата',
#         'content': 'Доставка и оплата',
#         'text_on_page': 'Доставка и оплата',
#     }
#
#     return render(request, 'home/info.html', context)
