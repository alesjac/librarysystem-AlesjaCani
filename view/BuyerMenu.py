from Book import *
from purchase import *
class BuyerMenu:
    book=Book()
    purchase = Purchase()
    def startBuyerMenu(self,user):
        try:
            print(f"\n« Welcome to Buyer Menu {user[1]} »\n")
            print("Please write down the number to continue:")
            print("1- See available books")
            print("2- Make a purchase")
            print("3- View my purchases")
            print("4- Log out")

            choice = int(input("Enter the number to continue: "))

            if choice ==1:
                self.book.display_all_books()
                BuyerMenu.startBuyerMenu(self,user)
            elif choice ==2:
                self.purchase.purchaseBook(user)
                BuyerMenu.startBuyerMenu(self,user)
                print('')
            elif choice ==3:
                self.purchase.displayPurchaseOfUser(user)
                BuyerMenu.startBuyerMenu(self,user)
            elif choice ==4:
                print("You have been successfully logged out. See you next time!")
            else:
                print("Please enter ONLY values from 1 -3. Try again!")
                BuyerMenu.startBuyerMenu(self,user)
        
        except(BaseException):
            print("Please enter ONLY values from 1 -3. Try again!")
            BuyerMenu.startBuyerMenu(self,user)