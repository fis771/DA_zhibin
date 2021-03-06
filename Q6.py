import scrapy
class mySpider(scrapy.Spider):
    name = 'new_spider'
    start_urls = ['http://172.17.50.43/nantes']
    def parse(self, response):
        css_sel = 'img'
        for x in response.css(css_sel):
            new_xpath_sel = '@src'
            yield {
                'IMAGE link': x.xpath(new_xpath_sel).extract_first()
            }
        next_sel = '.next a::attr(href)'
        next_page = response.css(next_sel).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)