import requests
from Database import WikipediaDatabase
from bs4 import BeautifulSoup
from Database import Country

db = WikipediaDatabase('wikipedia.db')
try:
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find('table', {'style': 'text-align:right'}).find_all('tr')
    for row in rows[2:]:
        rank = row.th.text.strip()
        columns = row.find_all('td')
        name = columns[0].text.strip()
        population = int(columns[1].text.strip().replace(',', ''))
        if rank == "–":
            rank = None
        else:
            rank = int(rank)
        db.add_country(Country(rank, name, population))
except:
    print("Countrys Already exist... Skipping Database\n")

while True:
    print("Please Enter 'Country' if you want to search by Country's name")
    print("Please Enter 'Rank' if you want to get Country by their Rank")
    choice = input("Please enter Choice: ")
    if choice == "Country":
        name = str(input("Please choose a Country name: "))
        country = db.get_country_by_name(name)
        if country is None:
            print("Such Country does not Exist")
            continue
        else:
            print(f"\nCountry's name is {country.name} with population of {country.population} and ranking of {country.rank}")
            break
    if choice == "Rank":
        rank = int(input('Input Team name: '))
        country = db.get_country_by_rank(rank)
        if country is None:
            print('Such ranking does not Exist')
            continue
        else:
            print(f"\nCountry's name is {country.name} with population of {country.population} and ranking of {country.rank}")
            break
    else:
        print("Invalid Choice! Try Again")
        continue
