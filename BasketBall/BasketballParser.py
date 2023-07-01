import requests
from Database import BasketballDatabase
from bs4 import BeautifulSoup
from Database import Team

db = BasketballDatabase('Basketball.db')
try:
    response = requests.get("https://www.basketball-reference.com/playoffs/NBA_2023.html")
    parser = BeautifulSoup(response.content, "html.parser")
    table = parser.find('div', {'id': 'all_totals_team-opponent'})
    rows = table.find('tbody').find_all("tr")
    for row in rows:
        name = row.find('td', {'data-stat': 'team'}).text.strip()
        points = row.find('td', {'data-stat': 'pts'}).text.strip()
        if len(points) == 0:
            points = 0
        else:
            points = int(points)
        team = Team(name, points)
        db.add_team(team)
except:
    print("Already Exists Moving on...")

while True:
    print("Please Enter 'Team' if you want to get specific Team's stats")
    print("Please Enter 'Groups' if you want to get all Groups stats")
    choice = input("Please enter Choice: ")
    if choice == "Groups":
        teams = db.get_all_teams()
        print("")
        for team in teams:
            print(f"Team {team.team} with {team.points}")
        break
    elif choice == "Team":
        team = input('Input Team name: ')
        team_stats = db.get_team_by_name(team)
        if team_stats:
            print("\n")
            print(f"Team {team_stats.team} with {team_stats.points}")
            break
        else:
            print('Invalid Team')
            continue
    else:
        print("invalid Choice")
        continue
