from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Room, Message


admin.site.register(Room)
admin.site.register(Message)