# Generated by Django 3.1.4 on 2022-12-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0015_auto_20221223_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='bewertung',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rezept',
            name='portionen',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
