from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Events

admin.site.register(Users, UserAdmin)
admin.site.register(Events)
