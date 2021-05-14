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
            record = dict(zip(headers, row))
            dictio = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price']),
            }
            portfolio.append(dictio)
        return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for n,row in enumerate(rows,start=1):
            #print(cpt,row)
            try:
                prices[row[0]] = float(row[1])
            except:
                sys.stdout.write(RED)
                print("read_prices: Error line",n,"of",filename,":",row)
                sys.stdout.write(RESET)
        return prices

def make_report(stocks, prices):
    list = []
    for stock in stocks:
        name, shares = stock['name'],stock['shares']
        price = prices[name]
        if price < stock['price']:
            change = -float(stock['price']-price)
        else:
            change = price - stock['price']
        list.append((name,shares,price,change))
    return list

headers = f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}\n' \
          f'---------- ---------- ---------- ----------'
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print(headers)
for r in report:
    print("%10s %10d %10s %10.2f" % (r[0],r[1],'$'+str(r[2]), r[3]))
cost = sum([s['shares'] * s['price'] for s in portfolio ])
print(cost)

# tests read_portfolio
""" 
portfolio = read_portfolio('Data/portfolio.csv')
total = 0.0
for s in portfolio:
    total += s['shares']*s['price']
pprint(portfolio)
print(total)
"""

# tests read_prices
""" 
prices = read_prices('Data/prices.csv')
print(prices['IBM'])
print(prices['MSFT'])
"""

# gain/loss
""""
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
"""