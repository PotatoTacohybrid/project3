# Generated by Django 2.1.4 on 2019-01-05 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0004_auto_20190105_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart_item',
            old_name='item',
            new_name='name',
        ),
    ]
