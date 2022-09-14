import csv
from Book import *
from datetime import datetime
class Purchase:

    user_records='users.csv'
    purchase_records='purchase.csv'
    book=Book()

    def getUserbyUsername(self,username):
        print("------------------------\n")
        user=[]
        with open(self.user_records,"r") as file:
            reader = csv.reader(file)
            for row in reader:    
                if row[0] == username:
                    user.append(row)
        return user

    def purchaseBook(self):
        try:
            user = Purchase.getUserbyUsername(self,"ilseacani")

            print("There is a list of books you may look before deciding what to buy\n")
            self.book.display_all_books()
            bookExists = False
            print(f"------Enter the Purchase details below to place an order {user[0][1]}------")
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

                        print("Successfully created a book")
                    else:
                        print(f"We have only {int(bookToBuy[0][4])} books left. Please try again!")
                        Purchase.purchaseBook(self)
            else:
                print("Incorrect input data. Please try again.")
                Purchase.purchaseBook(self)
        

        except(BaseException):
            print("Error!")
