import pandas as pd


# all_links = pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/cleaned_links.csv')
# articles_infos= pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/articles_infos.csv')
all_links = pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/unvisited_links.csv')
articles_infos= pd.read_csv('/home/aitabbou/Desktop/scraping_project/my_projects/Acm/Acm/articles_infos_2.csv')

all_links = all_links["links"]
visited_links  = articles_infos['dio'] 

# c=0
# for url in all_links:
#     c+=1
#     print(url)
#     print("\n",c)


unvisited_links2 = []
# c=0
for url in all_links:
    if not any(url in x  for x in visited_links):
    #if not(url in visited_links):
        # c+=1
        # print("*************"url)
        # print("\n",c)
        unvisited_links2.append(url)


print("all_links lenght :    ",len(all_links))
print("\n")
print("visited_links lenght :    ",len(visited_links))
print("\n")
print("unvisited_links lenght :    ",len(unvisited_links2))



dict = {'links': unvisited_links2}
df_new = pd.DataFrame(dict) 
df_new.to_csv('unvisited_links2.csv')