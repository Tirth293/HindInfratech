from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
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

# ── Serve media files always (no CDN/S3 configured — WhiteNoise only serves STATIC, not MEDIA) ──
# NOTE: django.conf.urls.static.static() silently returns an EMPTY list when
# DEBUG=False, so on production (Render, DEBUG=False) it was serving nothing
# and every project/gallery image 404'd. We register the serve view directly
# with re_path instead, so it works in both DEBUG and production.
urlpatterns += [
    re_path(
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
        static_serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]

# ── Serve static files via Django only in development (WhiteNoise handles it in production) ──
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
