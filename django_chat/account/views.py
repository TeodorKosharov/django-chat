from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django_chat.account.forms import RegisterForm, LoginForm


class RegisterPage(CreateView):
    template_name = 'register-page.html'
    form_class = RegisterForm
    success_url = '/'


class LoginPage(LoginView):
    template_name = 'login-page.html'
    form_class = LoginForm


class LogoutPage(LogoutView):
    pass
