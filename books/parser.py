from datetime import datetime
from typing import List


class BooksParser:
    def book_parser(self, data: dict) -> dict:
        published_date = self.date_parser(data["volumeInfo"].get("publishedDate", ""))

        image_links_data = data["volumeInfo"].get("imageLinks", "")
        if image_links_data:
            book_cover_link = (
                data["volumeInfo"].get("imageLinks", "").get("thumbnail", None)
            )
        else:
            book_cover_link = ""

        return {
            "book_id": data["id"],
            "published_date": published_date,
            "title": data["volumeInfo"].get("title", None),
            "page_count": int(data["volumeInfo"].get("pageCount", -1)),
            "book_cover_link": book_cover_link,
            "publication_language": data["volumeInfo"].get("language", None),
        }

    @staticmethod
    def authors_parser(data) -> List[str]:
        authors_list = list()
        authors_data = data["volumeInfo"].get("authors")

        if authors_data:
            for author in authors_data:
                authors_list.append(author)

            return authors_list

        return authors_list

    @staticmethod
    def industry_parser(data) -> List[dict]:
        industries_info = list()
        industry_data = data["volumeInfo"].get("industryIdentifiers")

        if industry_data:
            for industry in industry_data:
                industries_info.append(industry)
            return industries_info

        return industries_info

    @staticmethod
    def date_parser(text):
        for fmt in ("%Y-%m-%d", "%Y"):
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                pass

        return None
