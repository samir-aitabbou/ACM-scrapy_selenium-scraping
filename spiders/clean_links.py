import pandas as pd
import re


df = pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/links.csv')
start_urls = df['link'] 

clean_links = []

regex = re.compile('AZERTYUIOPQSDFGHJKLMWXCVBN')

for url in start_urls:
    cdt = False
    for element in str(url):
        if(element in "nAZERTYUIOPQSDFGHJKLMWXCVBN"):
            cdt = True    
    if (cdt == False) and (not('s0' in str(url))):
        clean_links.append(url)


print("lenght :    ",len(clean_links))



dict = {'links': clean_links}
df_new = pd.DataFrame(dict) 
df_new.to_csv('cleaned_links.csv')