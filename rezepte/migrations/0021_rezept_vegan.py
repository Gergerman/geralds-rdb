# Generated by Django 3.1.4 on 2023-01-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0020_auto_20230122_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezept',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
    ]