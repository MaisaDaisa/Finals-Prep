import requests
from Database import WikipediaDatabase
from bs4 import BeautifulSoup
from Database import Country

db = WikipediaDatabase('wikipedia.db')

soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').content, 'html.parser')
rows = soup.find_all('tr')
for row in rows[3:]:
    print(row)