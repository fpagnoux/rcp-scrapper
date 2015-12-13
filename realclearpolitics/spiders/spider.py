import scrapy
from realclearpolitics.items import TableItem

class spider(scrapy.Spider):
    name = "realclearpoliticsSpider"
    start_urls = []

    def __init__(self, url, noavg=""):
        self.url = url
        self.noavg = noavg

    def start_requests(self):
        return [scrapy.FormRequest(self.url,
                               callback=self.parse)]


    def parse(self, response):
        table = response.css('.data').pop()
        legend = table.css('.header')[0]
        fieldNames = legend.css('th::text, th div span::text').extract()
        nb_fields = len(fieldNames)
        items = []

        contentLines = table.css('tr')[(2 if self.noavg else 1)::]

        for line in contentLines:
            item = TableItem()
            values = line.css('td::text, td span::text, td a.normal_pollster_name::text').extract()
            for i in range(nb_fields):
                item[fieldNames[i]] = values[i] if values[i] != "--" else "0"

            items.append(item)

        return items
