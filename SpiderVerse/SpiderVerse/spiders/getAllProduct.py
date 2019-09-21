import scrapy

class spiderMan(scrapy.Spider):#collects all products available
	name = 'SpiderMan'
	allowed_domains = ["rajcomics.com"] # to prevent Spider to get out of the domain boundary and keep crawling indefinitely.
	start_urls = ["https://www.rajcomics.com/index.php"]

	##primtive/alternate way of initialisation of start urls.  
	# def start_requests(self):
	# 	urls = ["https://www.rajcomics.com"]

	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response): #parsing starts from start_urls
		yield {'comics':response.css('div.vm-product-descr-container-1').css('a::Text').getall()}	#names from product decription div

		links=response.css('a::attr(href)').getall() #gets all links in the present page.
		for link in links:
			link = response.urljoin(link)
			if(not link.endswith('-detail')): #individual products' links ends with -detail. since we are only interested with Names of all comics, we don't need to concern ourselves with other product detail.  
				yield scrapy.Request(link, callback=self.parse)
			

class spiderHam(scrapy.Spider): #searches specific attributes other than name.  
	name = 'SpiderHam'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php"]

	def parse(self, response):
		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if(not link.endswith('-detail')): #for links of non-individual products 
				yield scrapy.Request(link, callback=self.parse)
			else: #Individual products' links are sent to anither paerser which search for a given value in all the attributes of the product. 
				yield scrapy.Request(link, callback=self.search_attr)
		

	def search_attr(self, response):
		# productName = response.xpath('//*[@id="rajcomics-breadcrumb"]/div/div/div/ul/li[5]/span/text()').get().strip()
		productName = response.css('div.span12').css('h1::text').get()
		search_str = 'manu' #value to be searched. non case-sensitive.
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
	start_urls = ["https://www.rajcomics.com/index.php/login?task=user.login"] #starting from login page

	def parse(self, response):
		yield scrapy.FormRequest.from_response(response, formdata={'username': '', 'password': ''}, #usernaem and password needed to get the ordered products
			formxpath = '//*[@id="rc-pagecontent"]/div/div/div/div[1]/form', callback=self.gotoOrders) #xpath extracted from login page. 
		

	def gotoOrders(self, response): #Picks up individual orders and sends them to be parsed
		yield scrapy.Request("https://www.rajcomics.com/index.php/account-maintenance/editaddress", callback = self.getOrders)

	def getOrders(self, response):
		links=response.css('a::attr(href)').getall()
		for link in links:
			link = response.urljoin(link)
			if('/orders/number/' in link): 
				yield scrapy.Request(link, callback=self.getDetail)

	def getDetail(self, response):
		yield {'order':response.css('div#tab-1').css('a::text').getall()}
