from django.contrib import admin
from .models import CustomUserManager, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CustomUserManager)