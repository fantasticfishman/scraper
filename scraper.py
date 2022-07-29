import requests
from bs4 import BeautifulSoup
import os

def imagedown(search):
    try:
        os.mkdir(os.path.join(os.getcwd(),search))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),search))
    #searchurl = search.replace(' ','+')
    url = 'https://wallhaven.cc/search?q='+search
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    figures = soup.find_all('figure')
    href = []
    for figure in figures:
        h = figure.find('a').get('href')
        href.append(h)
        print(h)
        
    count = 0
    for link in href:
        name = str(count)
        imageID = link[23:]
        imageIDshort = imageID[:2]
        src = 'https://w.wallhaven.cc/full/'+imageIDshort+'/wallhaven-'+imageID+'.jpg'

        check = src
        if(requests.get(check).status_code == 404):
            src = 'https://w.wallhaven.cc/full/'+imageIDshort+'/wallhaven-'+imageID+'.png'
            with open(search+name+'.png', 'wb') as f:
                im = requests.get(src)
                f.write(im.content)
        else:
            with open(search+name+'.jpg', 'wb') as f:
                im = requests.get(src)
                f.write(im.content)
        count+=1
        
imagedown(input('enter your search term baka ') )