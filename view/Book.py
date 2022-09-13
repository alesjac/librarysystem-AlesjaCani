import csv
class Book:
    book_records='books.csv'
    def display_all_books(self):
        # book_records='books.csv'
        with open(self.book_records,"r") as file:
            reader = csv.reader(file)
            print("\nLIST OF BOOKS:\n")
            print("_________________________________")
            for row in reader:
                
                print("Book Title: ",row[0]) 
                print("Book Author: ",row[1]) 
                print("Book Price: ",row[2]) 
                print("Book Quantity: ",row[3]) 
                print("_________________________________")

    def getBookByAuthor(self):
        try:
            author = input("\nAuthor name: ")
            print("________________________")
            isAuthorCorrect = True
            book=[]
            #if user press enter immediately or a space
            if author=="" or author.isspace():
                isAuthorCorrect=False
            else:
                isAuthorCorrect=True
            if isAuthorCorrect == True:
                print("\nBOOKS of ",author,"\n")
                with open(self.book_records,"r") as file:
                    reader = csv.reader(file)
                    for row in reader:    
                        if row[2] == author:
                            print("Book Id: ",row[0])
                            print("Book Title: ",row[1]) 
                            print("Book Author: ",row[2]) 
                            print("Book Price: ",row[3]) 
                            print("Book Quantity: ",row[4]) 
                            print("_________________________________\n")
                            book.append(row)
                    
                    if(book==[]):
                        print("Author not found in database! Please try again!")
                        Book.getBookByAuthor(self)
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
            found=0
            reader = csv.reader(file)
            uprecord=[]
            for row in reader:
                if row[0]==id:
                    print("Book found: ", row)
                    row[1]=input("Enter new title: ")

                    print("Updated record: ",row )
                    found=1
                uprecord.append(row)
            if found == 0:
                print("Sorry! Record not found. \n\n")
                Book.updateBook(self)
                file.close()
            else:
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
                books.append(row)
            else:
                found = 1
        file.close()
        if found==0:
            print("Data not found")
        else:
            file=open(self.book_records,"w",newline='')
            writer=csv.writer(file)
            writer.writerows(books)
            print("Book is deleted")
            file.close()   



