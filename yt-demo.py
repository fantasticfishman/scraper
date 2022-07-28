import requests
from bs4 import BeautifulSoup
import os

search = input('enter your search term dummy ')
searchurl = search.replace(' ','+')
url = 'https://wallhaven.cc/search?q='+search
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')
count = 0
for image in images:
    link = image.get('data-src')
    check = image['alt']
    if(check == 'wallhaven'):
        continue
    else:
        name = str(count)
        with open(search+name+'.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
        count +=1