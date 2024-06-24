from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, FormView

from carts.models import Cart
from orders.models import Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm, ForgotPasswordForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy('home:index')

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('home:index')

    def form_valid(self, form):
        session_key = self.request.session.session_key

        user = form.get_user()

        if user:
            auth.login(self.request, user)
            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(self.request, f"{user.username}, Вы вошли в аккаунт")

                return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Авторизация'
        return context


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#
#             session_key = request.session.session_key
#
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, Вы вошли в аккаунт")
#
#                 if session_key:
#                     Cart.objects.filter(session_key=session_key).update(user=user)
#
#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#
#                 return HttpResponseRedirect(reverse('home:index'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Home - Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Регистрация'
        return context


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#
#             session_key = request.session.session_key
#
#             user = form.instance
#             auth.login(request, user)
#
#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)
#             messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
#             return HttpResponseRedirect(reverse('home:index'))
#     else:
#         form = UserRegistrationForm()
#
#     context = {
#         'title': 'Home - Регистрация',
#         'form': form
#     }
#     return render(request, 'users/registration.html', context)


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success((self.request, "Профайл успешно обновлён"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Произошла ошибка")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Кабинет'
        context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        ).order_by("-id")
        return context


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Профайл успешно обновлен")
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)
#
#     orders = Order.objects.filter(user=request.user).prefetch_related(
#         Prefetch(
#             "orderitem_set",
#             queryset=OrderItem.objects.select_related("product"),
#         )
#     ).order_by("-id")
#
#     context = {
#         'title': 'Home - Кабинет',
#         'form': form,
#         'orders': orders,
#     }
#     return render(request, 'users/profile.html', context)


class UserCartView(TemplateView):
    template_name = 'users/users_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Корзина'
        return context


# def users_cart(request):
#     return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('home:index'))


class ForgotPasswordView(FormView):
    template_name = 'users/forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        messages.success(self.request, f"Письмо отправлено на электронный адрес {email}")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Забыли пароль?'
        return context


# def forgot_password(request):
#     if request.method == 'POST':
#         form = ForgotPasswordForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             messages.success(request, f"Письмо отправлено на электронный адрес {email}")
#             return HttpResponseRedirect(reverse('home:index'))
#     else:
#         form = ForgotPasswordForm()
#
#     context = {
#         'title': 'Home - Забыли пароль?',
#         'form': form
#     }
#
#     return render(request, 'users/forgot_password.html', context)
