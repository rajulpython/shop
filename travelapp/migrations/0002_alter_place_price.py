# Generated by Django 4.0.5 on 2022-07-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='price',
            field=models.IntegerField(),
        ),
    ]
