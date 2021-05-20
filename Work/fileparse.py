# fileparse.py
#
# Exercise 3.3

import csv
import os
import sys

from colors import *

def parse_csv(filename: str, select: list = None, types: list = None,
              has_headers: bool = True, delimiter: str = ',', silence_errors: bool = False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    isFilenameAFile = False
    try:
        isFilenameAFile = os.path.isfile(filename)
        print(f'Parameter %s is a file.' % filename)
    except Exception:
        print("Parameter is not a file.")
    if isFilenameAFile:
        filename = open(filename)
    rows = csv.reader(filename, delimiter=delimiter)
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
    for i, row in enumerate(rows, 1):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if not silence_errors:
                    sys.stdout.write(RED)
                    print(f'File "{filename}" | Row {i}: Couldn\'t convert {row}')
                    print('Row %d: Reason %s' % (i, e))
                    sys.stdout.write(RESET)
                # raise
                continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    if isFilenameAFile:
        filename.close()
    return records
