from django.contrib import admin

# Register your models here.

from .models import *
# admin.site.register(User, UserAdmin)

admin.site.register(Rooms)
