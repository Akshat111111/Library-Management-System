# lib_oops.py
I created a practice OOPs based code (Central Library) which I made using CWH videos.(File type:Python py file)
class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks
        print("***Central Library***\n1)Showbooks\n2)Borrow Books\n3)Return Books\n4)Quit")

    def showBooks(self):
        
        for items in self.books:
            print(items)
    
    def borrowbooks(self,a):
        if a in self.books:
            print(f'{a} ,The book you wanted to issued,was issued')
            self.books.remove(a)
        else:
            print('Not there in library currently.Please check if font you entered matches exactly with Predefined books present in Library.')

    def returnbook(self,b):
        print(f'Thank you for returning:{b}book')
        self.books.append(b)
    

    def quit(self):
        return False


if __name__ == "__main__":
    while(True):
        centralLibrary = Library(['Physics','Chemistry','Math','Biology'])
        userinput = int(input("Enter a option :\n"))

        if userinput == 1:
            centralLibrary.showBooks()
        elif userinput == 2:
            a = input('Enter name of book you want to issue:\n')
            # try:
            #     int(a)
            # except Exception as e:
            #     print(e)
            centralLibrary.borrowbooks(a)
        elif userinput == 3:
            b = input('Enter name of book you want to return:\n')
            centralLibrary.returnbook(b)
        else:
            centralLibrary.quit()
