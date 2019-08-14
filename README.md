# SuperScraper
scrapes data from comics website and compare with purchase to generate various information.\
For now, Crawls throgh rajcomics.com and crates a list of all comics present in the site

Python -3.6  
pip 18.1 from c:\python36\lib\site-packages\pip (python 3.6)  
Scrapy 1.5.1  

install jsonlines library to parse jl file output scraped data  
pip install jsonlines  
tutorial: https://jsonlines.readthedocs.io/en/latest/  

scrapy tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html  
'allowed_domains' used to restrict search within domain.  
'scrapy crawl SpiderMan -o output/comics1.jl' To output the scraped data  
output for now: one json objectof format{'comics':[comcisList]} per link.  

run the 'read.py' file to get a set(redundancy removed) of all names.[To be integrated as a single code in future].  

Next step: Enable login through code to get all the ordered products.  

13/8/19:
Added Login functionality Usin Formrequest class's from_response method: https://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects  
Had to use formxpath parameter to distinguish forms.  
also changed references to old project names to new one in config and settings.py file  

15/8/19:  
Getting ordered products after login.  

'scrapy crawl Venom -o output/orders.jl' To get output in output/orders.jl  
still not able to distinguish bet shipped/pending etc. 
To Do: Calling Spiderssss through API to integrate the report generato code(read.py) with spiders.

