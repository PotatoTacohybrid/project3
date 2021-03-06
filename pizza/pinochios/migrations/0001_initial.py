# Generated by Django 2.1.4 on 2019-01-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regular_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('small_price', models.IntegerField(blank=True)),
                ('large_price', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='regular_pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='Regular_Pizzas', to='pinochios.Topping'),
        ),
    ]
