from django.core.management.base import BaseCommand
from random_word import RandomWords

from api.importer import BooksImporter
from api.models import Book, Author, ISBN


class Command(BaseCommand):
    help = 'Add some default books data- used only in development'

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.truncate_database: bool = False
        self.random_word = RandomWords()

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

        # Return a single random word
        word = self.random_word.get_random_word()
        url = f'https://www.googleapis.com/books/v1/volumes?q={"None"}+intitle'
        print(word)

        BooksImporter(url).import_books()
