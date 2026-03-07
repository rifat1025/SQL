import pandas as pd
import numpy as np
import random
from aircraftsdb import DBhelper
import sys

class Aircrafts:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):

        user_input = input("""
                1. Push Aircraft Data
                2. View Aircrafts
                3. Exit
                """)

        if user_input == "1":
            self.add_aircrafts()

        elif user_input == "2":
            self.view_aircrafts()

        else:
            sys.exit()


    def add_aircrafts(self):

        models = [
            {"en": "Boeing 777-300"},
            {"en": "Boeing 767-300"},
            {"en": "Sukhoi Superjet-100"},
            {"en": "Airbus A320-200"},
            {"en": "Airbus A321-200"},
            {"en": "Boeing 737-300"},
            {"en": "Bombardier CRJ-200"},
            {"en": "Cessna 208 Caravan"}
        ]

        data = []

        for i in range(200):

            model_info = random.choice(models)

            row = {
                "aircraft_code": random.randint(100,999),
                "model": model_info["en"],
                "range": random.randint(1200,15000)
            }

            data.append(row)

        aircrafts_data_large = pd.DataFrame(data)

        for _, row in aircrafts_data_large.iterrows():

            self.db.insert_aircraft(
                row["aircraft_code"],
                row["model"],
                row["range"]
            )

        print("200 Aircraft inserted successfully")

        self.menu()


    def view_aircrafts(self):

        data = self.db.view_aircraft()
        for i in data:
            print(i)

        self.menu()


obj = Aircrafts()