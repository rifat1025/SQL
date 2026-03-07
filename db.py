import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Rifat"
            )
            self.mycursor=self.conn.cursor()
            
            
        except:
            print("connection failed")
        else:
            print("connection successfull")
        
    def register(self,name,email,password):
        try:
            
            self.mycursor.execute(
                """
                INSERT INTO users (name,email,password) VALUES('{}','{}','{}')
                """.format(name,email,password)
            )
            self.conn.commit()
        except:
            print("registration failed")
        else:
            print("registration successfull")
    def login(self,email,password):
        
        self.mycursor.execute(
            """
            SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
            """.format(email,password)
        )
        result =self.mycursor.fetchall()
        
        return result
        
        
        
           
            
        
        