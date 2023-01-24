from django.urls import path
from django_chat.account.views import RegisterPage, LoginPage, LogoutPage

urlpatterns = (
    path('register/', RegisterPage.as_view(), name='register url'),
    path('login/', LoginPage.as_view(), name='login url'),
    path('logout/', LogoutPage.as_view(), name='logout url')
)
