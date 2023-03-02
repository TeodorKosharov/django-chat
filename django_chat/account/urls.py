from django.urls import path
from django_chat.account.views import RegisterPage, LoginPage, LogoutPage, settings_page, delete_room

urlpatterns = (
    path('register/', RegisterPage.as_view(), name='register url'),
    path('login/', LoginPage.as_view(), name='login url'),
    path('logout/', LogoutPage.as_view(), name='logout url'),
    path('settings/', settings_page, name='settings url'),
    path('delete-room/<str:room_name>/', delete_room, name='delete room')
)
