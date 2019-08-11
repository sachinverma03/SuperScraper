import scrapy

class spiderMan(scrapy.Spider):
	name = 'SpiderMan'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com"]
	# def start_requests(self):
	# 	urls = ["https://www.rajcomics.com"]

	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		yield {'comics':response.css('div.vm-product-descr-container-1').css('a::Text').getall()}

		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if(not link.endswith('-detail')):
				yield scrapy.Request(link, callback=self.parse)