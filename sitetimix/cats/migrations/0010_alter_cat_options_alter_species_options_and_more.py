# Generated by Django 5.0.1 on 2024-01-23 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0009_owner_cat_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cat',
            options={'ordering': ['-time_create'], 'verbose_name': 'Котик', 'verbose_name_plural': 'Котики'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'verbose_name': 'Порода', 'verbose_name_plural': 'Породы'},
        ),
        migrations.AlterField(
            model_name='cat',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='is_published',
            field=models.IntegerField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cats.owner', verbose_name='Хозяин'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='cats.species', verbose_name='Породы'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='cats.tagpost', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Породы'),
        ),
    ]
