from django.urls import path

from home_page import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
    path('payment/', views.payment, name='payment'),
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


