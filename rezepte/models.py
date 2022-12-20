from django.db import models
from django.urls import reverse

# Create your models here.
class Speisenart(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Speisenarten"

    def __str__(self):
       return self.name

class Rezept(models.Model):
    koch = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bezeichnung = models.CharField(max_length=80)
    #kategorie = models.CharField(max_length=80)
    kategorie = models.ForeignKey(Speisenart, on_delete=models.CASCADE)
    kueche = models.CharField(max_length=80, blank=True)
    art_zutaten = models.CharField(max_length=80, blank=True)
    portionen = models.IntegerField(blank=True, null=True)
    bewertung = models.IntegerField(blank=True, null=True)
    zutaten = models.TextField()
    zubereitung = models.TextField(blank=True)
    anmerkungen = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "rezepte"

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse('redetail', args=[str(self.id)])