import requests
import sqlite3
Connection = sqlite3.connect("Database11")
c = Connection.cursor()

#c.execute('''CREATE TABLE CLIENTS
#             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')
c.execute("""CREATE TABLE Accounts
            (Username text,Password)""")
c.execute("""INSERT INTO Accounts VALUES
        ("Red","Password")""");
Connection.commit()
