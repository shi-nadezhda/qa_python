import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    return BooksCollector()
