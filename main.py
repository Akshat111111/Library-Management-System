class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks
        print("***Central Library***\n1)Showbooks\n2)Borrow Books\n3)Return Books\n4)Quit")

    def showBooks(self):
        for item in self.books:
            print(item)

    def borrowBooks(self, book):
        if book in self.books:
            print(f"The book '{book}' you wanted to borrow has been issued.")
            self.books.remove(book)
        else:
            print("The book is not currently available in the library. Please check if the book is spelled correctly.")

    def returnBook(self, book):
        print(f"Thank you for returning the book: {book}")
        self.books.append(book)

    def quit(self):
        return False


if __name__ == "__main__":
    centralLibrary = Library(['Physics', 'Chemistry', 'Math', 'Biology'])
    while True:
        userinput = int(input("Enter an option: "))
        if userinput == 1:
            centralLibrary.showBooks()
        elif userinput == 2:
            book = input("Enter the name of the book you want to borrow: ")
            centralLibrary.borrowBooks(book)
        elif userinput == 3:
            book = input("Enter the name of the book you want to return: ")
            centralLibrary.returnBook(book)
        elif userinput == 4:
            break  # Break the while loop and exit the program
        else:
            print("Invalid input. Please enter a valid option.")

