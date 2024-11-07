# football_stats.py
import requests
from bs4 import BeautifulSoup

    #NFL Stats URL for touchdowns
url = 'https://www.cbssports.com/nfl/stats/player-stats/'

def get_football_stats(url):
    # Send a GET request to fetch the webpage
    response = requests.get(url)

    if response.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Locate the player statistics table
        stats_table = soup.find('table', {'class': 'TableBase-table'})
        stats_rows = stats_table.find_all('tr')[1:21]  # Get the first 20 player stats

        # Print header for clarity
        print("Top 20 NFL Players in Touchdowns:")
        
        # Loop through each row to extract player data
        for row in stats_rows:
            columns = row.find_all('td')
            if len(columns) > 0:
                player_name = columns[1].text.strip()
                position = columns[2].text.strip()
                team = columns[3].text.strip()
                touchdowns = columns[4].text.strip()
                
                # Display player information
                print(f"{player_name} | Position: {position} | Team: {team} | Touchdowns: {touchdowns}")
    else:
        print(f"Couldn't retrieve data: {response.status_code}")

