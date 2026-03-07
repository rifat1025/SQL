import mysql.connector
import sys

class DBhelper:

    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="DataScience"
            )

            self.cursor = self.conn.cursor()

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS aircrafts(
                id INT AUTO_INCREMENT PRIMARY KEY,
                aircraft_code VARCHAR(10),
                model VARCHAR(100),
                range_km INT
            )
            """)

        except Exception as e:
            print("Connection Failed:", e)
            sys.exit()

        else:
            print("Connection Successful")


    def insert_aircraft(self, aircraft_code, model, range_km):

        try:
            query = """
            INSERT INTO aircrafts (aircraft_code, model, range_km)
            VALUES (%s, %s, %s)
            """

            self.cursor.execute(query,(aircraft_code, model, range_km))
            self.conn.commit()

        except Exception as e:
            print("Insertion Failed:", e)

        else:
            print("Insertion Successful")
    
    def view_aircraft(self):
        try:
            query="""
            SELECT * FROM aircrafts
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Failed to fetch aircraft data:", e)
            return []   