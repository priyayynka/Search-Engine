import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/c-programming-language/?ref=shm')
soup = BeautifulSoup(r.content, 'html.parser')

count = 0

for ul in soup.find_all('ul', class_='leftBarList'):
    for li in ul.find_all('li'):
        count+=1
        print(count)
        a = li.find('a')

        for para in soup.find_all("p"):
            print(para.get_text())    
                       

        print(a['href'],"\n", a.get_text(),"\n","\n\n")