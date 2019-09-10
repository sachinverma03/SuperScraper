import scrapy

class spiderMan(scrapy.Spider):#collects all products available
	name = 'SpiderMan'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php"]
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
			

class spiderHam(scrapy.Spider): #searches specific attributes
	name = 'SpiderHam'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php"]

	def parse(self, response):
		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if(not link.endswith('-detail')): #for individual products
				yield scrapy.Request(link, callback=self.parse)
			else:
				yield scrapy.Request(link, callback=self.search_attr)
		

	def search_attr(self, response):
		# productName = response.xpath('//*[@id="rajcomics-breadcrumb"]/div/div/div/ul/li[5]/span/text()').get().strip()
		productName = response.css('div.span12').css('h1::text').get()
		search_str = 'manu'
		matched_product = []
		attr_list = []
		
		for attr in response.css('div.product-isbn::Text').getall():
			if(search_str.lower() in attr.lower().strip()):
				matched_product.append(productName)
				break

		yield {'comics':matched_product}




class venom(scrapy.Spider): #collects all orders
	name = 'Venom'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php/login?task=user.login"]

	def parse(self, response):
		yield scrapy.FormRequest.from_response(response, formdata={'username': '', 'password': ''}, 
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
