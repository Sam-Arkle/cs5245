import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    # def start_requests(self):
    #     urls = [
    #         'https://quotes.toscrape.com/page/1/',
    #         'https://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            next_page = response.css('li.next a::attr(href)').get()
            # if next_page is not None:
            #     # next_page = response.urljoin(next_page)
            #     # yield scrapy.Request(next_page, callback=self.parse)
            #     yield response.follow(next_page, callback=self.parse)
            # Shorter version below
            # for href in response.css('ul.pager a::attr(href)'):
            #     yield response.follow(href, callback=self.parse)

            # anchors = response.css('ul.pager a')
            # yield from response.follow_all(anchors, callback=self.parse)
            yield from response.follow_all(css='ul.pager a', callback=self.parse)
