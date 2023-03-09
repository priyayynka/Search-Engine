import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.tutorialspoint.com/')
soup = BeautifulSoup(r.content, 'html.parser')

count = 0

for ul in soup.find_all('ul', id='hslider'):
    for li in ul.find_all('li'):
        count+=1
        print(count)
        a = li.find('a') 
                       

        print("\n", a.get_text(),"\n\n")