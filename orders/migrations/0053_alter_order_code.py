# Generated by Django 4.2.4 on 2024-04-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0052_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='d88oqle79a8bbeq', max_length=15),
        ),
    ]
