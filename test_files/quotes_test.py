import csv
import random

quotes = []

def fetch_quotes(csv_file):
    global quotes
    #open csv file
    with open(csv_file, newline='', encoding="utf8") as quotes_file:
        #read quotes into list
        quote_reader = csv.reader(quotes_file)
        for row in quote_reader:
            quotes.append(row)

def get_quote():
    global quotes
    return(random.choice(quotes)[0])

if __name__ == '__main__':
    try:
        fetch_quotes('../csv/quotes.csv')
    except Exception as e:
        print('Exception thrown in fetch_quotes()\n')
        print(e)

    for quote in quotes:
        print(f'{quote}\n')
    try:
        random_quote = get_quote()
        print(random_quote)
    except Exception as e:
        print('Exception thrown in get_quote()\n')
        print(e)

    print('Tests successful.')
