f = open('Data/missing.csv', 'rt')
headers = next(f)
for line in f: 
    row = line.split(',')
    print(row)

f.close()
