# Generated by Django 2.1.4 on 2019-01-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regular_pizza',
            name='large_price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='regular_pizza',
            name='small_price',
            field=models.FloatField(blank=True),
        ),
    ]
