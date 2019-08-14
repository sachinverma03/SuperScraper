import scrapy

class spiderMan(scrapy.Spider):
	name = 'SpiderMan'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php/login?task=user.login"]
	# def start_requests(self):
	# 	urls = ["https://www.rajcomics.com"]

	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		yield {'comics':response.css('div.vm-product-descr-container-1').css('a::Text').getall()}	#name from product decription div

		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if(not link.endswith('-detail')): #for individual products
				yield scrapy.Request(link, callback=self.parse)


class venom(scrapy.Spider):
	name = 'Venom'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php/login?task=user.login"]

	def parse(self, response):
		yield scrapy.FormRequest.from_response(response, formdata={'username': '5achin', 'password': 'vsachi-.'}, 
			formxpath = '//*[@id="rc-pagecontent"]/div/div/div/div[1]/form', callback=self.gotoOrders) #xpath generated from page
		

	def gotoOrders(self, response):
		yield scrapy.Request("https://www.rajcomics.com/index.php/account-maintenance/editaddress", callback = self.getOrders)

	def getOrders(self, response):
		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if('/orders/number/' in link): 
				yield scrapy.Request(link, callback=self.getDetail)

	def getDetail(self, response):
		yield {'order':response.css('div#tab-1').css('a::text').getall()}
