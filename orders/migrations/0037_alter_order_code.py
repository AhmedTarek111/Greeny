# Generated by Django 4.2.4 on 2024-03-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='8gmem3ci4cmp78d', max_length=15),
        ),
    ]
