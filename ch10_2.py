"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression, then prints the results to the screen.

1. check the active folder - move to destination folder ('C:/Users/junke/mu_code/TestFolder') # even when hashed out - still causes erorrs if reversed slash is used :(
2. function to list all files (can find ext like .txt)
3. add their path's to the list and iterate through the contents of those files
4. in iteration look for "REGEX PROVIDED BY USER" in string(contents).
5. if found - print filename, path

"""




from pathlib import Path
import re

print('Welcome to my word finder, it will look through .txt files in the folder and find matches for the phrase you will add below.')
p = input('Your phrase: ')
Song_pattern = re.compile(p.lower()) #add looker here

#P = 'C:/Users/junke/mu_code/TestFolder'
for files in Path('C:/Users/junke/mu_code/TestFolder').glob('*.txt'):
    #print(files)
    with open(files,'r', encoding = 'utf-8') as Lyrics_Finder:
        content = Lyrics_Finder.read()
        Sresult = Song_pattern.findall(content.lower()) # lower makes sure it finds everything

        if Sresult:
            print(r'Found Match! File name: ' + str(files))
            print(Sresult)
        else:
            print(r'No results found in file' +str(files))
