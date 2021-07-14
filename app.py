from collections import defaultdict

import pandas

import yfinance as yf
data = yf.download("AMZN GOOGL", start="2021-02-01", end="2021-05-01")



print(data)

class Portfolio:

    def __init__(self) -> None:
        self.stocks = defaultdict()

    
    def add_entry(self, ticker, avg_value, amount):
        self.stocks[ticker] = {
            'avg_value': avg_value,
            'amount': amount
        }

    def view_entries(self):
        print(self.stocks)
    
# my_portfolio = Portfolio()

# my_portfolio.add_entry('AAPL', '112.3', '0.8733')

# my_portfolio.view_entries()


