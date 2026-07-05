from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Project


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean_number(self):
        number = self.cleaned_data['number']
        duplicate = Project.objects.filter(number__iexact=number)
        if self.instance.pk:
            duplicate = duplicate.exclude(pk=self.instance.pk)
        if duplicate.exists():
            raise forms.ValidationError(
                'A project with this number already exists. Please edit the existing project or use a different number.'
            )
        return number


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    # ── List view ──
    list_display  = ('thumbnail_preview', 'number', 'title', 'client', 'status', 'updated_at')
    list_display_links = ('thumbnail_preview',)   # click the photo to open the full edit page
    list_editable = ('number', 'title', 'client', 'status')  # edit these directly in the table, then click "Save"
    list_filter   = ('status',)
    search_fields = ('title', 'client', 'description', 'number')
    ordering      = ('number',)
    list_per_page = 25

    # ── Use the same form (with duplicate-number check) for inline list editing ──
    def get_changelist_form(self, request, **kwargs):
        return ProjectAdminForm

    # ── Form layout ──
    fieldsets = (
        ('Project Photos', {
            'fields': ('image', 'image_preview', 'image2', 'image2_preview'),
            'description': (
                'Upload up to two JPEG or PNG images. The first image shows on the project card; '
                'both images appear in the popup when a visitor clicks the project. Recommended: 800×500px or larger.'
            ),
        }),
        ('Project Info', {
            'fields': ('number', 'title', 'client', 'status', 'description')
        }),
        ('Badge Styling', {
            'fields': ('badge_color', 'text_color'),
            'classes': ('collapse',),
            'description': (
                'CSS classes used to style the project badge on the public website. '
                'Choices: bg-blue-soft / bg-orange-soft / bg-green-soft / badge-purple '
                'and text-blue / text-orange / text-green'
            ),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at', 'image_preview', 'image2_preview')

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
    thumbnail_preview.short_description = 'Photo'

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

    # ── Large preview for the second image in the change form ──
    def image2_preview(self, obj):
        if obj.image2:
            return format_html(
                '<img src="{}" style="max-width:320px;max-height:220px;'
                'border-radius:10px;border:2px solid #E5E7EB;margin-top:6px;display:block;">',
                obj.image2.url
            )
        return format_html(
            '<span style="color:#9CA3AF;font-style:italic;">{}</span>',
            'No second image uploaded yet.'
        )
    image2_preview.short_description = 'Current Second Image Preview'
