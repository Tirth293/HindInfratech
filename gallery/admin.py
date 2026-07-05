from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    # ── List view ──
    list_display  = ('thumbnail_preview', 'display_order', 'title', 'client', 'updated_at')
    list_display_links = ('thumbnail_preview',)   # click the photo to open the full edit page
    list_editable = ('display_order', 'title', 'client')  # edit these directly in the table, then click "Save"
    list_filter   = ('client',)
    search_fields = ('title', 'client', 'description')
    ordering      = ('display_order',)
    list_per_page = 25

    # ── Form layout ──
    fieldsets = (
        ('Image Upload', {
            'fields': ('image', 'image_preview', 'display_order'),
            'description': 'Upload a JPEG or PNG image. Recommended: 1200×800px or larger.',
        }),
        ('Details', {
            'fields': ('title', 'description', 'client'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    # ── Thumbnail in list view ──
    def thumbnail_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="width:80px;height:56px;object-fit:cover;'
                'border-radius:6px;border:1.5px solid #E5E7EB;display:block;">',
                obj.image.url
            )
        return format_html(
            '<span style="color:#9CA3AF;font-size:12px;">{}</span>',
            'No image'
        )
    thumbnail_preview.short_description = 'Preview'

    # ── Large preview in change form ──
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:320px;max-height:220px;'
                'border-radius:10px;border:2px solid #E5E7EB;margin-top:6px;display:block;">',
                obj.image.url
            )
        return format_html(
            '<span style="color:#9CA3AF;font-style:italic;">{}</span>',
            'No image uploaded yet.'
        )
    image_preview.short_description = 'Current Image Preview'
