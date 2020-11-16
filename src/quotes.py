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

# if __name__ == '__main__':
#     Quotes.fetch_quotes('../csv/quotes.csv')
#     print(Quotes.quotes)
#     random_quote = Quotes.get_quote()
#     print(random_quote)
