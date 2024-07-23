import sqlite3
from pathlib import Path

class dataBase:

    PATH = Path(__file__).parent

    def __init__(self):
        """Conecta ao banco de dados e cria as tabelas se não existirem."""
        self.con = sqlite3.connect(self.PATH / "database.bd")
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        """Cria as tabelas Athletes e Categories no banco de dados."""
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
                            FOREIGN KEY (athlete_id) REFERENCES Athletes(id))""")

    def query(self, query: str, data=tuple()):
        """Executa uma consulta no banco de dados e faz commit ou rollback em caso de erro."""
        try:
            self.cur.execute(query, data)
            self.con.commit()
        except Exception as err:
            self.con.rollback()
            raise err
