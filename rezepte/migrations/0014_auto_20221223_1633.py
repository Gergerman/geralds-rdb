# Generated by Django 3.1.4 on 2022-12-23 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0013_auto_20221223_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezept',
            name='kueche',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rezepte.kueche'),
        ),
    ]