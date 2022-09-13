from Login import * 
class Menu:
    login = Login()
    def startMenu(self):
        print(" ~ Welcome everybody to Library Project by ALESJA CANI! :) ~ \n")
        print("Please write down the number to continue of whatever menu you want.")
        print("1 - Go to ADMIN MENU")
        print("2 - Go to BUYER MENU")
        print("\n")
        
        try:
            choice = int(input("Write down the number to continue: "))
                    
            if(choice==1 or choice ==2):
                self.login.loginMethod()
            else:
                print("Please write 1 or 2 numbers. Try again!\n\n\n")
                Menu.startMenu(self)

        except(BaseException): 
            print("Please write 1 or 2 numbers. Try again!\n\n\n")
            Menu.startMenu(self)

menu=Menu()
menu.startMenu()