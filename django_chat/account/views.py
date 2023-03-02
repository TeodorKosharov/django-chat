from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django_chat.account.forms import RegisterForm, LoginForm
from django_chat.core.models import ChatRoom


class RegisterPage(CreateView):
    template_name = 'register-page.html'
    form_class = RegisterForm
    success_url = '/'


class LoginPage(LoginView):
    template_name = 'login-page.html'
    form_class = LoginForm


class LogoutPage(LogoutView):
    pass


def settings_page(request):
    user_rooms = ChatRoom.objects.filter(creator_id=request.user.id)
    context = {
        'user_rooms': user_rooms
    }
    return render(request, 'settings.html', context)


def delete_room(request, room_name):
    ChatRoom.objects.filter(room_name=room_name)[0].delete()
    return HttpResponse()
