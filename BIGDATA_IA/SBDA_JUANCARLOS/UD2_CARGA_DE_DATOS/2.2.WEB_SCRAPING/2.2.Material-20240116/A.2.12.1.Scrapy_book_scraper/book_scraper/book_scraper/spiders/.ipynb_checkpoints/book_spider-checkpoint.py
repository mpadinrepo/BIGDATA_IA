import scrapy

class BooksSpider(scrapy.Spider):
    name = 'libros'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        # Extracting book details
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            yield {
                'title': title,
                'price': price,
            }

        # Follow pagination link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)