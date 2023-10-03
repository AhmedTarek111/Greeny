# Generated by Django 4.2.4 on 2023-10-03 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_cartdetail_quantity_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='f0jclcq46l9i9qf', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_coupon', to='orders.coupon'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_after_coupon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
