# Generated by Django 2.1.4 on 2019-01-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0007_auto_20190105_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart_item',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]