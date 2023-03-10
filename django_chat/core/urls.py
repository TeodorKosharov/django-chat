from django.urls import path
from django_chat.core.views import home, chat_room, add_chat_room, enter_chat_room, add_message, get_info, \
    delete_message

urlpatterns = (
    path('', home, name='home'),
    path('<str:room_name>/', chat_room, name='chat room'),
    path('add-room/<str:room_name>/', add_chat_room, name='add chat room'),
    path('enter-room/<str:room_name>/', enter_chat_room, name='enter chat room'),
    path('send/<str:message>/<str:sender_id>/<str:room_name>/', add_message, name='add message'),
    path('info/get', get_info, name='get info'),
    path('delete-message/<int:message_id>/', delete_message, name='delete message'),
)
