import scrapy


class CalientespiderSpider(scrapy.Spider):
    name = "calientespider"
    allowed_domains = ["sports.caliente.mx"]
    start_urls = ["https://sports.caliente.mx"]

    def parse(self, response):
        pass
