import django_filters.rest_framework as django_filter

from .models import Book


class BookFilter(django_filter.FilterSet):
    authors = django_filter.CharFilter(
        field_name='authors__name',
        lookup_expr='contains',
    )
    start_date = django_filter.DateFilter(field_name='published_date', lookup_expr='gte')
    end_date = django_filter.DateFilter(field_name='published_date', lookup_expr='lte')

    class Meta:
        model = Book
        filter_backends = (django_filter.DjangoFilterBackend,)
        fields = (
            'title',
            'publication_language',
        )
