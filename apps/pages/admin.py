from django.contrib import admin

from .models import StaticPage


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'image', 'created_at', 'updated_at']
    list_display_links = ['title', 'slug']
