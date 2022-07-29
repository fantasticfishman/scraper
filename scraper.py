import requests
from bs4 import BeautifulSoup
import os


def imagedown(search,page,index):
    #searchurl = search.replace(' ','+')
    url = 'https://wallhaven.cc/search?q='+search+'&page='+str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    figures = soup.find_all('figure')
    href = []
    for figure in figures:
        h = figure.find('a').get('href')
        href.append(h)
        print(h)
        
    count = index
    for link in href:
        name = str(count)
        imageID = link[23:]
        imageIDshort = imageID[:2]
        src = 'https://w.wallhaven.cc/full/'+imageIDshort+'/wallhaven-'+imageID+'.jpg'

        check = src
        if(requests.get(check).status_code == 404):
            src = 'https://w.wallhaven.cc/full/'+imageIDshort+'/wallhaven-'+imageID+'.png'
            with open(search+' '+name+'.png', 'wb') as f:
                im = requests.get(src)
                f.write(im.content)
        else:
            with open(search+' '+name+'.jpg', 'wb') as f:
                im = requests.get(src)
                f.write(im.content)
        count+=1
    return count


def main():
    ogdir = os.getcwd()
    arg = 'cringe'
    page = 1
    index = 1
    while(arg != 'quit'):
        #get the search term
        oldarg = arg
        arg = input('Enter your search term, type continue to go to the next page of your previous search term, or type quit to quit ')
        #exit
        if(arg == 'quit'):
            print('see you next time')
            exit()
        elif(arg == 'continue' and oldarg == 'cringe'):
            print('baka')
            continue
            #if continue without selecting search term
        if(arg == 'continue' and oldarg != 'cringe'):
            page += 1
            index = imagedown(oldarg,page,index)
            print('You are currently on page '+str(page))
            #continue
        else:
            #if no keywords, then search
            #check if search term has changed, if so make new dir and reset everything
            if (arg != oldarg):
                page = 1
                index = 1
                if(os.path.exists(os.path.join(ogdir,arg))):
                    os.chdir(os.path.join(ogdir,arg))
                    largest = 0
                    for file in os.listdir(os.path.join(ogdir,arg)):
                        filename = os.fsdecode(file)
                        check = int(filename[filename.rfind(' ')+1:-4])
                        if(check > largest):
                            largest = check
                    print(largest)
                    index = largest+1
                else:
                    try:
                        os.chdir(ogdir)
                        os.mkdir(os.path.join(ogdir,arg))
                        os.chdir(os.path.join(ogdir,arg))
                    except:
                        pass
            #get page number
            try:
                page = int(input('enter the page number you would like to go to or leave blank for page 1 '))
                if(os.path.exists(os.path.join(ogdir,arg))):
                    os.chdir(os.path.join(ogdir,arg))
                    largest = 0
                    for file in os.listdir(os.path.join(ogdir,arg)):
                        filename = os.fsdecode(file)
                        check = int(filename[filename.rfind(' ')+1:-4])
                        if(check > largest):
                            largest = check
                    print(largest)
                    index = largest+1
                else:
                    try:
                        os.chdir(ogdir)
                        os.mkdir(os.path.join(ogdir,arg))
                        os.chdir(os.path.join(ogdir,arg))
                    except:
                        pass
            except:
                print('thats not a page baka')
                continue
            if(input == ''):
                page = 1
            #search for wallpaper and write to current directory, increment index
            index = imagedown(arg,page,index)

main()