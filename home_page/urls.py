from django.urls import path

from home_page import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('info/', views.InfoView.as_view(), name='info'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
]


# from django.urls import path, register_converter
#
# from .views import HomeListView
# from .converters import ULIDConverter
#
#
# register_converter(converter=ULIDConverter, type_name='ulid')
#
# urlpatterns = [
#     path('', HomeListView.as_view(), name='home_index'),
#     #path('<ulid:post_ulid>/', )
# ]


