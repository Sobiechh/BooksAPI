from django import forms
from django_filters import FilterSet, DateFilter

from api.models import Book


class BookFilter(FilterSet):
    date_input = forms.DateInput(
        attrs={
            "type": "date",
        }
    )
    start_date = DateFilter(
        field_name="published_date",
        label="From: ",
        lookup_expr="gte",
        widget=date_input,
    )
    end_date = DateFilter(
        field_name="published_date", label="To: ", lookup_expr="lte", widget=date_input
    )

    class Meta:
        model = Book
        fields = (
            "title",
            "authors",
        )
