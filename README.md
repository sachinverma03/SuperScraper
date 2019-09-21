# SpiderVerse
Aim:\
  Personal project to help make informed choices while buying comics.\
About:\
scrapes data from comics website and gives out useful information.\
Features to date:\
Crawls throgh comics website and collects name of all available comics, ordered comics, or comics with a given attribute value.\ 
Compares them to give out names of all comics already purchased, available but not bought, bought but unavailable, in geral or for a specific search value.\

Language/Framework/Libraries used:\
  Python -3.6  \
  pip 18.1 from c:\python36\lib\site-packages\pip (python 3.6)  (to install other frameworks.)\

  Scrapy 1.5.1  (Creates the backbone of project. Framework used to scrape data.)\
  scrapy tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html \ 

  Both the  python and Scrapy should be added to Systems' Environment path variable if we want to run them from anywhere. \  

  
  jsonlines library to parse jl file output from scrapy Spiders\ 
  run in cmd: pip install jsonlines  \
  (Not in-depth knowledge needed, just how to read the jl files using this library)\
  tutorial: https://jsonlines.readthedocs.io/en/latest/  \
  
  Any text editor or IDE which supports python. Sublime Text 3 was used originally but is not to be claimed as the best and only option.\

Project structure:\
  It is recommended to go through scrapy's quick tutorial to understand basic scrapy project structure.\
  The project was created by running the 'scrapy startproject project_name' command in cmd\
  Most of the files were generated automatically and are not used explicitly for now.\
  Initially the root folder(Where you created the project by runnin the startproject command) Contained the SpiderVerse(initially created as SuperScraper. More on name change in Misc.) and scrapy.cfg folder.\

  Inside SpiderVerse we have different .py files as explained in official Scrapy tutorial, but we won't need to be concerned with those for now\
  along with the .py files we have spiders folder here which carries all the spiders(These are the Heroes who will be scraping the data for us).\
  The spiders folder contains the 'getAllProduct.py' which holds the definition of our SpiderGuys.\
  Presently the output of the spiders are stored in the 'output' folder in the root folder as .jl files.\
  The 'read.py' File is a script which, once the spiders have collected all the required data, is run to genrate reports.\
  
  Final Structure- \
    * --> not generated automatically from startproject command.\
      SpiderVerse/
          scrapy.cfg            # deploy configuration file\
        * read.py\
        * output\
              .jl files with spiders' output\
          SpiderVerse/             # project's Python module.\
              __init__.py\
              items.py          # project items definition file\
              middlewares.py    # project middlewares file\
              pipelines.py      # project pipelines file\
              settings.py       # project settings file\
              spiders/          # a directory where you'll later put your spiders\
                  __init__.py\
                * getAllProduct.py(Contains the Spiders. Read the documetation in code to get more information about individual spiders)\
 
 How to run:\
   In the root folder(one containing the scrapy.cfg file.) type cmd in address bar to open cmd or you can navigate to this folder after opening cmd.\
   run the cmd: 'scrapy crawl Spider_name -o output/file_name.jl' to run the desired spiders. crawling may(will definitely) take some (maybe a lot of)time.\\
   For Example: 'scrapy crawl SpiderMan -o output/comics1.jl'. gives the name of all  products available on rajcomics.com\
   the same file_name must be used in read.py to fetch corresponding data.\
  output for now: one json object of format{'comics':[comcisList]} per link. We don't Interact with these files directly but via read.py.  \
  It's not necessary to run all the Spiders, only what are required. For Example if we just want the list of available comics, running SpiderMan is sufficient. we just need to comment out the code from read.py which refers/depends to the other Spiders' output.\
  Once all the required spiders are run and the required data is collected, run the 'read.py' file to get a set(redundancy removed) of all names.  \

Misc:\
  To change the name of project in addition to changing the folder name we had to change the name of all refernce in the settings.py and scrapy.cfg to new name in corresponding casing.\
  Scrapy takes care of Duplicate links i.e. makes sure we don't visit same link twice.\
  \
To Dos/ Can be dones:\
  Add Holy cow entertainment and Fenil comics as well.   \
  Date wise matching of available products to spot new additions or sold out goods.   \
  Integerating Spiders annd read.py script to reduce manual work.   \
  combine specific search spider(SpiderHam) and general collector spider(SpiderMan).\
Logs:\
  13/8/19:\
    Added Login functionality Using Formrequest class's from_response method: https://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects  \
    Had to use formxpath parameter to distinguish forms.  \
    also changed references to old project names to new one in config and settings.py file  \
\
\
  15/8/19:\  
    Getting ordered products after login.  \
    'scrapy crawl Venom -o output/orders.jl' To get output in output/orders.jl \ 
    still not able to distinguish bet shipped/pending etc. \
    To Do: Calling Spiderssss through API to integrate the report generato code(read.py) with spiders.\  
    https://docs.scrapy.org/en/latest/topics/practices.html#run-from-script\
  
  

