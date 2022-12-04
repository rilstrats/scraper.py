import requests
from bs4 import BeautifulSoup

PREFIX = 'https://www.churchofjesuschrist.org'
# URL = PREFIX + '/study/general-conference/speakers/jeffrey-r-holland?lang=eng'
URL = PREFIX + '/study/general-conference/speakers/russell-m-nelson?lang=eng'


page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')

main = soup.find(id='main')

links = main.find_all('a')

with open('output.txt','w') as outfile:

    for link in links:
        print(PREFIX + link['href'])
        sub_page = requests.get(PREFIX + link['href'])
        sub_soup = BeautifulSoup(sub_page.content, 'html.parser')

        title = sub_soup.find(id='title1')
        # print(title.text)
        outfile.writelines(title.text.upper()+'\n\n')

        bodies = sub_soup.find_all('div', class_='body-block')

        for body in bodies:
            ps = body.find_all('p')

            for p in ps:
                # print(p.text)
                outfile.writelines(p.text+'\n\n')

        outfile.write('\n\n')

    outfile.writelines('')
    



