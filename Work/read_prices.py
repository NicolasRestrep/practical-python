# read_prices.py
import csv

def read_prices(filename):
    f = open(filename, 'r')
    rows = csv.reader(f)
    stocks = {}

    for row in rows:
        try:
            stocks[row[0]] = float(row[1])
        except IndexError:
            print("Couldn't parse", row)
    
    return stocks
    f.close()
