# Generated by Django 4.2.4 on 2023-10-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_cart_coupon_cart_total_after_coupon_alter_order_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.FloatField(default=10.1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='jpc01glnp9lm3ip', max_length=15),
        ),
    ]
