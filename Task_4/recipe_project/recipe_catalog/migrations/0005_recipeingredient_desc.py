# Generated by Django 4.2.16 on 2024-11-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0004_recipeingredient_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]
