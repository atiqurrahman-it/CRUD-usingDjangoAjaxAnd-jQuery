from django.contrib import admin
from .models import MyUser


# Register your models here.
@admin.register(MyUser)
class adminMyuser(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
