# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    sum = 0
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                sum += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", row)
    return sum


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
