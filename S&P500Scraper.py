from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table',{'class':'wikitable sortable', 'id':'constituents'})

file = open('S&P500Symbols.txt','w')

for i in table.find_all('tr'):
    file.write(i.get_text().split()[0] + "\n")


file.close()