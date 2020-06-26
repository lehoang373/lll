from django import forms
import django_filters
from .models import Lesson


class LessonFilter(django_filters.FilterSet):
    projectnumber__ = django_filters.CharFilter(lookup_expr='icontains')
    projectname__ = django_filters.CharFilter(lookup_expr='icontains')
    client__ = django_filters.CharFilter(lookup_expr='icontains')
    projectlocation__ = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    division = django_filters.CharFilter(lookup_expr='icontains')
    marketsector__ = django_filters.CharFilter(lookup_expr='icontains')
    discipline = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    memo__ = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lesson
        fields = [
                'projectnumber','projectname', 'client','projectlocation', 'description',
                'division','marketsector','discipline','author','memo',
        ]