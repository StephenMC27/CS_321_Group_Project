from requests_html import HTMLSession
import csv

session = HTMLSession()

#scrape all 100 pages of website
quote_elements = []
for i in range(1,10):
    print(i)
    response = session.get(f'https://www.goodreads.com/quotes/tag/inspirational?page={i}')
    quote_elements += response.html.find('.quote.mediumText ')

print(f'# of quotes: {len(quote_elements)}')

csv_file = open('quotes.csv', 'w') #open new csv file
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote + Credit']) #column name

#loop through quote-containing HTML elements and store the text and author in csv_file
for quote_element in quote_elements:
    quote_string = quote_element.find('.quoteText')[0].text.split('//', 1)[0]
    split_string = quote_string.split('""')
    s = '"'
    quote_string = s.join(split_string)
    csv_writer.writerow([quote_string])
    print(quote_string)

csv_file.close()

# print(quote_elements[3].find('.quoteText', clean=True)[0].text.split('//', 1)[0])
