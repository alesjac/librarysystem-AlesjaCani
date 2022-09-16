import csv
from lib2to3.pytree import Base
from Book import *
from purchase import *
class AdminMenu:
    book = Book()
    puchase=Purchase()
    def startAdminMenu(self,user):
        try:
            print(f"\n« Welcome to Admin Menu {user[1]} » \n")
            print("Please write down the number to continue:")
            print("1- See all books")
            print("2- Display books by author name")
            print("3- Create a  book")
            print("4- Edit a book")
            print("5- Delete a book")
            print("6- List of purchases")
            print("7- Top 3 books sold")
            print("8- Log out\n")

            choice = int(input("Enter the number to continue: "))

            if choice ==1:
                self.book.display_all_books_admin()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==2:
                self.book.getBookByAuthor()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==3:
                self.book.createBook()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==4:
                self.book.updateBook()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==5:
                self.book.deleteBook()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==6:
                self.puchase.allPurchases()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==7:
                self.puchase.top3soldBooks()
                AdminMenu.startAdminMenu(self,user)
            elif choice ==8:
                print("You have been successfully logged out. See you next time!")
            else:
                print("Please enter ONLY values from 1 -8. Try again!")
                AdminMenu.startAdminMenu(self,user)
                         
        except(BaseException):
            print("Please enter ONLY values from 1 -8. Try again!")
            AdminMenu.startAdminMenu(self,user)
  
