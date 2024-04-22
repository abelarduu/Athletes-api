import sqlite3
from pathlib import Path

class dataBase:

    PATH= Path(__file__).parent

    def __init__(self):
        #Connecting with db
        self.con= sqlite3.connect(self.PATH / "database.bd")
        self.cur= self.con.cursor()
        self.create_tables()

    def create_tables(self):
        #Tables
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Athletes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(40),
                            cpf VARCHAR(11),
                            age INT,
                            weight FLOAT,
                            height FLOAT,
                            sex VARCHAR(1))""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Categories (
                            athlete_id INTEGER,
                            name VARCHAR(40),
                            weight FLOAT,
                            FOREIGN KEY (athlete_id) REFERENCES Atletas(id))""")

    def query(self, query: str, data= tuple()):
        try:
            self.cur.execute(query, data)
            self.con.commit()
        except Exception as err:
            self.con.rollback()
            raise err