# Generated by Django 5.0.1 on 2024-01-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_tagpost_alter_cat_spec_cat_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='cat',
            new_name='tags',
        ),
    ]