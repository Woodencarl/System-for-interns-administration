from django.contrib import admin
from .models import Intern


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Intern, AuthorAdmin)
