# Generated by Django 3.1.4 on 2022-12-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0010_auto_20221222_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='kueche',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
