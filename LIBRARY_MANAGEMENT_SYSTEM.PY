# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library object using this Library class and show how you can print all books,
#   add a book and get the number of books using different methods. 
#   Show that your program doesn’t persist the books after the program is stopped!



class Library:
    def __init__ (self , no_books,books1):
        self.nobooks = no_books
        self.book = books1


    def showbooks(self):
            print(self.book)


    def addbook(self,book1):
            self.book.append(book1)
            self.nobooks +=1


    def countbook(self,no_books):
            print((self.nobooks))


library = Library(3,["python" , 'hindi' , "sanskrit" ])
library.showbooks
library.addbook("DSA")
library.countbook



    
