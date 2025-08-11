import os
import sys
import django
from decimal import Decimal
from django.core.files import File
from pathlib import Path

# Ensure project root is on sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Management.settings')
django.setup()

from api.models import Product

# Sample product data — category keys must match PRODUCT_CATEGORY
products_data = [
    {
        'name': 'Smartphone',
        'description': 'High-end smartphone with AMOLED display',
        'price': Decimal('699.99'),
        'category': 'electronics',
        'stock': 10,
        'image': 'sample_images/smartphone.jpg'
    },
    {
        'name': 'Cookbook',
        'description': 'A cookbook with delicious recipes',
        'price': Decimal('19.99'),
        'category': 'books',
        'stock': 50,
        'image': 'sample_images/cookbook.jpg'
    },
    {
        'name': 'Running Shoes',
        'description': 'Lightweight running shoes for daily training',
        'price': Decimal('89.99'),
        'category': 'fashion',
        'stock': 25,
        'image': 'sample_images/shoes.jpg'
    },
]

# Loop and create/update products
for data in products_data:
    image_path = BASE_DIR / 'api' / data['image']  # adjust folder as needed

    product, created = Product.objects.update_or_create(
        name=data['name'],
        defaults={
            'description': data['description'],
            'price': data['price'],
            'category': data['category'],
            'stock': data['stock']
        }
    )

    if image_path.exists():
        with open(image_path, 'rb') as img_file:
            product.image.save(os.path.basename(image_path), File(img_file), save=True)

print("Products populated successfully!")
