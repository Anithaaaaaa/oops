class User:
    def __init__(self, withdrawal, deposit, password="123"):
        self.withdrawal=withdrawal
        self.deposit=deposit
        self.password=password
        
    def display_details(self):
         print("withdrawal:", self.withdrawal)
         print("deposit:", self.deposit)
         print("password:", self.password)
         
        
    def display_info(self, user_input):
        if (user_input == withdrawal):
            print("password")
            
        elif (user_input == deposit):
            print("password")
            
        else:
            print("exit")
            
user = User("withdrawal" ,"deposit", "A1234")            
print(user.display_details())   

user_input=input("withdrawl") 
user = User("withdrawal" ,"deposit", "A1234") 
print(user.display_info())    