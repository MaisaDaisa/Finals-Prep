from bs4 import BeautifulSoup
import requests
from Database import TeamsDatabase
from Database import Team


soup = BeautifulSoup(requests.get("https://www.skysports.com/champions-league-table").content, 'html.parser')
tables = soup.find_all("table")
db = TeamsDatabase('sports.db')

try:
    for table in tables:
        group = table.find('caption', {'class': 'standing-table__caption'}).text.strip()[30]
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            row_info = []
            for cell in cells:
                row_info.append(cell.text.strip())
            if len(row_info) != 0:
                team = Team(group, row_info[1], row_info[-2])
                db.add_team(team)
except:
    print("Teams Exist moving on.... Skipping Database\n")

while True:
    print("Please Enter 'Group' if you want to search by Groups and get their losers and winners")
    print("Please Enter 'Team' if you want to get specific Team's stats")
    choice = input("Please enter Choice: ")
    if choice == "Group":
        group = input("Input Group letter only: ")
        group_list = db.get_team_by_groupe(group)
        if len(group_list) != 0:
            print(f"\ndominator of this group is {group_list[0].team} with {group_list[0].score}. Loser of this Group is {group_list[-1].team} with {group_list[-1].score}\n")
            print(f"These are All Groups in this Letter thingy: \n")
            for group in group_list:
                print(f"{group.team} WITH {group.score} POINTS")
            break
        else:
            print('Invalid Group')
            continue
    if choice == "Team":
        team = input('Input Team name: ')
        team_stats = db.get_team_by_name(team)
        if team_stats:
            print(f"Team: {team_stats.team} is in {team_stats.groupe} with {team_stats.score}")
            break
        else:
            print('Invalid Team')
            continue
    else:
        print("Invalid Choice! Try Again!")
        continue
