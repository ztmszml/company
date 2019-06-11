import scrapy
from company.items import CsItem
from scrapy import Selector, Request
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware

script = """
function main(splash, args)
  splash.images_enabled = false  
  assert(splash:go(args.url))
  assert(splash:wait(1))
  js = string.format("document.querySelector('#J-ajax-main > div > div.m-page.J-ajax-page > a:nth-child(6)').click();", args.page)
  splash:runjs(js)
  assert(splash:wait(5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
"""


class CsSpider(scrapy.Spider):
    name = 'cs'
    allowed_domains = ['xinsanban.eastmoney.com']
    start_urls = ['http://xinsanban.eastmoney.com/QuoteCenter/ListedCompany/Index/']


    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def start_requests(self):
        for page in range(1, 5):
                url = self.start_urls
                yield SplashRequest(url, callback=self.parse, endpoint='execute',
                                    args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        trlist = response.xpath('//*[@id="J-ajax-main"]/div/table//tr')
        for tr in trlist:
            item=CsItem()
            item["CId"]=tr.xpath("./td[1]/a/text()").extract_first()
            item["CName"] = tr.xpath("./td[2]/a/text()").extract_first()
            item["NPrice"] = tr.xpath("./td[3]/em/text()").extract_first()
            item["UpDown"] = tr.xpath("./td[4]/em/text()").extract_first()
            item["Range"] = tr.xpath("./td[5]/em/text()").extract_first()
            item["Volume"] = tr.xpath("./td[6]/text()").extract_first()
            item["Transaction"] = tr.xpath("./td[7]/text()").extract_first()
            item["CloseY"] = tr.xpath("./td[8]/text()").extract_first()
            item["OpenT"] = tr.xpath("./td[9]/em/text()").extract_first()
            item["HPrice"] = tr.xpath("./td[10]/em/text()").extract_first()
            item["LPrice"] = tr.xpath("./td[11]/em/text()").extract_first()
            item["PE"] = tr.xpath("./td[12]/text()").extract_first()
            item["Value"] = tr.xpath("./td[13]/text()").extract_first()
            yield item










