import scrapy
import re


class GetUrlsSpider(scrapy.Spider):
    name = "get_urls"
    allowed_domains = ["index.minfin.com.ua"]
    start_urls = ["https://index.minfin.com.ua/ua/russian-invading/casualties"]

    def parse(self, response, **kwargs):
        prefix = "/month.php?month="
        content = response.xpath("/html//div[@class='ajaxmonth']/h4[@class='normal']/a")
        for link in content:
            yield {
                "href": prefix + re.search(r"\d{4}-\d{2}", link.xpath("@id").get()).group()
            }
