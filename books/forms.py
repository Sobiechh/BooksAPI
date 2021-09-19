from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

from api.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'published_date': DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }

    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')

        if not published_date:
            raise ValidationError('Fill this field')

        if published_date > date.today():
            raise ValidationError('How can you predict the future?')

        return published_date

    def clean_page_count(self):
        page_count = self.cleaned_data.get('page_count')

        if not page_count:
            raise ValidationError('Fill this field')

        return page_count
