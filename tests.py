import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.mark.parametrize(
        'book',
        [
            '',
            'Удивительная история Бенджамина Баттона, часть 2'
        ]
    )
    def test_add_new_book_name_len(self, book, books_collection):
        books_collection.add_new_book(book)
        assert len(books_collection.get_books_genre()) == 0

    

    def test_set_book_genre_exists_genre_true(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert books_collection.get_book_genre(book) == genre
        
        
    def test_set_book_genre_exists_genre_false(self, books_collection):
        book = 'Том Сойер'
        genre = 'Документальный'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert books_collection.get_book_genre(book) == ''
        
        
    def test_get_book_genre_true(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert books_collection.get_book_genre(book) == genre
        
        
    def test_get_books_with_specific_genre_books_exists_true(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert len(books_collection.get_books_with_specific_genre(genre)) == 1
        
        
    def test_get_books_with_specific_genre_books_not_exists_false(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert len(books_collection.get_books_with_specific_genre('Ужасы')) == 0
        
        
    def test_get_books_with_specific_genre_genre_not_exists_false(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert len(books_collection.get_books_with_specific_genre('Докуменитальный')) == 0
        
        
    def test_get_books_genre_true(self, books_collection):
        books_collection.add_new_book('Том Сойер')
        books_collection.add_new_book('Мэри Поппинс')
        
        assert len(books_collection.get_books_genre()) == 2
        
        
    def test_get_books_for_children_genre_not_age_rating_true(self, books_collection):
        book = 'Том Сойер'
        genre = 'Фантастика'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert book in books_collection.get_books_for_children()
        
        
    def test_get_books_for_children_genre_age_rating_false(self, books_collection):
        book = 'Том Сойер'
        genre = 'Ужасы'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        
        assert len(books_collection.get_books_for_children()) == 0
        
        
    def test_add_book_in_favorites_book_exists_in_library_success(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        
        assert book in books_collection.get_list_of_favorites_books()
        
        
    def test_add_book_in_favorites_add_exists_in_favorites_book_failed(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.add_book_in_favorites(book)
        
        assert len(books_collection.get_list_of_favorites_books()) == 1
        
        
    def test_add_book_in_favorites_add_book_not_exists_in_library_failed(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_book_in_favorites(book)
        
        assert len(books_collection.get_list_of_favorites_books()) == 0
    
    
    def test_delete_book_from_favorites_book_exists_in_favorites_success(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.delete_book_from_favorites(book)
        
        assert book not in books_collection.get_list_of_favorites_books()
        
        
    def test_delete_book_from_favorites_book_not_exists_in_favorites_failed(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.delete_book_from_favorites('Мэри Поппинс')
        
        assert len(books_collection.get_list_of_favorites_books()) == 1
        

    def test_get_list_of_favorites_books_true(self, books_collection):
        book = 'Том Сойер'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        
        assert len(books_collection.get_list_of_favorites_books()) == 1
        