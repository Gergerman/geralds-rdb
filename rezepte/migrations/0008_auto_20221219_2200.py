# Generated by Django 3.1.4 on 2022-12-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0007_auto_20221219_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='kategorie',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]