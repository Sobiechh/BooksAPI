from rest_framework import serializers

from .models import Book, Author, ISBN


class IsbnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ISBN
        fields = (
            'isbn_id',
            'book',
        )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
        )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.HyperlinkedRelatedField(many=True, view_name='author-detail', queryset=Author.objects.all())
    isbns = IsbnSerializer(read_only=True, many=True, source='isbn_set')

    class Meta:
        model = Book
        fields = (
            'book_id',
            'title',
            'authors',
            'published_date',
            'page_count',
            'book_cover_link',
            'publication_language',
            'isbns',
        )
