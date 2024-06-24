from django.urls import path, include
from rest_framework import routers
from . import views
# from django.conf.urls import url

app_name = 'restapi'


router = routers.DefaultRouter()
router.register(r'carts', views.CartViewSet, basename='carts')
router.register(r'product', views.ProductViewSet, basename='products')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'users', views.UserViewSet, basename='users')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     url(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'),
#     url(r'^subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),
# ]