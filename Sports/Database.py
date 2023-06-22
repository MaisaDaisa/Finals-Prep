import sqlite3

class Team:
    def __init__(self, groupe, team, score):
        self.groupe = groupe
        self.team = team
        self.score = score

class TeamsDatabase:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teams(
                id INTEGER PRIMARY KEY,
                groupe TEXT,
                team TEXT UNIQUE,
                score INT
            )
        """)

    def add_team(self, Team):
        self.cursor.execute("""
            INSERT INTO teams VALUES 
            (?, ?, ?, ?)
        """, (self.get_last_id()+1, Team.groupe, Team.team, Team.score))
        self.conn.commit()

    def get_team_by_name(self, team):
        self.cursor.execute("""
            SELECT * FROM teams WHERE team=?
        """, (team,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Team(*row[1:])

    def get_team_by_groupe(self, groupe):
        self.cursor.execute("""
               SELECT * FROM teams WHERE groupe=?
               ORDER BY score DESC
           """, (groupe,))
        rows = self.cursor.fetchall()
        teams = [Team(*row[1:]) for row in rows]
        return teams


    def get_last_id(self):
        self.cursor.execute("""
            SELECT id FROM teams ORDER BY id DESC LIMIT 1
        """)
        row = self.cursor.fetchone()
        if row is None:
            return 0
        return row[0]