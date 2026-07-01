from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from projects.views import home

# ── Admin site branding ──
admin.site.site_header = 'Hind Infratech'
admin.site.site_title  = 'Hind Infratech Admin'
admin.site.index_title = 'Admin Panel'

# ── Remove User and Group from admin so sidebar only shows Projects & Gallery ──
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

urlpatterns = [
    # Main admin — Django's built-in admin already handles:
    #   /admin/password_change/       (AdminPasswordChangeView)
    #   /admin/password_change/done/  (PasswordChangeDoneView)
    # Do NOT add custom routes for these — they conflict and break the form.
    path('admin/', admin.site.urls),

    # Public website home
    path('', home, name='home'),
]

# ── Serve media and static files in development ──
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
