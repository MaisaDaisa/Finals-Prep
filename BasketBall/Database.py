import sqlite3

class Team:
    def __init__(self, team: str, points):
        self.team = team
        self.points = points
class BasketballDatabase:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS basketball(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                team TEXT,
                points INTEGER
            )"""
        )

    def add_team(self, Team):
        self.cursor.execute("""
            INSERT INTO basketball(team, points)
            VALUES (?, ?)""", (Team.team, Team.points))
        self.conn.commit()

    def get_team_by_name(self, team):
        self.cursor.execute(f"""
                SELECT * from basketball
                WHERE team like '%{team}%'""")
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Team(*row[1:])
    def get_all_teams(self):
        self.cursor.execute("""SELECT * from basketball""")
        rows = self.cursor.fetchall()
        teams = [Team(*row[1:]) for row in rows]
        return teams