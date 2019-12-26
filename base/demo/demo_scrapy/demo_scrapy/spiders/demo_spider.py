import scrapy

from demo_scrapy.items import DemoScrapyItem

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["toutiao.com"]
    start_urls = [
        "https://www.toutiao.com/ch/news_tech/",
        "https://www.toutiao.com/ch/news_game/",
        "https://www.toutiao.com/ch/news_image/"
    ]

    def parse(self, response):

        for sel in response.xpath('//ul/li'):
            item = DemoScrapyItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print("=====>", title, link, desc)

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)