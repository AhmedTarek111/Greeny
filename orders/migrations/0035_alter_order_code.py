# Generated by Django 4.2.4 on 2024-03-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='23jmke7q24egoc1', max_length=15),
        ),
    ]