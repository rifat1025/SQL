import sys
from db import DBhelper


class Flipkart:
    def __init__(self):
        self.db=DBhelper()
        self.menu()
    
    def menu(self):
        user_input=input(
            """
            "1.register"
            "2.login"
            "3.exit"
            """
            

        )
        
        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit()
            
    def register(self):
        
        name=input("enter your name")
        email=input("enter your email")
        password=input("enter your password")
            
        self.db.register(name,email,password)
        
        self.menu()
    def login(self):
        email=input("enter your email")
        password=input("enter your password")
        
        result=self.db.login(email,password)
        if len(result)==0:
            print("login failed")
            self.login()
        else:
            print("login successful")
        
        
            
            

obj=Flipkart()


            
        
        
        