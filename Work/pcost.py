# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    sum = 0
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for n,row in enumerate(rows,1):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                sum += nshares * price
            except ValueError:
                print(f"Row {n}: Couldn't convert {row}")
    return sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
