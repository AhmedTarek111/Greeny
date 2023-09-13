# Generated by Django 4.2.4 on 2023-09-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('facebook_link', models.EmailField(max_length=254)),
                ('twiter_link', models.EmailField(max_length=254)),
                ('linkedin_link', models.EmailField(max_length=254)),
                ('instagram_link', models.EmailField(max_length=254)),
                ('pintrest_link', models.EmailField(max_length=254)),
                ('android_app', models.URLField()),
            ],
        ),
    ]
