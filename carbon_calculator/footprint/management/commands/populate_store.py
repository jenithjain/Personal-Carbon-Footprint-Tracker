from django.core.management.base import BaseCommand
from footprint.models import Category, Product

class Command(BaseCommand):
    help = 'Populate initial store data'

    def handle(self, *args, **kwargs):
        # Create Categories
        home_living = Category.objects.create(
            name='Home & Living',
            description='Eco-friendly products for your home'
        )

        kitchen = Category.objects.create(
            name='Kitchen',
            description='Sustainable kitchen essentials'
        )

        personal_care = Category.objects.create(
            name='Personal Care',
            description='Natural and sustainable personal care items'
        )

        # Create Products
        Product.objects.create(
            name='Bamboo Utensil Set',
            description='Complete set of sustainable bamboo utensils perfect for everyday use and travel.',
            category=kitchen,
            price=24.99,
            original_price=29.99,
            image_url='https://example.com/bamboo-utensils.jpg',
            eco_score=9,
            carbon_reduction=5.2,
            max_discount=25,
            stock=50
        )

        Product.objects.create(
            name='Reusable Shopping Bags',
            description='Set of 5 durable organic cotton bags for all your shopping needs.',
            category=home_living,
            price=19.99,
            original_price=24.99,
            image_url='https://example.com/shopping-bags.jpg',
            eco_score=8,
            carbon_reduction=7.5,
            max_discount=20,
            stock=100
        )

        Product.objects.create(
            name='Stainless Steel Water Bottle',
            description='Double-walled insulated bottle keeps drinks cold for 24 hours or hot for 12 hours.',
            category=personal_care,
            price=29.99,
            original_price=34.99,
            image_url='https://example.com/water-bottle.jpg',
            eco_score=9,
            carbon_reduction=12.3,
            max_discount=15,
            stock=75
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated store data')) 