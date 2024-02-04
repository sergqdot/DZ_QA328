# задача :
# Класс Книга должен содержать информацию о названии, авторе и жанре книги
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


my_book = Book(title='Лабиринт отражений', author='Сергей Лукьяненко', genre='Фантастика')
print(f'Моя книга: Название - {my_book.title}, Автор - {my_book.author}, Жанр - {my_book.genre}.')

