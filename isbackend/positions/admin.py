from django.contrib import admin
from .models import Position


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Position, AuthorAdmin)