# Generated by Django 4.2.4 on 2024-03-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_coupon_end_date_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='d02ao4cp4oj4f0k', max_length=15),
        ),
    ]