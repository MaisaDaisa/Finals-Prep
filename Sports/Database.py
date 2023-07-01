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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                groupe TEXT,
                team TEXT UNIQUE, 
                score INT
            )
        """)
        # TEAM UNIQUE იმიტომ დავწერე, რომ მეორეჯერ დამატებისას ამოაგდოს ერრორი და ამით დაისკიპოს დამატება, რადგან Try მაქ გაშვებული

    def add_team(self, Team):
        self.cursor.execute("""
            INSERT INTO teams (groupe, team, score) VALUES (?, ?, ?)
        """, (Team.groupe, Team.team, Team.score))
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