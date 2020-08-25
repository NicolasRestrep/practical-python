# fileparse.py
import csv

def parse_csv(filename, select = None, types = None, has_headers=True, delimiter = None):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    with open(filename) as f:
        if not delimiter:
            rows = csv.reader(f)
        else:
            rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was give, find indices of the specified columns 
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []
        

        
        records = []
        for row in rows:
            if not row:     # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Couldn't convert {row}")
                    print(f'{row}: ', e)
            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
            else: 
                records.append(row)
    
    return records

# I am so proud of what I'm doing here