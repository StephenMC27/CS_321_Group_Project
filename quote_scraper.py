from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://www.goodreads.com/quotes/tag/inspirational')

quote_elements = response.html.find('.quote.mediumText ')

# for quote_element in quote_elements:
#     quote_string = quote_element.find('.quoteText')[0].text
#     print(quote_string)

print(quote_elements[0].find('.quoteText')[0].html)
