# qa_python
1. test_add_new_book_add_two_books - проверка на возможность добавления двух книг
2. test_add_new_book_name_len - параметризированная проверка на возможность добавления книги с именем нулевой длины и длиной более 41 символа
3. test_set_book_genre_exists_genre_true - установка книге жанра, существующенго в списке
4. test_set_book_genre_exists_genre_false - жанр, не существующий в списке, книге не устанавливается
5. test_get_book_genre_true - проверка успешного получения книги по жанру
6. test_get_books_with_specific_genre_books_exists_true - проверка удачного получения книги определенного жанра, которая существует в библиотеке
7. test_get_books_with_specific_genre_books_not_exists_false - проверка не удачного получения книги определенного жанра, которой нет в библиотеке
8. test_get_books_with_specific_genre_genre_not_exists_false - проверка неудачного получения книги по жанру, которого нет в библиотеке
9. test_get_books_genre_true - проверка удачного пролучения списка книг
10. test_get_books_for_children_genre_not_age_rating_true - проверка удачного получения списка книг, которые не находятся в списке ограничения по возрастному рейтингу
11. test_get_books_for_children_genre_age_rating_false - проверка неудачного получения списка книг, которые находятся в списке ограничения по возрастному рейтингу
12. test_add_book_in_favorites_book_exists_in_library_success - проверка удачного добавления в избранное книги, которая находится в библиотеке
13. test_add_book_in_favorites_add_exists_in_favorites_book_failed - проверка не удачного повторного добавления в избранное книги, которая уже есть в избранном 
14. test_add_book_in_favorites_add_book_not_exists_in_library_failed -  проверка неудачного добавления в избранное книги, которой нет в библиотеке
15. test_delete_book_from_favorites_book_exists_in_favorites_success - проверка на удачное удаление книги из избранного
16. test_delete_book_from_favorites_book_not_exists_in_favorites_failed - проверка на неудачное удаление книги, не существующей в избранном
17. test_get_list_of_favorites_books_true - проверка удачного получения списка избранных книг
