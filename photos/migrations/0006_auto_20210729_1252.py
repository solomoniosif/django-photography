# Generated by Django 3.2.5 on 2021-07-29 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_alter_photo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
