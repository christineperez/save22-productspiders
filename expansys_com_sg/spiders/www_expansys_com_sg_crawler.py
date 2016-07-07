from scrapy.spider import BaseSpider
from scrapy.spider import HtmlXpathSelector
from scrapy,contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from expansys_com_sg.items import ExpansysComSgItem

class WwwExpansysComSgCrawler(BaseSpider):
  name = "www_expansys_com_sg_crawler"
  allowed_domains = ["www.expansys.com.sg"]
  start_urls = ['http://www.expansys.com.sg/']
  
  rules = (
    Rule(SgmlLinkExtractor(allow=(r'//?page=[0-9]#listing '), deny = ()), follow=True,callback='parse_item',
        ),
        )

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    tds = hxs.select('')
    for td in tds:
  
  def parse_item(self, response):
  
      
       

