from books.models import Book
from books.serializers import BookModelSerializer
import requests


def fetch_from_open_library(isbn: str) -> dict:
    """
    Fetch book details from Open Library using ISBN.
    Returns a dict formatted for the Book model.

    Args:
        isbn (str): ISBN number of the book.

    Returns:
        dict: {
            "title": str,
            "author": str,
            "pages": int | None,
            "isbn": str,
            "short_description": str,
            "publisher": str,
            "source": str
        }
    """
    base_url = f"https://openlibrary.org/isbn/{isbn}.json"
    source_url = f"https://openlibrary.org/isbn/{isbn}"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        book_data = response.json()

        # Title
        title = book_data.get("title", "Unknown Title")

        # Number of pages
        pages = book_data.get("number_of_pages")

        # Description
        desc = book_data.get("description")
        if isinstance(desc, dict):
            short_description = desc.get("value", "No description available.")
        elif isinstance(desc, str):
            short_description = desc
        else:
            short_description = "No description available."

        # Author
        author_name = "Unknown Author"
        authors = book_data.get("authors", [])
        if authors:
            author_key = authors[0].get("key")
            if author_key:
                author_url = f"https://openlibrary.org{author_key}.json"
                author_resp = requests.get(author_url)
                if author_resp.status_code == 200:
                    author_name = author_resp.json().get("name", "Unknown Author")

        # Publisher
        publishers = book_data.get("publishers", [])
        publisher_name = publishers[0] if publishers else "Unknown Publisher"

        return {
            "title": title,
            "author": author_name,
            "pages": pages,
            "isbn": isbn,
            "short_description": short_description,
            "publisher": publisher_name,
            "source": source_url,
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}


def handle_search_isbn(isbn: str) -> tuple[bool, dict]:
    """
    Fetch book details by ISBN.

    Workflow:
    1. Search in local database.
    2. If not found, query Open Library API.
    3. If found, store the retrieved data in the database.
    4. Return a response containing:
       - found_status (bool): whether the book was found
       - data (dict): book details (title, authors, publishers, publish date, etc.)
    """
    books = Book.objects.filter(isbn=isbn)
    if books.exists():
        book = books.first()
        serializer = BookModelSerializer(book)
        return True, serializer.data

    data = fetch_from_open_library(isbn)
    if data:
        serializer = BookModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return True, serializer.data
    return False, {}
