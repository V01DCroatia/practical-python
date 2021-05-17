# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename: str, select: list = None, types: list = None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)
        if has_headers:
            headers = next(rows)
        else:
            headers = []
        if select is None:
            select = ['name', 'shares', 'price']
            indices = []
        else:
            indices = [headers.index(colname) for colname in select]
            headers = select
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records


dictio = parse_csv('Data/portfolio.dat',types=[str, int, float], delimiter=' ')
print(dictio)
