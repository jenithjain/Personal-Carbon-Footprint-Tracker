from django.core.management.base import BaseCommand
from footprint.models import Category, Product

def populate_data():
    # Create Categories
    categories = [
        {
            'name': 'Home & Living',
            'description': 'Eco-friendly products for your home'
        },
        {
            'name': 'Kitchen',
            'description': 'Sustainable kitchen essentials'
        },
        {
            'name': 'Personal Care',
            'description': 'Natural and sustainable personal care items'
        },
        {
            'name': 'Fashion',
            'description': 'Sustainable fashion and accessories'
        }
    ]

    for cat_data in categories:
        Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )

    # Get category objects
    home_category = Category.objects.get(name='Home & Living')
    kitchen_category = Category.objects.get(name='Kitchen')
    personal_category = Category.objects.get(name='Personal Care')

    # Create Products
    products = [
        {
            'name': 'Bamboo Utensil Set',
            'description': 'Sustainable bamboo utensils for everyday use',
            'category': kitchen_category,
            'price': 24.99,
            'original_price': 29.99,
            'image_url': 'https://example.com/bamboo-utensils.jpg',
            'eco_score': 9,
            'carbon_reduction': 5.2,
            'stock': 50
        },
        {
            'name': 'Reusable Shopping Bags',
            'description': 'Set of 5 organic cotton shopping bags',
            'category': home_category,
            'price': 19.99,
            'original_price': 24.99,
            'image_url': 'https://example.com/shopping-bags.jpg',
            'eco_score': 8,
            'carbon_reduction': 7.5,
            'stock': 100
        },
        {
            'name': 'Bamboo Toothbrush',
            'description': 'Biodegradable bamboo toothbrush',
            'category': personal_category,
            'price': 4.99,
            'original_price': 5.99,
            'image_url': 'https://example.com/bamboo-toothbrush.jpg',
            'eco_score': 9,
            'carbon_reduction': 0.5,
            'stock': 200
        }
    ]

    for prod_data in products:
        Product.objects.get_or_create(
            name=prod_data['name'],
            defaults={
                'description': prod_data['description'],
                'category': prod_data['category'],
                'price': prod_data['price'],
                'original_price': prod_data['original_price'],
                'image_url': prod_data['image_url'],
                'eco_score': prod_data['eco_score'],
                'carbon_reduction': prod_data['carbon_reduction'],
                'stock': prod_data['stock']
            }
        )

class Command(BaseCommand):
    help = 'Populate initial data for the eco-friendly store'

    def handle(self, *args, **kwargs):
        populate_data()
        self.stdout.write(self.style.SUCCESS('Successfully populated initial data')) 