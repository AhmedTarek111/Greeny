# Generated by Django 4.2.4 on 2023-12-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='n2p62j7b3d4o0lj', max_length=15),
        ),
    ]