from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from rest_framework.response import Response

from carts.models import Cart
from carts.utils import get_user_carts
# from carts.serializers import CartSerializer

from goods.models import Products
from rest_framework import viewsets, mixins, generics


def cart_add(request):
    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quaantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


#_________________ API __________________
# class CartViewSet(generics.ListAPIView):
#     queryset = Cart.objects.all().order_by('id')
#     serializer_class = CartSerializer
#     http_method_names = ['get']

    # def POST(self, request):
    #     serializer = CartSerializer(data=request.data)
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
    #         instance = Cart.objects.get(pk=pk)
    #     except:
    #         return Response({'errors': 'Method PUT not allowed'})
    #
    #     serializer = CartSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})


# class CartViewSet(APIView):
#
#     def get(self, request):
#         lst = Cart.objects.all().values()
#         return Response({'carts': list(lst)})
#
#     def post(self, request):
#         post_new = Cart.objects.create(
#             user=request.data['user'],
#             product=request.data['product'],
#             quantity=request.data['quantity'],
#             created_timestamp=request.data['created_timestamp'],
#         )
#         return Response({'carts': model_to_dict(post_new)})


# class CartViewSet(APIView):
#
#     def get(self, request):
#         carts = Cart.objects.all()
#         return Response({'carts': CartSerializer(carts, many=True).data})
#
#     def post(self, request):
#         post_new = Cart.objects.create(
#             user=request.data['user'],
#             product=request.data['product'],
#             quantity=request.data['quantity'],
#             created_timestamp=request.data['created_timestamp'],
#         )
#         return Response({'carts': model_to_dict(post_new)})
