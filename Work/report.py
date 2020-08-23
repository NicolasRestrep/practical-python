import csv

def read_portfolio(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []

    for row in rows: 
        name = row[0]
        nshares = int(row[1])
        price = float(row[2])
        holding = {'name': name,
                   'shares': nshares, 
                   'price': price}
        portfolio.append(holding)
    return(portfolio)

    f.close()

def read_prices(filename):
    f = open(filename, 'r')
    rows = csv.reader(f)
    stocks = {}

    for row in rows:
        try:
            stocks[row[0]] = float(row[1])
        except IndexError:
            pass
    
    return stocks
    f.close()

def make_report(report):
    for name, num_shares, cost, price, gainloss in report:
        print(f'{name:>10s}{num_shares:>10d}{cost:>10.2f}{price:>10.2f}{gainloss:>10.2f}') 

def print_report(fn1, fn2): 
    portfolio = read_portfolio(filename = fn1)
    prices    = read_prices(filename = fn2)
    change_data = []
    for stock in portfolio:
        name = stock['name']
        num_shares = int(stock['shares'])
        cost = float(stock['price'])
        price = float(prices[stock['name']])
        gainloss = price - cost
        share = (name, num_shares, cost, price, gainloss)
        change_data.append(share)

    headers = ('Name', 'Shares', 'Cost', 'Price', 'Change')
    print('%10s %10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    make_report(change_data)

print_report(fn1 = 'Data/portfolio.csv', fn2 = 'Data/prices.csv')







