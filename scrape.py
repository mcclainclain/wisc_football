from bs4 import BeautifulSoup
import pandas as pd
import requests

BASE_URL = "https://uwbadgers.com/sports/football/roster/"
years = list(range(2013, 2024))

columns=["Name", "Pos", "Grade", "Hometown", "Year"]
players = pd.DataFrame(columns=columns)

for year in years:
    soup = BeautifulSoup(requests.get(BASE_URL + str(year)).content, 'html.parser')
    roster = soup.find("ul", {"class": "sidearm-roster-players"})
    names = [h.find('a').text for h in soup.find_all("h3") if h.find('a') != None]
    positions = [t.text.strip() for t in roster.find_all('span', {"class": "text-bold"})]
    other = roster.find_all("div", {"class": "sidearm-roster-player-other flex-item-1 columns hide-on-medium-down"})
    grades = [s.find('span', {'class': 'sidearm-roster-player-academic-year'}).text for s in other]
    towns = [s.find('span', {'class': 'sidearm-roster-player-hometown'}).text for s in other]
    years = [year] * len(names)
    players = pd.concat([players, pd.DataFrame(list(zip(names, positions, grades, towns, years)), columns=columns)])
    

players.to_csv("players.csv", index=False)
