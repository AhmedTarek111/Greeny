# Generated by Django 4.2.4 on 2023-12-05 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_codes


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_remove_deliveryaddress_profile_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile')),
                ('code', models.CharField(default=utils.generate_codes.generate_code, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Bussiness', 'Bussiness'), ('Academy', 'Academy'), ('Other', 'Other')], max_length=80)),
                ('address', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contact_number', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
