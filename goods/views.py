from django.http import Http404
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView
from rest_framework.response import Response


from goods.models import Products, Categories
from goods.utils import q_search
# from goods.serializers import ProductSerializer, CategorySerializer

from rest_framework import viewsets, mixins, generics


class CatalogView(ListView):
    model = Products
    # queryset = Products.objects.all().order_by('-id')
    template_name = 'goods/catalog.html'
    context_object_name = 'goods'
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        query = self.request.GET.get('q')

        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)


        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Каталог'
        context['slug_url'] = self.kwargs.get('category_slug')
        # context['categories'] = Categories.objects.all()
        return context


# def catalog(request, category_slug=None):
#     page = request.GET.get('page', 1)
#     on_sale = request.GET.get('on_sale', None)
#     order_by = request.GET.get('order_by', None)
#     query = request.GET.get('q', None)
#
#     if category_slug == "all":
#         goods = Products.objects.all()
#     elif query:
#         goods = q_search(query)
#     else:
#         goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
#
#     if on_sale:
#         goods = goods.filter(discount__gt=0)
#
#     if order_by and order_by != "default":
#         goods = goods.order_by(order_by)
#
#     paginator = Paginator(goods, 3)
#     current_page = paginator.page(int(page))
#
#     context = {
#         "title": "Home - Каталог",
#         "goods": current_page,
#         "slug_url": category_slug
#     }
#     return render(request, "goods/catalog.html", context)


class ProductView(DetailView):

    # model = Products
    # queryset = Products.objects.all()
    template_name = 'goods/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

# def product(request, product_slug):
#     product = Products.objects.get(slug=product_slug)
#
#     context = {"product": product}
#
#     return render(request, "goods/product.html", context=context)


#_________________ API __________________
# class ProductViewSet(generics.ListAPIView):
#     queryset = Products.objects.all().order_by('id')
#     serializer_class = ProductSerializer

    # def POST(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response({'carts': serializer.data})
    #
    # def PUT(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'errors': 'Method PUT not allowed'})
    #
    #     try:
    #         instance = Products.objects.get(pk=pk)
    #     except:
    #         return Response({'errors': 'Method PUT not allowed'})
    #
    #     serializer = ProductSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})


# class CategoryViewSet(generics.ListAPIView):
#     queryset = Categories.objects.all().order_by('id')
#     serializer_class = CategorySerializer
#     http_method_names = ['get']

    # def POST(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response({'carts': serializer.data})
    #
    # def PUT(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'errors': 'Method PUT not allowed'})
    #
    #     try:
    #         instance = Categories.objects.get(pk=pk)
    #     except:
    #         return Response({'errors': 'Method PUT not allowed'})
    #
    #     serializer = CategorySerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
