from django.contrib import admin

from voli.core.models import Recipe, Tag

admin.site.register(Recipe)
admin.site.register(Tag)