from django.shortcuts import render
from projects.models import Project
from gallery.models import Gallery


def home(request):
    """Main home page view — reads live data from SQLite."""
    projects = Project.objects.all().order_by('number')
    gallery_items = Gallery.objects.all().order_by('display_order')
    completed_count = Project.objects.filter(status='completed').count()
    total_projects = Project.objects.count()

    context = {
        'projects': projects,
        'gallery_items': gallery_items,
        'completed_count': completed_count,
        'total_projects': total_projects,
    }

    return render(request, 'index.html', context)
