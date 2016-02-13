# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('element_id', models.AutoField(serialize=False, primary_key=True)),
                ('element_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='ItemReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'No Title', max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField(choices=[(0, b''), (1, b'Disappointed'), (2, b'Not Promissing'), (3, b'OK'), (4, b'Good'), (5, b'Awesome')])),
                ('review', models.TextField()),
                ('item', models.ForeignKey(to='restaurant.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.AutoField(serialize=False, primary_key=True)),
                ('restaurant_name', models.CharField(max_length=70)),
                ('proprietor_name', models.CharField(max_length=70)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('address', models.CharField(default=b'Not added', max_length=100)),
                ('district', models.CharField(max_length=20)),
                ('website', models.URLField(null=True, blank=True)),
                ('login', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='element',
            name='item',
            field=models.ManyToManyField(to='restaurant.Item'),
        ),
    ]
