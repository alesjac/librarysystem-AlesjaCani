import csv
from AdminMenu import *
from BuyerMenu import *
class Login:
    adminMenu =  AdminMenu()
    buyerMenu = BuyerMenu()

    def start(self):
        try: 
            print(" ~ Welcome everybody to Library Project by ALESJA CANI! :) ~ \n")
            print("------------------------------------------------------------")
            print("LOGIN PAGE\n")
            print("Please enter your credentials to login\n\n")

            user_records='users.csv'

            username = input("Enter the username: ")
            password = input("Enter the password: ")
            isCredentialsCorrect = False
            ifUserExits = False
            role =""
            fullname=""
            user=[]
            

            with open(user_records,"r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == username and row[2] == password:
                        isCredentialsCorrect = True
                        # role = row[3]
                        # fullname = row[1]
                        user=row
                        

                    if row[0] == username or row[2] == password:
                        ifUserExits = True

                    
                    
            if isCredentialsCorrect == True and user[3] == "Admin":
                print("Logged in ADMIN")
                self.adminMenu.startAdminMenu(user)

            elif isCredentialsCorrect == True and user[3] == "Buyer":
                print("logged in BUYER ")
                self.buyerMenu.startBuyerMenu(user)
            else:
                if ifUserExits == True:
                    print("\n xxx-> Wrong username or password.Please try again. <-xxx \n")
                    Login.start()
                else:
                    print("\n xxx -> User does not exists. Please try again. <- xxx\n")
                    Login.start()
        except(BaseException):
            Login.start(self)

login=Login()
login.start()

            
            

            