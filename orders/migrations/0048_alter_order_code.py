# Generated by Django 4.2.4 on 2024-04-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0047_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='l97g073dnlmqio8', max_length=15),
        ),
    ]