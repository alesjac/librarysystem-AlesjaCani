import csv
class User:
    user_records='users.csv'

    def getUserbyUsername(self,username):
        print("------------------------\n")
        user=[]
        with open(self.user_records,"r") as file:
            reader = csv.reader(file)
            for row in reader:    
                if row[0] == username:
                    user.append(row)
        return user