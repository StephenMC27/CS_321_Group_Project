import csv
import random

class Quotes:

    quotes = []

    @classmethod
    def fetch_quotes(cls, csv_file):
        #open csv file
        with open(csv_file, newline='') as quotes_file:
            #read quotes into list
            quote_reader = csv.reader(quotes_file)
            for row in quote_reader:
                cls.quotes.append(row)

    @classmethod
    def get_quote(cls):
        return(random.choice(cls.quotes)[0])

if __name__ == '__main__':
    Quotes.fetch_quotes('../csv/quotes.csv')
    print(Quotes.quotes)
    random_quote = Quotes.get_quote()
    print(random_quote)
