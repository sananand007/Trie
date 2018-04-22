import scrapy as sc

#// *[ @ id = "qt0324253"] / div[1] / p / text()

class matrixQuotes(object):
    name="qoutes"
    start_urls=[
        'https://www.imdb.com/title/tt0133093/quotes',
    ]

    def parse(self, response):
        for quote in response.css('div.list'):
            print(quote)