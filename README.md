# Wallpaper Downloader

Ever got sick of opening in new tabs and downloading a bunch of seperate files when searching for a wallpaper? Do you also get sick of organizing them by folder,
or moving them from downloads? This will solve all your problems.

#Installation

Just clone this repo, and cd into it.
Then all you have to do is open the terminal, and type "python(orpython3)scraper.py". You will then be prompted 
"Enter your search term, type continue to go to the next page of your previous search term, or type quit to quit".

#Usage

Typing your search term will create a new folder in the root directory with the name of your search term, and files in it will be titled "SEARCHTERM+INDEX".

Then once that finishes you will be prompted again "Enter your search term, type continue to go to the next page of your previous search term, or type quit to quit".

The nice thing is that if you continue from the current search, the index will continue incrementing and no duplicate files will be created. 
You can also switch to a different search term, and if you go back to your first search term, the first term's index will be saved.

For example, if I were to first search "Rem", I would get this. 

![image](https://user-images.githubusercontent.com/40068612/186287997-2312e054-db1a-4977-9384-a0278ca8b606.png)

If I were to continue when prompted, I would get 24 more images in that folder, starting from rem 25. 

![image](https://user-images.githubusercontent.com/40068612/186288217-745a2182-ba98-47b5-aadf-bac6f0c463c5.png)

If I were to search for another wallpaper, say "Miku Nakano",
then I would get a folder titled "Miku Nakano" with 24 of those wallpapers. 

![image](https://user-images.githubusercontent.com/40068612/186288367-7b42d1f5-ddfd-4c64-bda0-b66c4629df73.png)

And if I were to search for a wallpaper of "Rem", it would not create another folder,
but search the directory for a folder of that name, check the highest index, and start titling the images from there. In this case the first new image would
be called rem 49. 

Note that this downloader works by grabbing all the images from one page of a search from wallhaven, a wallpaper site. If you've already visited a page, then
you can just specify the page that you want to go to next.

That's about all. Have fun!
