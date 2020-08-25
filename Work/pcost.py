# pcost.py
#
# Exercise 1.27
import csv
import sys
import report

def portfolio_cost(filename):
    p = report.read_portfolio(filename)
    total = 0
    for stock in p: 
        try:
            nshares = stock['shares']
            price = stock['price']
            total += nshares * price
        except ValueError:
            print(f'Could not convert: {stock}')

    return(total)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost:", cost)