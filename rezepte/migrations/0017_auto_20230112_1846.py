# Generated by Django 3.1.4 on 2023-01-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0016_auto_20221225_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='art_zutaten',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='rezept',
            name='kategorie',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='rezept',
            name='kueche',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.DeleteModel(
            name='Kueche',
        ),
        migrations.DeleteModel(
            name='Speisenart',
        ),
        migrations.DeleteModel(
            name='Zutatenart',
        ),
    ]
