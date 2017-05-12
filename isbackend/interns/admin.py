from django.contrib import admin
from .models import Intern
from .models import Comments


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Intern, AuthorAdmin)
admin.site.register(Comments, AuthorAdmin)
