# Generated by Django 3.2.5 on 2021-07-25 05:56

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('photos', '0002_alter_photo_album'),
        ('blog', '0005_alter_post_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.ManyToManyField(to='photos.Photo'),
        ),
    ]
