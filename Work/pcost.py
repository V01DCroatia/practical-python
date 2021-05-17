#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import sys
import csv
import report


def portfolio_cost(filename: str):
    portfolio = report.read_portfolio(filename)
    somme = sum([s['price']*s['shares'] for s in portfolio])
#    with open(filename) as file:
#        rows = csv.reader(file)
#        headers = next(rows)
#        for n,row in enumerate(rows,1):
#            record = dict(zip(headers,row))
#            try:
#                nshares = int(record['shares'])
#                price = float(record['price'])
#                sum += nshares * price
#            except ValueError:
#                print(f"Row {n}: Couldn't convert {row}")
    return somme


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio')
    print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
    main(sys.argv)

#cost = portfolio_cost(filename)
