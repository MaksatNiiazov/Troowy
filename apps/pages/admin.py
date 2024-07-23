from django.contrib import admin
from django.utils.html import format_html

from .models import StaticPage, WelcomeProperty, WelcomeCars, WelcomeTours, WelcomeInternationalTours, \
    WelcomeMedicalTours, ImageBase, WelcomePropertyImage, WelcomeCarsImage, WelcomeToursImage, \
    WelcomeInternationalToursImage, WelcomeMedicalToursImage, Banner


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'image', 'created_at', 'updated_at']
    list_display_links = ['title', 'slug']


class BaseImageInline(admin.TabularInline):
    fields = ['image_preview', 'image']
    readonly_fields = ['image_preview']
    extra = 1

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; height: auto;" />', obj.image.url)
        return ""

    image_preview.short_description = "Предпросмотр"


class WelcomePropertyImageInline(BaseImageInline):
    model = WelcomePropertyImage


class WelcomeCarsImageInline(BaseImageInline):
    model = WelcomeCarsImage


class WelcomeToursImageInline(BaseImageInline):
    model = WelcomeToursImage


class WelcomeInternationalToursImageInline(BaseImageInline):
    model = WelcomeInternationalToursImage


class WelcomeMedicalToursImageInline(BaseImageInline):
    model = WelcomeMedicalToursImage


class WelcomeBaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_preview']
    search_fields = ['title', 'content']

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_preview.short_description = "Краткое содержание"


@admin.register(WelcomeProperty)
class WelcomePropertyAdmin(WelcomeBaseAdmin):
    inlines = [WelcomePropertyImageInline]


@admin.register(WelcomeCars)
class WelcomeCarsAdmin(WelcomeBaseAdmin):
    inlines = [WelcomeCarsImageInline]


@admin.register(WelcomeTours)
class WelcomeToursAdmin(WelcomeBaseAdmin):
    inlines = [WelcomeToursImageInline]


@admin.register(WelcomeInternationalTours)
class WelcomeInternationalToursAdmin(WelcomeBaseAdmin):
    inlines = [WelcomeInternationalToursImageInline]


@admin.register(WelcomeMedicalTours)
class WelcomeMedicalToursAdmin(WelcomeBaseAdmin):
    inlines = [WelcomeMedicalToursImageInline]


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "page_for", "is_active", "created_at"]
    list_filter = ["title", "page_for", "is_active", "created_at"]
    search_fields = ["title", "page_for", "link", "created_at"]
    date_hierarchy = "created_at"
    fields = (
        "title",
        "link",
        "page_for",
        "image_desktop",
        "get_image_desktop",
        "image_mobile",
        "get_image_mobile",
        "is_active",
        "created_at",
    )
    readonly_fields = ("get_image_desktop", "get_image_mobile", "created_at")
