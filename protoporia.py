import scrapy

ITEMS_PER_PAGE = 1000

class MySpider(scrapy.Spider):
    name = 'protoporia'
    allowed_domains = ['protoporia.gr']
    start_urls = [
        f'https://www.protoporia.gr/?items_per_page={ITEMS_PER_PAGE}&subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q=%CE%BC%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&dispatch=products.search',
    ]

    custom_settings = {
        'FEEDS': {
            'protoporia.csv': {
                'format': 'csv',
                'encoding': 'utf8',
            }
        },
        'DOWNLOAD_DELAY': 5, # seconds
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
    }

    field_css = (
        ('title', 'div.ty-grid-list__item-name > a::text'),
        ('author', 'div.ty-grid-list__sigrafeas ::text'),
        ('price', 'span.ty-price-num:nth-child(2) ::text'),
        ('old_price', 'span.ty-list-price:nth-child(2) ::text'),
        ('url', 'div.ty-grid-list__item-name > a::attr(href)'),
    )

    def parse(self, response):
        for item in response.css('div.ty-grid-body'):
            yield dict([(field, item.css(css).get()) for field, css in self.field_css])

        for href in response.css('a.ty-pagination__item::attr(href)').getall():
            yield scrapy.Request(href, self.parse)
