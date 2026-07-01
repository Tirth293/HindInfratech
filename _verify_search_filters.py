import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from django.contrib.auth import get_user_model
from django.test import Client

from gallery.models import Gallery
from projects.models import Project


User = get_user_model()
username = "codex_search_admin"
User.objects.filter(username=username).delete()
user = User.objects.create_superuser(
    username=username,
    email="codex@example.com",
    password="Searchpass12345",
)

project = None
gallery = None

try:
    client = Client()
    assert client.login(username=username, password="Searchpass12345")

    project = Project.objects.create(
        number="SRCH99",
        title="Codex Search Project",
        client="Codex",
        status="ongoing",
        description="Temporary record for admin search verification.",
        badge_color="bg-blue-soft",
        text_color="text-blue",
    )
    existing_gallery = Gallery.objects.first()
    if existing_gallery:
        gallery = Gallery.objects.create(
            title="Codex Search Gallery",
            description="Temporary record for admin search verification.",
            image=existing_gallery.image,
            client="Codex",
            display_order=999,
        )

    checks = [
        ("/admin/projects/project/?q=Codex+Search+Project", b"Codex Search Project"),
        ("/admin/projects/project/?status__exact=ongoing", b"Codex Search Project"),
    ]
    if gallery:
        checks.extend(
            [
                ("/admin/gallery/gallery/?q=Codex+Search+Gallery", b"Codex Search Gallery"),
                ("/admin/gallery/gallery/?client=Codex", b"Codex Search Gallery"),
            ]
        )

    for url, expected in checks:
        response = client.get(url)
        assert response.status_code == 200, (url, response.status_code)
        assert expected in response.content, url
        assert b'id="changelist-search"' in response.content, url
        assert b'id="changelist-filter"' in response.content or "gallery" in url, url

finally:
    if project:
        project.delete()
    if gallery:
        gallery.delete()
    user.delete()

print("admin search and filter verification passed")
