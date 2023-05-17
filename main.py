# lib_oops.py

class Library:
    def __init__(self, books):
        self._books = books
        self._options = {
            1: self._displayBooks,
            2: self._issueBook,
            3: self._returnBook,
            4: self.quit,
            5: self.addBook,
            6: self.removeBook
        }
        self._menu()

    def _menu(self):
        print("***Central Library***")
        print("1) Show books")
        print("2) Borrow books")
        print("3) Return books")
        print("4) Quit")
        print("5) Add book")
        print("6) Remove book")

    def _displayBooks(self):
        for book in self._books:
            print(book)

    def _issueBook(self):
        book = input('Enter the name of the book you want to issue: ')
        if book in self._books:
            print(f'{book}, the book you wanted to issue, was issued')
            self._books.remove(book)
        else:
            print('The book is not available in the library.')

    def _returnBook(self):
        book = input('Enter the name of the book you want to return: ')
        print(f'Thank you for returning: {book} book')
        self._books.append(book)

    def addBook(self):
        book = input('Enter the name of the book you want to add: ')
        self._books.append(book)
        print(f'{book} book has been added to the library.')

    def removeBook(self):
        book = input('Enter the name of the book you want to remove: ')
        if book in self._books:
            self._books.remove(book)
            print(f'{book} book has been removed from the library.')
        else:
            print(f'{book} book is not available in the library.')

    def quit(self):
        return False


if __name__ == "__main__":
    books = ['Physics', 'Chemistry', 'Math', 'Biology']
    centralLibrary = Library(books)

    while True:
        userinput = int(input("Enter an option: "))

        if userinput in centralLibrary._options:
            if userinput == 4:
                if centralLibrary.quit():
                    break
            else:
                centralLibrary._options[userinput]()
        else:
            print('Invalid input, please try again.')

