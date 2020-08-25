import csv
import fileparse

def read_portfolio(filename):
    p = fileparse.parse_csv(filename, types=[str, int, float])
    return p

def read_prices(filename):
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers=False)
    prices_dict = dict(prices)
    return prices_dict

def make_report(report):
    for name, num_shares, cost, price, gainloss in report:
        print(f'{name:>10s}{num_shares:>10d}{cost:>10.2f}{price:>10.2f}{gainloss:>10.2f}') 

def print_report(fn1, fn2): 
    portfolio = read_portfolio(filename = fn1)
    prices    = read_prices(filename = fn2)
    change_data = []
    for stock in portfolio:
        name = stock['name']
        num_shares = stock['shares']
        cost = stock['price']
        price = prices[stock['name']]
        gainloss = price - cost
        share = (name, num_shares, cost, price, gainloss)
        change_data.append(share)

    headers = ('Name', 'Shares', 'Cost', 'Price', 'Change')
    print('%10s %10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    make_report(change_data)

print_report(fn1 = 'Data/portfolio.csv', fn2 = 'Data/prices.csv')







