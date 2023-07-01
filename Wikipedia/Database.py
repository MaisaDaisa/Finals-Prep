import sqlite3

class Country:
    def __init__(self, rank, name: str, population: int):
        self.rank = rank
        self.name = name
        self.population = population

class WikipediaDatabase:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS countrys(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rank INTEGER,
                name TEXT UNIQUE,
                population INTEGER
            )"""
        )

    def add_country(self, Country):
        self.cursor.execute("""
            INSERT INTO countrys(rank, name, population)
            VALUES (?, ?, ?)""", (Country.rank, Country.name, Country.population))
        self.conn.commit()

    def get_country_by_name(self, name):
        self.cursor.execute(f"""
                SELECT * from countrys
                WHERE name like '%{name}%'""")
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Country(*row[1:])
    def get_all_country(self):
        self.cursor.execute("""SELECT * from countrys""")
        rows = self.cursor.fetchall()
        countrys = [Country(*row[1:]) for row in rows]
        return countrys

    def get_country_by_rank(self, rank):
        self.cursor.execute("""SELECT * from countrys WHERE rank = ?""", (rank,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Country(*row[1:])