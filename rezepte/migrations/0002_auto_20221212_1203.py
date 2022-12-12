# Generated by Django 3.1.4 on 2022-12-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rezept',
            options={'verbose_name_plural': 'rezepte'},
        ),
        migrations.AddField(
            model_name='rezept',
            name='anmerkungen',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rezept',
            name='art_zutaten',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rezept',
            name='bewertung',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rezept',
            name='kueche',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rezept',
            name='portionen',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
