import csv
# from AdminMenu import *
class Book:
    book_records='books.csv'
    # adminMenu = AdminMenu()
    def display_all_books(self):
        with open(self.book_records,"r") as file:
            reader = csv.reader(file)
            print("\nLIST OF BOOKS:")
            print("----------------")
            next(file)
            for row in reader:
                if int(row[4])>0:
                    print(f"Book Id: {row[0]} --- Book Title: {row[1]} --- Book Author: {row[2]} --- Book Price: {row[3]} --- Book Quantity: {row[4]} \n") 

            
    def getBookByAuthor(self):
        try:
            print("--------------------------------------")
            print("Search book by author name")
            print("--------------------------------------")

            author = input("\nAuthor name: ")
            print("-------------------")
            isAuthorCorrect = True
            book=[]

            #if user press enter immediately or a space
            if author=="" or author.isspace():
                isAuthorCorrect=False
            else:
                isAuthorCorrect=True

            #if user inputs correct values (not spaces )
            if isAuthorCorrect == True:
                print("\nBOOKS of ",author,"\n")

                #read records
                with open(self.book_records,"r") as file:
                    reader = csv.reader(file)
                    for row in reader:    

                        #get only the books with the author name entered by user
                        if row[2] == author:
                            print("Book Id: ",row[0])
                            print("Book Title: ",row[1]) 
                            print("Book Author: ",row[2]) 
                            print("Book Price: ",row[3]) 
                            print("Book Quantity: ",row[4]) 
                            print("_________________________________\n")
                            book.append(row)

                    # if book is not found with the author name
                    if(book==[]):
                        print("Author not found in database! Please try again!")
                        Book.getBookByAuthor(self)
            
            # if user inputs incorrect values -> isAuthorCorrect == False:
            else:
                print("Enter correct values. Try again!")
                Book.getBookByAuthor(self)

        except(BaseException):
            print("xxx Error ! Please try again!")
            Book.getBookByAuthor(self)

    def createBook(self):
        try:
            print("--------------------------------------")
            print("Create book section")
            print("--------------------------------------")


            rec_fields = ['id','title','author','price','quantity']
            books=[]
            bookExists=False
            lastId=0
            correctValue=True


             #automatically add id when book is created
            values=[]
            for row in Book.all_books(self):
                if len(row)>0:
                    values.append(int(row[0]))
            lastId=max(values)
            books.append(lastId+1)
            
            # require from user to put values for fields name except ID, which is automatically added
            for i in range(1,len(rec_fields)):
                value=input("Enter "+ rec_fields[i] + ": ")

                if value == "" or value.isspace():
                    self.correctValue =False
                    break
                else:
                    self.correctValue=True
                    
                    #add values entered by user
                    books.append(value)
               
            if self.correctValue == True:
                
                #if book exists
                for rows in Book.all_books(self):
                    if rows[1] == books[1]:
                        bookExists = True
            

                if bookExists == False:
                   
                    # add book in books.csv
                    with open(self.book_records,"a",encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerows([books])

                    print("Successfully created a book")  

                if bookExists == True:
                    print("Book exists! Try again.")
                    Book.createBook(self)
            else:
                print("Enter correct values. Try again!")
                Book.createBook(self)

        except(BaseException):
            print("Error occured. Try again")
            Book.createBook(self)
       
    
    #return all books from the books.csv file
    def all_books(self):  
        
        books=[]
        with open(self.book_records,"r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:    
                    books.append(row)
            return books
    


    def updateBook(self):
        print("--------------------------------------")
        print("Update book section")
        print("--------------------------------------")
        
        
        try:
            Book.display_all_books(self)
            print("----------------------------------\n")
            file = open(self.book_records,"r")
            id = input("Enter id book to update: ")
            found=False
            reader = csv.reader(file)
            uprecord=[]
            for row in reader:
                #update the wanted book
                if row[0]==id:
                    print("Book found: ", row)
                    row[1]=input("Enter new title: ")
                    row[2]=input("Enter new author: ")
                    row[3]=input("Enter new price: ")
                    row[4]=input("Enter new quantity: ")

                    print("Updated record: ",row )
                    found=True
                uprecord.append(row)

            if found == False:
                print("Sorry! Record not found. \n\n")
                Book.updateBook(self)
                file.close()
            else:
                #update the whole file
                file=open(self.book_records,"w",encoding="utf-8",newline='')
                writer = csv.writer(file)
                writer.writerows(uprecord)
                print("You record is successfully updated.")
                file.close()
    
        except(BaseException):
            print("Error. Try again")
            # Book.createBook(self)


    def deleteBook(self):
        file = open(self.book_records,"r")
        reader = csv.reader(file)
        id=input("Enter the book id you want to delete: ")
        found=0
        books=[]

        for row in reader:
            if row[0]!=id:
                #get all books except the one with the bookid user entered to delete
                books.append(row)
            else:
                found = 1
        file.close()
        if found==0:
            print("Data not found")
        else:
            #update the file without the deleted book
            file=open(self.book_records,"w",newline='')
            writer=csv.writer(file)
            writer.writerows(books)
            print("Book is deleted")
            file.close()   


    def getBookById(self,id):
        try:
            book=[]
            with open(self.book_records,"r") as file:
                reader = csv.reader(file)
                for row in reader:    
                    if row[0] == id:
                        book.append(row)
                    
            return book
        except:
            print("Error occured! Try again.")
    
    def changeQuantityOfBook(self,book,number):
        try:
            file = open(self.book_records,"r")
            reader = csv.reader(file)
            updated_list=[]
            for row in reader:
                if row[0]==book[0][0]:
                    quantityofBook = int(book[0][4])
                    quantityofBook-=number
                    row[4]=str(quantityofBook)
                updated_list.append(row)
            file=open(self.book_records,"w",encoding="utf-8",newline='')
            writer = csv.writer(file)
            writer.writerows(updated_list)
            file.close()
            print("success - quantity changed")
    
        except(BaseException):
            print("Error. Try again")
            # Book.createBook(self)
