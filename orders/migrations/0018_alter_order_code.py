# Generated by Django 4.2.4 on 2023-11-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0017_deleviry_fee_alter_order_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="code",
            field=models.CharField(default="if57f45fl2eoeii", max_length=15),
        ),
    ]
