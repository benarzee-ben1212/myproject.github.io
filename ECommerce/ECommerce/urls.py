from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('electronicstore.urls')),
    path('', include('chat.urls')),
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
]
