import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["ammannet.net/أخبار"]
    start_urls = ["http://ammannet.net/أخبار/"]

    def parse(self, response):
        news = response.css('div.views-row')
        for new in news:
            item = {
                'title': new.css('a::text').get(),
                'content': new.css('p::text').get(),
                'created_at': new.css('div.field--name-node-post-date::text').get()
            }
            yield item
        pass
