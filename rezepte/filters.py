import django_filters
from .models import *

override = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             }
         }

class RezeptFilter(django_filters.FilterSet):
    class Meta:
        model = Rezept
        fields = {
            'bezeichnung': ['contains'],
            'kategorie': ['contains'],
            'kueche': ['contains'],
            'art_zutaten': ['contains']
            }
        filter_overrides = override
