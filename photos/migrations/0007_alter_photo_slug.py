# Generated by Django 3.2.5 on 2021-07-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20210729_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
