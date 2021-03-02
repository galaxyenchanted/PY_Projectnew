import scrapy
imageLinks = []
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/multi/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            imageLinks.append(x.xpath(newsel).extract_first())
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        print("******************** Result ********************")
        print(imageLinks)


