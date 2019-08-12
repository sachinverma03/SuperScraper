import scrapy

class spiderMan(scrapy.Spider):
	name = 'SpiderMan'
	allowed_domains = ["rajcomics.com"]
	start_urls = ["https://www.rajcomics.com/index.php/login?task=user.login",]
	# def start_requests(self):
	# 	urls = ["https://www.rajcomics.com"]

	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)


	def parse(self, response):
		yield scrapy.FormRequest.from_response(response, formdata={'username': '5achin', 'password': 'vsachi-.'}, 
			formxpath = '//*[@id="rc-pagecontent"]/div/div/div/div[1]/form',
                    callback=self.after_post)
		

	def after_post(self, response):
		 print(response.css('a::text').getall())
		# yield {'comics':response.css('div.vm-product-descr-container-1').css('a::Text').getall()}	#name from product decription div

		# links=response.css('a::attr(href)').getall()
		# for link in links:
		# 	link = response.urljoin(link)
		# 	if(not link.endswith('-detail')): #for individual products
		# 		yield scrapy.Request(link, callback=self.parse)