from scrapy.spider import BaseSpider
from scrapy.spider import HtmlXpathSelector
from scrapy,contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from expansys_com_sg.items import ExpansysComSgItem

class WwwExpansysComSgCrawler(BaseSpider):
  name = "www_expansys_com_sg_crawler"
  allowed_domains = ["www.expansys.com.sg"]
  start_urls = ['http://www.expansys.com.sg/mobile-phones/' , 'http://www.expansys.com.sg/tablet-pcs+ipads/' , 'http://www.expansys.com.sg/accessory-finder/' , 'http://www.expansys.com.sg/audio/' , 'http://www.expansys.com.sg/watches/' , 'http://www.expansys.com.sg/smart-gadget-offers/' , 'http://www.expansys.com.sg/action/cameras/']
  
  def parse(self, response)
    hxs = HtmlXPathSelector(response)
    dls = hxs.select('///dl')
    for dl in dls:
       

