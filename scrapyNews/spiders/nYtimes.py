import scrapy
from scrapyNews.items import NYtimesItem

class NYtimesSpider(scrapy.Spider):
	name="nYtimes"
	alllowed_domains=["nytimes.com"]
	start_urls = ["http://spiderbites.nytimes.com/free_2014/index.html"]
	baseURL1="http://spiderbites.nytimes.com"

	def parse(self,response):
		for url in response.xpath('//div[@class="articlesMonth"]/ul/li/a/@href').extract():
			yield scrapy.Request(self.baseURL1+url,callback=self.parseNews)

	def parseNews(self,response):
		News_urls =  response.xpath('//ul[@id="headlines"]/li/a/@href').extract()
		for url in News_urls:
			yield self.make_requests_from_url(url).replace(callback=self.parseSave)
		

	def parseSave(self,response):
		item = NYtimesItem()
		item["link"] = unicode(response.url)
		# 
		item["category"] = unicode(response.url.split("/")[-2])
		#
		item["title"] = unicode(response.xpath('//meta[@name="hdl"]/@content').extract()[0])
		# 
		item["author"] = unicode(response.xpath('//meta[@name="byl"]/@content').extract()[0])
		#
		item["date"] = unicode(response.xpath('//meta[@name="dat"]/@content').extract()[0])
		# 
		item["article"] = response.xpath('//p/text()').extract()
		return item
		
		

