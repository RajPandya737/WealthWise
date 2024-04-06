from datetime import timedelta
from datetime import datetime
import json
import yfinance as yf
class InvestmentData:
    def __init__(self, historical_file):
        self.historical_file = historical_file
        self.data = {
            "investments": {
                "stocks": [],
                "bonds": []
            }
        }
    def save_historical_data(self):
        # Overwrite the file with the current data
        with open(self.historical_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_stock(self, currency, ticker, amount, purchase_date, purchase_price):
        # Construct the new stock entry
        new_stock = {
            "currency": currency,
            "ticker": ticker,
            "amount": amount,
            "purchase_date": purchase_date,
            "purchase_price": purchase_price
        }
        # Directly add to the initialized data structure
        self.data['investments']['stocks'].append(new_stock)

    def addBond(self, currency, ticker, amount, purchase_date, purchase_price):
        # Construct the new bond entry
        new_bond = {
            "currency": currency,
            "ticker": ticker,
            "amount": amount,
            "purchase_date": purchase_date,
            "purchase_price": purchase_price
        }
        # Directly add to the initialized data structure
        self.data['investments']['bonds'].append(new_bond)




class HistoricalData:
    def __init__(self, live_file):
        self.live_file = live_file

    def fetch_and_process_data(self, tickers):
        data = {}
        today = datetime.now().date()
        offsets = {
            "1day": 1,
            "week": 7,
            "month": 30,
            "three_months": 90,
            "six_months": 180,
            "year": 365,
            "five_year": 1825
        }

        for ticker in tickers:
            equity = yf.Ticker(ticker)
            historical_data = equity.history(period="5y", interval="1d")

            # Skip if no data
            if historical_data.empty:
                print(f"No data for {ticker}")
                continue

            # Initialize a dictionary for the ticker
            ticker_data = {}

            for period_name, days_ago in offsets.items():
                target_date = today - timedelta(days=days_ago)

                # Adjust for weekends/holidays by finding the closest earlier date with data
                adjusted_date = target_date.strftime('%Y-%m-%d')
                while adjusted_date not in historical_data.index.strftime('%Y-%m-%d') and target_date > today - timedelta(days=1825):
                    target_date -= timedelta(days=1)
                    adjusted_date = target_date.strftime('%Y-%m-%d')

                # Attempt to retrieve and store the data
                try:
                    closing_price = historical_data.loc[adjusted_date]['Close']
                    ticker_data[period_name] = round(closing_price, 2)
                except KeyError:
                    ticker_data[period_name] = "No Data"

            # Assign the collected data under the ticker
            data[ticker] = ticker_data

        self.save_historical_data(data)

    def save_historical_data(self, data):
        with open(self.live_file, 'w') as file:
            json.dump(data, file, indent=4)

historical_data = HistoricalData('historical_data.json')
tickers = ["XIU.TO", "HBM", "L", "WFG", "SPY", "APO", "AAPL", "CEG", "EA", "ISRG", "MA", "TEX", "AMSF", "VEEV", "GSL", "XBB", "AGG", "SPSB"]
historical_data.fetch_and_process_data(tickers)


data_manager = InvestmentData('portfolio_historical.json')


# CAD Portfolio
data_manager.add_stock("CAD", "XIU", 519, "DD/MM/YYYY", 31.26)
data_manager.addBond("CAD", "XBB", 741, "DD/MM/YYYY", 28.15)
data_manager.add_stock("CAD", "HBM", 225, "DD/MM/YYYY", 6.68)
data_manager.add_stock("CAD", "L", 20, "DD/MM/YYYY", 126.00)
data_manager.add_stock("CAD", "WFG", 23, "DD/MM/YYYY", 112.40)
data_manager.add_stock("CAD", "CSH.UN", 107, "DD/MM/YYYY", 11.60)

# USD Portfolio
data_manager.addBond("USD", "AGG", 96, "DD/MM/YYYY", 97.83)
data_manager.add_stock("USD", "SPY", 25, "DD/MM/YYYY", 406.81)
data_manager.add_stock("USD", "APO", 30, "DD/MM/YYYY", 62.36)
data_manager.add_stock("USD", "AAPL", 4, "DD/MM/YYYY", 165.39)
data_manager.add_stock("USD", "CEG", 25, "DD/MM/YYYY", 76.42)
data_manager.add_stock("USD", "EA", 16, "DD/MM/YYYY", 121.57)
data_manager.add_stock("USD", "ISRG", 8, "DD/MM/YYYY", 238.04)
data_manager.add_stock("USD", "MA", 5, "DD/MM/YYYY", 358.41)
data_manager.add_stock("USD", "TEX", 56, "DD/MM/YYYY", 34.66)
data_manager.add_stock("USD", "AMSF", 45, "DD/MM/YYYY", 47.20)
data_manager.add_stock("USD", "VEEV", 5, "DD/MM/YYYY", 189.04)
data_manager.add_stock("USD", "GSL", 101, "DD/MM/YYYY", 20.29)
data_manager.addBond("USD", "SPSB", 320, "DD/MM/YYYY", 29.73)

data_manager.save_historical_data()
