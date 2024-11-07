# applepy stock.py
import requests
from bs4 import BeautifulSoup

# uRL for Apple stock historical prices
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

def get_apple_stock_data(url):
    # Sending a GET request to fetch the webpage
    response = requests.get(url)

    if response.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding the historical prices table
        prices_table = soup.find('table', {'data-test': 'historical-prices'})
        prices_rows = prices_table.find_all('tr')[1:]  # Skip header row

        # Print header 
        print("Apple Stock Historical Closing Prices:")
        
        # Looping through each row to extract date and close price
        for row in prices_rows:
            columns = row.find_all('td')
            if len(columns) > 0:
                date = columns[0].text.strip()
                close_price = columns[4].text.strip()  # Close price is usually the 5th column
                
                # Display date and closing price
                print(f"Date: {date} | Close Price: {close_price}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    get_apple_stock_data(url)
