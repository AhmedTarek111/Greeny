import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker 
from product.models import Brand ,Product
import random
from random import randint

fake = Faker()

def seed_brand(n):
    for _ in range(n):
        image=['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']

        Brand.objects.create(
            name=fake.name(),
            image=f"brand_images/{image[randint(0,9)]}"
        )
    print(f"added {n} brands successfuly ")

# seed_brand(45)

def seed_products(n):
    images=['11.jpeg', '12.jpeg', '13.jpeg', '14.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg', '19.jpeg']
    flag_choices =['Sale','New','Feature']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            subtitle =fake.text(),
            image =f'product_images/{images[randint(0,8)]}',
            price =round(random.uniform(9.99,99.99),2),
            sku =randint(10000,100000000),
            description = fake.text() ,
            flag = flag_choices[randint(0,2)],
            brand= Brand.objects.get(id=randint(134,180)),
            quantity = randint(0,10),
            tags="dummy",
        )
    print(f"added {n} Products successfuly ")

seed_products(100)