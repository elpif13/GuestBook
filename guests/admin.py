from django.contrib import admin

from .models import Entry, User

admin.site.register(User)
admin.site.register(Entry)
# Register your models here.
