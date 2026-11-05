from django.core.management.base import BaseCommand
from core.models import Category, Product

class Command(BaseCommand):
    help = 'Add clearly identified local sample catalogue records without overwriting existing records.'
    def handle(self, *args, **options):
        produce, _ = Category.objects.get_or_create(slug='fresh-produce', defaults={'name': 'Fresh produce'})
        pantry, _ = Category.objects.get_or_create(slug='pantry-essentials', defaults={'name': 'Pantry essentials'})
        samples = [
            ('Fresh tomatoes', '500 g pack', 185000, 8, produce, '/images/sample-tomatoes.png', False),
            ('Long grain rice', '1 kg pack', 320000, 5, pantry, '/images/sample-rice.png', False),
            ('White yam', '1 piece', 450000, 4, produce, '/images/sample-yam.png', False),
            ('Leafy greens', '1 bunch', 120000, 0, produce, '/images/sample-greens.png', False),
            ('Example grocery basket', '1 basket', 850000, 2, pantry, '', True),
        ]
        for name, unit, price, stock, category, image, basket in samples:
            Product.objects.get_or_create(name=name, unit=unit, defaults={'category': category, 'price_kobo': price, 'stock': stock, 'image_path': image, 'is_basket': basket})
        self.stdout.write('Sample catalogue ready; existing records were not overwritten.')
