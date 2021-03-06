# Generated by Django 3.2.7 on 2021-09-12 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('url', models.URLField()),
                ('open_hours', models.IntegerField()),
                ('close_hours', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='restaurent/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_food_api.customer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_food_api.order')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='menu/%Y/%m/%d/')),
                ('rest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_food_api.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='reservate',
            field=models.ManyToManyField(through='online_food_api.Reservation', to='online_food_api.Order'),
        ),
    ]
