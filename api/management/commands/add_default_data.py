import logging
import requests
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError

from api.models import Book, Author, ISBN

URL = "https://www.googleapis.com/books/v1/volumes?q=lion+intitle&maxResults=40"


class Command(BaseCommand):
    help = 'Add default books data'

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.truncate_database: bool = False

    def add_arguments(self, parser):
        parser.add_argument('--truncate-database', default=False, action="store_true",
                            help="Clean database before import")

    def handle(self, *args, **options):
        self.truncate_database = options.get('truncate_database')

        if self.truncate_database:
            Book.objects.all().delete()
            Author.objects.all().delete()
            ISBN.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('All data cleaned'))

        data: dict = requests.get(url=URL).json()

        for book_data in data['items']:
            id = book_data['id']
            try:  # TODO data is sometimes in format yyyy-mm-dd
                published_date = int(book_data['volumeInfo'].get('publishedDate', -1))
            except:
                published_date = -1
            title = book_data['volumeInfo'].get('title', None)
            page_count = int(book_data['volumeInfo'].get('pageCount', -1))
            book_cover_link = book_data['volumeInfo']['imageLinks'].get('thumbnail', None)
            publication_language = book_data['volumeInfo'].get('language', None)

            book, created = Book.objects.get_or_create(
                book_id=id,
                title=title,
                published_year=published_date,
                page_count=page_count,
                book_cover_link=book_cover_link,
                publication_language=publication_language
            )

            if not created:
                logging.log('Book exist')
            else:
                logging.info('Book created')
