import requests
from bs4 import BeautifulSoup
import time

def scrape_apple_stock_details(retries=3):
    url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
    for _ in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            break
        time.sleep(2)
    else:
        raise Exception(f"Failed to load page {url} after {retries} retries")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting stock price
    stock_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    # Extracting previous close
    previous_close = soup.find('td', {'data-test': 'PREV_CLOSE-value'}).text
    # Extracting market cap
    market_cap = soup.find('td', {'data-test': 'MARKET_CAP-value'}).text

    return {
        'stock_price': stock_price,
        'previous_close': previous_close,
        'market_cap': market_cap
    }

if __name__ == "__main__":
    apple_stock_details = scrape_apple_stock_details()
    print("Apple Inc. (AAPL) Stock Details:")
    print(f"Stock Price: {apple_stock_details['stock_price']}")
    print(f"Previous Close: {apple_stock_details['previous_close']}")
    print(f"Market Cap: {apple_stock_details['market_cap']}")
