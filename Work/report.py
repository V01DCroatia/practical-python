# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint
RED = "\033[1;31m"
RESET = "\033[0;0m"

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            dict = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
            }
            portfolio.append(dict)
        return portfolio

def read_prices(filename):
    prices = {}
    cpt = 1
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            #print(cpt,row)
            try:
                prices[row[0]] = float(row[1])
            except:
                sys.stdout.write(RED)
                print("read_prices: Error line",cpt,":",row)
                sys.stdout.write(RESET)
            cpt+=1
        return prices

#tests read_portfolio
""" 
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for s in portfolio:
    total += s['shares']*s['price']
pprint(portfolio)
print(total)
"""

#tests read_prices
""" 
prices = read_prices('Data/prices.csv')
print(prices['IBM'])
print(prices['MSFT'])
"""

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
gain = 0
loss = 0
for action in portfolio:
    portfolio_price = action['shares'] * action['price']
    actual_price = action['shares'] * prices[action['name']]
    if portfolio_price > actual_price:
        gain += portfolio_price - actual_price
    else:
        loss += actual_price - portfolio_price

print("gain and loss are",gain,loss)
print(f'gain/loss ratio is {gain/loss:0.2f}')
