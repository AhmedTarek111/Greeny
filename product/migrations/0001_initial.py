# Generated by Django 4.2.3 on 2023-08-29 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='brand_images', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtitle')),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('price', models.FloatField(verbose_name='Price')),
                ('sku', models.CharField(max_length=150, verbose_name='SKU')),
                ('description', models.TextField(max_length=40000, verbose_name='Description')),
                ('flag', models.CharField(choices=[('Sale', 'Sale'), ('New', 'New'), ('Feature', 'Feature')], max_length=50, verbose_name='Flag')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.brand', verbose_name='Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500, verbose_name='Review')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Proudct')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='proudct_images', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Proudct')),
            ],
        ),
    ]
