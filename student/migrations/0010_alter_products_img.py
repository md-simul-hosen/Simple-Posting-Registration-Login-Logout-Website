# Generated by Django 4.0 on 2022-01-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]