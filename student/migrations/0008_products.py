# Generated by Django 4.0 on 2022-01-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_info_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
