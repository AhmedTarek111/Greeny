# Generated by Django 4.2.4 on 2024-04-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0058_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='qi7i7dlemla3f1f', max_length=15),
        ),
    ]