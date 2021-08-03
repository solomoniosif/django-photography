# Generated by Django 3.2.5 on 2021-08-02 16:14

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('photos', '0008_alter_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
