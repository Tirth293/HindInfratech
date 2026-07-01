import os
import django
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gallery.models import Gallery

class Command(BaseCommand):
    help = 'Fix gallery image paths from "images/" to "gallery/"'

    def handle(self, *args, **options):
        self.stdout.write('Starting gallery image path fix...')

        updated_count = 0
        for item in Gallery.objects.all():
            if item.image:
                # Get the current path
                current_path = str(item.image)
                
                # If it's using 'images/' path, convert it to 'gallery/' path
                if current_path.startswith('images'):
                    # Extract just the filename
                    filename = os.path.basename(current_path)
                    # Create new path with 'gallery/' prefix
                    new_path = os.path.join('gallery', filename)
                    
                    # Update the item
                    item.image = new_path
                    item.save()
                    updated_count += 1
                    self.stdout.write(f"✓ Fixed: {current_path} → {new_path}")

        self.stdout.write(self.style.SUCCESS(f'✓ Fixed {updated_count} gallery items successfully!'))
