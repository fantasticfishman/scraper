import requests
from bs4 import BeautifulSoup
import os


#function to download images, given search term
def imagedown(search,page,index):
    #searches wallhaven for search term on specififed page
    url = 'https://wallhaven.cc/search?q='+search+'&page='+str(page)
    r = requests.get(url)
    #scrape html code from webpage
    soup = BeautifulSoup(r.text, 'html.parser')

    #finds all href image links
    figures = soup.find_all('figure')
    href = []
    for figure in figures:
        h = figure.find('a').get('href')
        href.append(h)
        print(h)
    
    #find link to full image, not thumbnail
    #if image is not a jpg, this will produce 404 error, 
    #in that case use png instead of jpg in the image link
    #then write to current directory, file name will be '(Search Term) (Index).png/jpg'
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
    #main function, runs when file is run
    ogdir = os.getcwd()
    #arg to check if they put a search term yet, page number, and index is the number to put after the downloaded photo
    arg = 'cringe'
    page = 1
    index = 1
    while(arg != 'quit'):
        #get the search term
        oldarg = arg
        arg = input('Enter your search term, type continue to go to the next page of your previous search term, or type quit to quit ')
        #exit if user says quit
        if(arg == 'quit'):
            print('see you next time')
            exit()
        elif(arg == 'continue' and oldarg == 'cringe'):
            print('baka')
            continue
            #if continue without selecting search term, try again because cannot go to next page
        if(arg == 'continue' and oldarg != 'cringe'):
            page += 1
            index = imagedown(oldarg,page,index)
            print('You are currently on page '+str(page))
            #continue and go to next page
        else:
            #if no other keywords, then search using input
            #check if search term has changed, if so make new dir and reset page and index
            if (arg != oldarg):
                page = 1
                index = 1
                #if image folder exists already because user searched this term before, 
                #then change directory to that folder and find largest index in that folder
                #all future downloaded images will have index larger than that so no duplicate filenames
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
                #if folder does not already exist create the directory and change to it
                    try:
                        os.chdir(ogdir)
                        os.mkdir(os.path.join(ogdir,arg))
                        os.chdir(os.path.join(ogdir,arg))
                    except:
                        pass
            #get page number
            try:
                #if user wants to go to specific page when searching, do same thing where check if folder already exists
                search = input('enter the page number you would like to go to or leave blank for page 1 ')
                if(search == ''):
                    page =  1
                else: 
                    page = int(search)
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
                #if page not given
                print('thats not a page baka')
                continue
            if(input == ''):
                #if page not specified
                page = 1
            #search for wallpaper and write to current directory, increment index
            index = imagedown(arg,page,index)

main()