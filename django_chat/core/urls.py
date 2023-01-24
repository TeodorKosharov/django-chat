from django.urls import path
from django_chat.core.views import home

urlpatterns = (
    path('', home),

)
