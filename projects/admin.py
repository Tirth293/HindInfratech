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
    list_display  = ('number', 'title', 'client', 'status_badge', 'updated_at')
    list_filter   = ('status',)
    search_fields = ('title', 'client', 'description', 'number')
    ordering      = ('number',)
    list_per_page = 25

    # ── Form layout ──
    fieldsets = (
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

    readonly_fields = ('created_at', 'updated_at')

    # ── Custom columns ──
    def status_badge(self, obj):
        colors = {
            'completed': ('#15803d', '#dcfce7'),
            'ongoing':   ('#c2410c', '#ffedd5'),
        }
        color, bg = colors.get(obj.status, ('#1B4FA0', '#eff6ff'))
        label = obj.get_status_display()
        return format_html(
            '<span style="display:inline-flex;align-items:center;padding:3px 10px;'
            'border-radius:20px;font-size:11.5px;font-weight:700;'
            'color:{};background:{}">{}</span>',
            color, bg, label
        )
    status_badge.short_description = 'Status'
    status_badge.admin_order_field = 'status'
