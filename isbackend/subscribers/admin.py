from django.contrib import admin
from .models import Subscriber

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subscriber, AuthorAdmin)