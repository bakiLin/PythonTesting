# Generated by Django 4.2.16 on 2024-12-12 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0007_recipe_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
    ]