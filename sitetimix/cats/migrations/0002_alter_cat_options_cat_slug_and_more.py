# Generated by Django 5.0.1 on 2024-01-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cat',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='cat',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='cat',
            index=models.Index(fields=['-time_create'], name='cats_cat_time_cr_044b61_idx'),
        ),
    ]
