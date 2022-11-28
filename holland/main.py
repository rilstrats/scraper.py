import requests
from bs4 import BeautifulSoup

URL = 'https://www.churchofjesuschrist.org/study/general-conference/speakers/jeffrey-r-holland?lang=eng'

page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')

main = soup.find(id='main')

raw_links = main.find_all('a')

links = []
for link in raw_links:
    links.append(f'https://www.churchofjesuschrist.org/{link["href"]}')





