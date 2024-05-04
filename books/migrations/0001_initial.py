# Generated by Django 5.0.4 on 2024-05-04 14:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(default=None, max_length=2000)),
                ('language', models.CharField(max_length=500)),
                ('genres', models.CharField(default=None, max_length=2000)),
                ('bookFormat', models.CharField(max_length=500)),
                ('edition', models.CharField(max_length=500)),
                ('pages', models.FloatField(blank=True, null=True)),
                ('publisher', models.CharField(max_length=500)),
                ('awards', models.CharField(max_length=500)),
                ('likedPercent', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(default=False, max_length=2083)),
                ('price', models.FloatField(blank=True, null=True)),
                ('book_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(blank=True, max_length=255, null=True)),
                ('town_city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('order_notes', models.TextField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
