from pprint import pprint

import requests

from api.models import Book, Author, ISBN
from books.parser import BooksParser


class BooksImporter:
    def __init__(self, url):
        self.url = url
        self.step = 40

    def import_books(self):
        raw_request: dict = self.get_url_request(self.url)

        for start_index in self.get_start_index(raw_request):
            url = self.url + f'&maxResults={self.step}&startIndex={start_index}'
            request = self.get_url_request(url)

            items = request.get('items')
            if not items:
                return

            for book_data in items:
                book_info = BooksParser().book_parser(book_data)

                book, created_book = Book.objects.get_or_create(
                    book_id=book_info['book_id'],
                    title=book_info['title'],
                    published_date=book_info['published_date'],
                    page_count=book_info['page_count'],
                    book_cover_link=book_info['book_cover_link'],
                    publication_language=book_info['publication_language']
                )

                for author_name in BooksParser().authors_parser(book_data):
                    author, created_author = Author.objects.get_or_create(
                        name=author_name
                    )
                    book.authors.add(author)

                for industry in BooksParser().industry_parser(book_data):
                    isbn, created_isbn = ISBN.objects.get_or_create(
                        isbn_id=industry.get('identifier'),
                        book=book
                    )
                    isbn.save()

                book.save()

            if start_index > 1:
                pprint(f'{start_index} books downloaded')

    @staticmethod
    def get_url_request(url: str) -> dict:
        return requests.get(url=url).json()

    def get_start_index(self, request):
        items_count = request['totalItems']

        for index in range(1, items_count, self.step - 1):
            yield index - 1
