# Generated by Django 3.1.4 on 2023-01-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0021_rezept_vegan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='art_zutaten',
            field=models.CharField(blank=True, choices=[('Fleisch', 'Fleisch'), ('Schwein', 'Schwein'), ('Rind', 'Rind'), ('Lamm', 'Lamm'), ('Huhn, Geflügel', 'Huhn, Geflügel'), ('Wild', 'Wild'), ('Pasta', 'Pasta'), ('Gemüse', 'Gemüse'), ('Obst', 'Obst'), ('Reis, Getreide', 'Reis, Getreide'), ('Mehlspeise', 'Mehlspeise'), ('Fisch, Meeresfrüchte', 'Fisch, Meeresfrüchte'), ('-----', '-----------')], max_length=80),
        ),
        migrations.AlterField(
            model_name='rezept',
            name='bezeichnung',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='rezept',
            name='kueche',
            field=models.CharField(blank=True, choices=[('international', 'international'), ('österreichisch', 'österreichisch'), ('italienisch', 'italienisch'), ('thailändisch', 'thailändisch'), ('chinesisch', 'chinesisch'), ('französisch', 'französisch'), ('spanisch', 'spanisch'), ('japanisch', 'japanisch'), ('---------', '---------')], max_length=80),
        ),
    ]