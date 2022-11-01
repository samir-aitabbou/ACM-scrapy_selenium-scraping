import scrapy
import time
from selenium import webdriver
import pandas as pd
import csv
from selenium.webdriver.common.by import By


#webdriver with selenium 4::
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class ArticlesInfosSpider(scrapy.Spider):
    name = 'articles_infos'

 
    # opening the CSV file
    # with open('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/spiders/cleaned_links.csv', mode ='r')as file:
    
    # # reading the CSV file
    # csvFile = csv.reader(file)
    # start_urls = csvFile['links']
    
    # # displaying the contents of the CSV file
    # # for lines in start_urls:
    # #         print(lines)

    # df = pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/spiders/cleaned_links.csv')
    # global start_urls 
    # start_urls = df['links'] 

    try:
        with open("cleaned_links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = [] 

   
    def start_requests(self):
        headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        # for url in self.start_urls:
        #     print(" ********************* RAHAAAAAAAAAAAAA ! **********************")
        #     time.sleep(5)
        #     print("#################### JME3333333333333333333333333 #################")
        #     print("$$$$$$$$$$$$$$$$$$$$$$$$",url)
        #     yield scrapy.Request(url, headers=headers, callback=self.parse)
        yield scrapy.Request(start_urls[0], headers=headers, callback=self.parse)



            
    def parse(self, response):
        #print("****************************",response.request.url)
        #each url is gathered from response.request object
        time.sleep(3)
        driver.get(response.request.url)
        time.sleep(3)
            
        title = driver.find_element(By.XPATH,'//h1[@class="citation__title"]').text
         #Author name is taken here. Since there are multiple authors in some articles, these are lists of elements
        pub_date = driver.find_element(By.XPATH,'//span[@class="CitationCoverDate"]').text
        citation = driver.find_element(By.XPATH,'//span[@class="citation"]//span').text
        downloads = driver.find_element(By.XPATH,'//span[@class="metric"]//span').text
        #Abstract of the article we have try except here since some of the articles does not have abstract and we set its initial value to none
        abstract = "None"
        try:
            abstract = driver.find_element(By.XPATH,'//div[@class="abstractSection abstractInFull"]//p').text
        except:
            pass
        dio = driver.find_element(By.XPATH,'//a[@class="issue-item__doi"]').text

        #In order to reach the location info a button on the page must be triggered to fire embedded JavaScript code in order to 
        #make the page generate a div element that contains location info
        driver.execute_script("document.getElementsByClassName('loa__link w-slide__btn tab-link')[0].click()")
        time.sleep(2)
        
        #Location is here. Since there are multiple contributing institutions in some articles, this is a list of elements
        author_name = driver.find_elements(By.XPATH,'//div[@class="auth-info"]//span[@class="auth-name"]//*')
        location = driver.find_elements(By.XPATH,'//div[@class="auth-info"]//span[@class="info--text auth-institution"]')
        
        #Empty arrays to be filled with texts stored in each element in the lists gathered above.
        authors_name = []
        auths_institution =[] 
        auths_per_institution = []

        # Necessary loops to extract texts from previously gathered lists and to be stored as array of texts.
        for au in author_name:
            authors_name.append(au.text)
            # print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm ",au.text)
            # print("\n")
        
        for lo in location:
            auth_institution = lo.text.rsplit(',', 1)[-2]
            auths_institution.append(auth_institution)
        
        for au in range(len(authors_name)):
            au_inst = "("+authors_name[au]+")"+" FROM "+"("+auths_institution[au]+")"
            auths_per_institution.append(au_inst)

        # get unique contries 
        unique_contries = []
        countries = []

        for lo in location:
            country = lo.text.split(",")[-1].lstrip()
            countries.append(country)

        for cont in countries:
            if cont not in unique_contries:
                unique_contries.append(cont)

        # Yielding takes place in each location element since we need our data to reflect number of contributions from countries among the world
        for lo in unique_contries:
            yield {
                'title':title,
                'authors_name':authors_name,
                'auths_institution':auths_institution,
                'auths_per_institution':auths_per_institution,
                'abstract':abstract,
                'location':country,
                'pub_date':pub_date,
                'citation_nbres':citation,
                'download_nbres':downloads,
                'dio':dio
            }

