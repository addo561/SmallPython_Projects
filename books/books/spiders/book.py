import scrapy

from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            item = BooksItem()
            item['url'] = book.css("h3 > a::attr(href)").get()
            item['title'] = book.css("h3 > a::attr(text)").get()
            item['price'] = book.css(".price_color::text").get()
            yield item
            
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield scrapy.Request(url = next_page_url,callback=self.parse)
            
#commands
'''
python -m pip install scrapy   
scrapy startproject books
scrapy shell http://books.toscrape.com
crapy genspider book https://books.toscrape.com/
scrapy crawl book
'''       