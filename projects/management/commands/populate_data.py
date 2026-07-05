import os
import django
from django.core.management.base import BaseCommand
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from projects.models import Project
from gallery.models import Gallery

class Command(BaseCommand):
    help = 'Populate database with initial projects and gallery data'

    def handle(self, *args, **options):
        self.stdout.write('Starting data population...')

        # Delete existing data
        Project.objects.all().delete()
        Gallery.objects.all().delete()

        # Create Projects
        projects_data = [
            {
                'number': '01',
                'title': 'Utility Duct – Devka Beach (5.5 km)',
                'description': 'Casting & laying 600mm & 750mm utility ducts with lid along Devka Beach coastal corridor.',
                'client': 'RKC Infrabuilt',
                'status': 'completed',
                'badge_color': 'bg-blue-soft',
                'text_color': 'text-blue',
                'image': 'projects/devka-beach-utility-duct-1.jpeg',
            },
            {
                'number': '02',
                'title': 'Box Culvert – Silvassa',
                'description': 'Casting and erecting various types of box culvert structures at Silvassa for road infrastructure.',
                'client': 'MJ Infra',
                'status': 'completed',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/silvassa-box-culvert-1.jpeg',
            },
            {
                'number': '03',
                'title': 'Utility Duct – Silvassa (8 km Double Row)',
                'description': 'Casting & laying 600mm–1200mm utility ducts with lid at Silvassa (8 km double row).',
                'client': 'RKC Infrabuilt',
                'status': 'completed',
                'badge_color': 'bg-blue-soft',
                'text_color': 'text-blue',
                'image': 'projects/silvassa-box-culvert-2.jpeg',
            },
            {
                'number': '04',
                'title': 'Precast Elements – Dharoi Dam',
                'description': 'Casting precast benches, coping, light poles, chambers, and other elements at Dharoi Dam site.',
                'client': 'PSP Projects',
                'status': 'completed',
                'badge_color': 'badge-purple',
                'text_color': 'text-purple',
                'image': 'projects/dharoi-dam-precast-1.jpeg',
            },
            {
                'number': '05',
                'title': 'Boundary Wall – Vadodara-Delhi Expressway (55 km)',
                'description': 'Casting 55 km precast boundary wall (planks & poles) for Vadodara-Delhi Expressway Package-11, Ganjad.',
                'client': 'RKC Infrabuilt',
                'status': 'completed',
                'badge_color': 'bg-blue-soft',
                'text_color': 'text-blue',
                'image': 'projects/devka-beach-utility-duct-2.jpeg',
            },
            {
                'number': '06',
                'title': 'Flooring & Landscaping – Dharoi Dam',
                'description': 'Complete flooring and landscaping construction at Dharoi Dam for public infrastructure development.',
                'client': 'PSP Projects',
                'status': 'completed',
                'badge_color': 'badge-purple',
                'text_color': 'text-purple',
                'image': 'projects/dharoi-dam-precast-2.jpeg',
            },
            {
                'number': '07',
                'title': 'Structural Work – Silvassa',
                'description': 'Box culverts, protection walls, culverts, and other structural works at Silvassa.',
                'client': 'RKC Infrabuilt',
                'status': 'completed',
                'badge_color': 'bg-blue-soft',
                'text_color': 'text-blue',
                'image': 'projects/silvassa-box-culvert-3.jpeg',
            },
            {
                'number': '08',
                'title': 'U-Shape Drain – Precast Factory',
                'description': 'Casting 450mm and 550mm U-shape drains at Precast Factory for drainage infrastructure.',
                'client': 'PSP Projects',
                'status': 'completed',
                'badge_color': 'badge-purple',
                'text_color': 'text-purple',
                'image': 'projects/dharoi-dam-precast-3.jpeg',
            },
            {
                'number': '09',
                'title': 'Precast Girder – Dandi',
                'description': 'Construction of precast girders at Dandi for structural bridge infrastructure support.',
                'client': 'Independent',
                'status': 'completed',
                'badge_color': 'bg-green-soft',
                'text_color': 'text-green',
                'image': 'projects/devka-beach-utility-duct-3.jpeg',
            },
            {
                'number': 'OG1',
                'title': 'Kerbs & Road Furnishings – Mankol',
                'description': 'Casting various types of kerbs and road furnishing items at Precast Factory Mankol. Continuous work.',
                'client': 'PSP Projects',
                'status': 'ongoing',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/silvassa-box-culvert-4.jpeg',
            },
            {
                'number': 'OG2',
                'title': 'Precast Benches – Sabarmati Riverfront',
                'description': 'Casting and laying precast benches at the iconic Sabarmati Riverfront, Ahmedabad.',
                'client': 'PSP Projects',
                'status': 'ongoing',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/dharoi-dam-precast-4.jpeg',
            },
            {
                'number': 'OG3',
                'title': 'Precast Drains – Ahmedabad Ring Road',
                'description': 'Casting and laying precast drains at Ahmedabad Ring Road Project.',
                'client': 'RKC Infrabuilt',
                'status': 'ongoing',
                'badge_color': 'bg-blue-soft',
                'text_color': 'text-blue',
                'image': 'projects/devka-beach-utility-duct-4.jpeg',
            },
            {
                'number': 'OG4',
                'title': 'Flooring & Tiling – 19 Storey Building, Ambali',
                'description': 'Flooring and tiling work for 19-storey residential building at Ambali, Ahmedabad.',
                'client': 'PSP Projects',
                'status': 'ongoing',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/dharoi-dam-precast-1.jpeg',
            },
            {
                'number': 'OG5',
                'title': 'High Level Major Bridge on Kim River',
                'description': 'Construction of high level major bridge on Kim River at Valia-Mangrol Road, Ta. Valia, Dist. Bharuch — in joint venture with Brahmani Buildtech Company.',
                'client': 'Joint Venture',
                'status': 'ongoing',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/silvassa-box-culvert-1.jpeg',
            },
            {
                'number': 'OG6',
                'title': 'Bridge on Nahiyer Khadi',
                'description': 'Construction of bridge on Palej-Ikhar-Sarbhan Road on Nahiyer Khadi, Ta. Amod, Dist. Bharuch — in joint venture with Brahmani Buildtech Company.',
                'client': 'Joint Venture',
                'status': 'ongoing',
                'badge_color': 'bg-orange-soft',
                'text_color': 'text-orange',
                'image': 'projects/silvassa-box-culvert-2.jpeg',
            },
        ]

        for project_data in projects_data:
            Project.objects.create(**project_data)
            self.stdout.write(f"✓ Created project: {project_data['title']}")

        # Create Gallery Items
        gallery_data = [
            {
                'title': 'Utility Duct – Devka Beach',
                'description': 'Casting & laying 600mm & 750mm utility ducts with lid along Devka Beach coastal corridor (5.5 km).',
                'client': 'RKC Infrabuilt Pvt Ltd',
                'display_order': 0,
            },
            {
                'title': 'Utility Duct – Devka Beach',
                'description': 'Casting & laying 600mm & 750mm utility ducts with lid along Devka Beach coastal corridor (5.5 km).',
                'client': 'RKC Infrabuilt Pvt Ltd',
                'display_order': 1,
            },
            {
                'title': 'Utility Duct – Devka Beach',
                'description': 'Casting & laying 600mm & 750mm utility ducts with lid along Devka Beach coastal corridor (5.5 km).',
                'client': 'RKC Infrabuilt Pvt Ltd',
                'display_order': 2,
            },
            {
                'title': 'Utility Duct – Devka Beach',
                'description': 'Casting & laying 600mm & 750mm utility ducts with lid along Devka Beach coastal corridor (5.5 km).',
                'client': 'RKC Infrabuilt Pvt Ltd',
                'display_order': 3,
            },
            {
                'title': 'Dharoi Dam Precast Elements',
                'description': 'Casting precast benches, coping, light poles, chambers, and other elements at Dharoi Dam.',
                'client': 'PSP Projects Ltd',
                'display_order': 4,
            },
            {
                'title': 'Dharoi Dam Precast Elements',
                'description': 'Casting precast benches, coping, light poles, chambers, and other elements at Dharoi Dam.',
                'client': 'PSP Projects Ltd',
                'display_order': 5,
            },
            {
                'title': 'Dharoi Dam Precast Elements',
                'description': 'Casting precast benches, coping, light poles, chambers, and other elements at Dharoi Dam.',
                'client': 'PSP Projects Ltd',
                'display_order': 6,
            },
            {
                'title': 'Dharoi Dam Precast Elements',
                'description': 'Casting precast benches, coping, light poles, chambers, and other elements at Dharoi Dam.',
                'client': 'PSP Projects Ltd',
                'display_order': 7,
            },
            {
                'title': 'Box Culvert – Silvassa',
                'description': 'Casting and erecting various types of box culvert structures for road infrastructure at Silvassa.',
                'client': 'M J Infra',
                'display_order': 8,
            },
            {
                'title': 'Box Culvert – Silvassa',
                'description': 'Casting and erecting various types of box culvert structures for road infrastructure at Silvassa.',
                'client': 'M J Infra',
                'display_order': 9,
            },
            {
                'title': 'Box Culvert – Silvassa',
                'description': 'Casting and erecting various types of box culvert structures for road infrastructure at Silvassa.',
                'client': 'M J Infra',
                'display_order': 10,
            },
            {
                'title': 'Box Culvert – Silvassa',
                'description': 'Casting and erecting various types of box culvert structures for road infrastructure at Silvassa.',
                'client': 'M J Infra',
                'display_order': 11,
            },
        ]

        for i, gallery_item_data in enumerate(gallery_data):
            image_filename = [
                'devka-beach-utility-duct-1.jpeg',
                'devka-beach-utility-duct-2.jpeg',
                'devka-beach-utility-duct-3.jpeg',
                'devka-beach-utility-duct-4.jpeg',
                'dharoi-dam-precast-1.jpeg',
                'dharoi-dam-precast-2.jpeg',
                'dharoi-dam-precast-3.jpeg',
                'dharoi-dam-precast-4.jpeg',
                'silvassa-box-culvert-1.jpeg',
                'silvassa-box-culvert-2.jpeg',
                'silvassa-box-culvert-3.jpeg',
                'silvassa-box-culvert-4.jpeg',
            ][i]

            # Use 'gallery/' path to match the upload_to setting in the model
            image_path = os.path.join('gallery', image_filename)
            
            Gallery.objects.create(**gallery_item_data, image=image_path)
            self.stdout.write(f"✓ Created gallery item: {gallery_item_data['title']} ({i+1}/12)")

        self.stdout.write(self.style.SUCCESS('✓ Data population completed successfully!'))
