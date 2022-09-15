import csv
from lib2to3.pytree import Base
from Book import *
from datetime import datetime
from User import *
from statistics import mode
from operator import itemgetter

class Purchase:

    # user_records='users.csv'
    purchase_records='purchase.csv'
    book=Book()
    user=User()

    # def getUserbyUsername(self,username):
    #     print("------------------------\n")
    #     user=[]
    #     with open(self.user_records,"r") as file:
    #         reader = csv.reader(file)
    #         for row in reader:    
    #             if row[0] == username:
    #                 user.append(row)
    #     return user

    def purchaseBook(self,user):
        try:
            # user = Purchase.getUserbyUsername(self,"ilseacani")
            print("--------------------------------------")
            print(F"MAKE A PURCHASE SECTION FOR {user[1]}")
            print("--------------------------------------")

            print("There is a list of books you may look before deciding what to buy\n")
            self.book.display_all_books()
            bookExists = False
            print(f"\n------Enter the Purchase details below to place an order {user[0][1]}------")
            purchase=[]
            bookToBuy=[]

            #first value
            buyer_id=user[0][0]
            purchase.append(buyer_id)

            #second and third values 

            # require from user to put values for fields name except ID, which is automatically added
            required_details=['Book id','Quantity']
            value_of_req_details=[]
            quantityToBuy=''
            for i in range(0,2):
                value=input("Enter "+ required_details[i] + ": ")
                if value == "" or value.isspace():
                    self.correctValue=False
                    break
                else:
                    self.correctValue=True
                    value_of_req_details.append(value)


            if self.correctValue == True:
                print("")
                book = self.book.getBookById(value_of_req_details[0])
                if book == []:
                    print("This book does not exists. Try a different id.")
                    Purchase.purchaseBook(self)
                    # raise BookDoesNotExists("This book does not exists. Try a different id.")
                else:
                    purchase.append(value_of_req_details[0])
                    bookToBuy=book

                    if int(value_of_req_details[1])>0 and int(value_of_req_details[1])<=int(bookToBuy[0][4]):
                        purchase.append(int(value_of_req_details[1]))
                        quantityToBuy = int(value_of_req_details[1])
                        # other values
                        #data calculated within code
                        # book = self.book.getBookById(value[0])
                        self.book.changeQuantityOfBook(book,quantityToBuy)
                        totalprice = quantityToBuy * int(book[0][3])
                        purchase.append(totalprice)
                        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        purchase.append(date)


                        #add purchase in file
                        with open(self.purchase_records,"a",encoding="utf-8") as file:
                            writer = csv.writer(file)
                            writer.writerows([purchase])

                        print(f"Successfully made a purchase '{bookToBuy[0][1]} - {bookToBuy[0][2]}'!\n Enter nr 3 to view all your purchases.")
                    else:
                        print(f"\nWe have only {int(bookToBuy[0][4])} books left. Please try again!")
                        Purchase.purchaseBook(self)
            else:
                print("Incorrect input data. Please try again.")
                Purchase.purchaseBook(self)
        
    
        except(BaseException):
            print("Error!")


    # def getPurchaseByUserId(self,username):
    #     print("------------------------\n")
    #     purchaseByUser=[]
    #     with open(self.purchase_records,"r") as file:
    #         reader = csv.reader(file)
    #         for row in reader:    
    #             if row[0] == username:
    #                 purchaseByUser.append(row)
    #     return purchaseByUser


    def displayPurchaseOfUser(self,userLogin):
        print("\n--------------------------------------")
        print(F"LIST OF PURCHASES FOR {userLogin[1]}")
        print("--------------------------------------")
        user = self.user.getUserbyUsername(self,userLogin[0])
        # purchaseOfUser = Purchase.getPurchaseByUserId(self,"ilseacani")
        # print(purchaseOfUser)
        hasPurchased=True
        with open(self.purchase_records,"r") as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==user[0][0]:
                    print(f"Book Title: {row[1]} --- Book Author {row[2]} --- Book Price {row[3]} --- Quantity purchased: {row[4]} --- Total price: {row[5]} --- Date: {row[6]} \n") 
                    hasPurchased=True
                else:
                    hasPurchased=False
                    
        if(hasPurchased==False):
            print("No books purchased.")

#methods for top 3 sold books START
    def getBookAndQuantity(self):
        purchases=[]
        with open(self.purchase_records,"r") as file:
            reader = csv.reader(file)
            for row in reader:    
                purchases.append(row)
        booksandquantity=[]
        for i in range(1,len(purchases)):
            booquantity=[]
            booquantity.append(purchases[i][1])
            booquantity.append(int(purchases[i][4]))
            booksandquantity.append(booquantity)
        return booksandquantity

    def frequentBook(self,bookAndQuantity):

        first_frequent_book_found=""

        titles_of_frequent_book=[]

        frequent_book_list=[]

        total_quantity_of_freq_book=0

    

        for i in range(0,len(bookAndQuantity)):

            titles_of_frequent_book.append(bookAndQuantity[i][0])

        first_frequent_book_found = mode(titles_of_frequent_book)

    

        for i in range(0,len(bookAndQuantity)):

            if(bookAndQuantity[i][0]==first_frequent_book_found):

                frequent_book_list.append(bookAndQuantity[i])

    

        for i in range(0,len(frequent_book_list)):

            total_quantity_of_freq_book += frequent_book_list[i][1]

    

        final_first_book=[]

        final_first_book.append(first_frequent_book_found)

        final_first_book.append(total_quantity_of_freq_book)


        return final_first_book
    
    def newListOfBookAndQuantity(self,bookandquantity,bookTitle):
        newList=[]
        for i in range(0,len(bookandquantity)):
            if(bookandquantity[i][0]!=bookTitle):
                newList.append(bookandquantity[i])
        return newList
    
    def top3soldBooks(self):

        try:
            print("\n--------------------------------------")
            print("TOP 3 SOLD BOOKS")
            print("----------------------------------------\n")
            bookAndQuantity = Purchase.getBookAndQuantity(self)
            if len(bookAndQuantity)>=3:

                first_book = Purchase.frequentBook(self,bookAndQuantity)
                newListBQ1=Purchase.newListOfBookAndQuantity(self,bookAndQuantity,first_book[0])

                second_book=Purchase.frequentBook(self,newListBQ1)
                newListBQ2=Purchase.newListOfBookAndQuantity(self,newListBQ1,second_book[0])

                third_book=Purchase.frequentBook(self,newListBQ2)
                
                all3books=[]
                all3books.append(first_book)
                all3books.append(second_book)
                all3books.append(third_book)
            
                final = sorted(all3books,key=itemgetter(1),reverse=True)
                print(f"First book: {final[0][0]}. Total amount sold {final[0][1]} ")
                print(f"Second book: {final[1][0]}. Total amount sold {final[1][1]} ")
                print(f"Third book: {final[2][0]}. Total amount sold {final[2][1]} ")
            else:
                print("\nYou have less than 3 books sold until now.\nCheck List of purchases nr 6.")
        except(BaseException):
            print("\nXXX Something went wrong. Try again! XXX")

    #methods for top 3 sold books END


    def allPurchases(self):
        try:
            print("\n--------------------------------------")
            print("LIST OF ALL PURCHASES")
            print("----------------------------------------\n")
            # anyPurchase=True
            with open(self.purchase_records,"r") as file:
                reader=csv.reader(file)
                next(file)
                for row in reader:
                    
                    user = self.user.getUserbyUsername(self,row[0])
                    print(f"Book purchased by {user[0][1]}")
                    print(f"Book Title: {row[1]} --- Book Author {row[2]} --- Book Price {row[3]} --- Quantity purchased: {row[4]} --- Total price: {row[5]} --- Date: {row[6]} \n") 
                    anyPurchase=True
                    
            if anyPurchase == False:
                print("There is no purchase yet.\n\n")
        except(BaseException):
            print("There is no purchase yet.\n\n")