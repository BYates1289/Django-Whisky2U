# Generated by Django 3.2.8 on 2022-02-16 19:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('info', models.TextField(max_length=250)),
                ('rating_number', models.IntegerField(blank=True, default=0)),
                ('total_ratings', models.IntegerField(blank=True, default=0)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('abv', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('product_stripe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price_is_subscribe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price_not_subscribe_id', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('stars', models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userraing', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
