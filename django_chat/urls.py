from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('django_chat.core.urls')),
    path('account/', include('django_chat.account.urls'))
]
