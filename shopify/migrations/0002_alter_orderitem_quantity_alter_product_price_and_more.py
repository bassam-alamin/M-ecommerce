# Generated by Django 5.0.4 on 2024-04-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]