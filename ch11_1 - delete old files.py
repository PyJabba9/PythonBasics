'''
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB AND HAVENT BEEN UPDATED FOR 3 MONTHS
(Remember that, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.


1. It will be a function - so I can pass a folder path and it runs through it printing all files with set conditions (over 100MB + last change >= 90 days from today)
2. logic for storing matches? list? dictionary? how to relate and delete later? - if dictionary - can store path (and call by name to delete if needed)
key = path; value = list of size and datetime

'''

def filecleaner(folder,howold,S):   #S - threshold size of the file to look for, howold - how many days old the file has to be to be selected for deletion, folder - path to the folder)



    folder = Path(folder)
    L = []
    FD = {}
    reply = 0
    for folder_name, subfolders, filenames in os.walk(folder):
    #    print(type(folder_name)) # str
    #    print(type(subfolders)) # list
    #    print(type(filenames)) # list
    #    print(type(folder)) # path - works

        L += list(folder.glob('*')) # list of all paths to all files in all directories in the folder

    for files in L:
        size = os.path.getsize(files)/1024**2
        DT = datetime.datetime.fromtimestamp(files.stat().st_mtime)
        #print(files.stat().st_mtime)
        dt = DT.date()
        delta = (datetime.datetime.now() - datetime.timedelta(days=howold)).date()
        #FD.setdefault(files,[int(size),DT.date()])
        if size >= S and dt <= delta:
            targetfilesize = size
            targetfilename = files
            targetfiledate = DT
            FD.setdefault(files,[int(size),DT.date()])



    print(list(FD))
    print('---------------------------------')
    deleteall = False

    for key, value in FD.items():
        print(f'File Path: {key}\nFile Size {value[0]} MB\nFile Last update date: {value[1]}')
        print('Do you want to delete this file?y/n?\nIf you want to delete everything, type all')
        r = input()
        if r == 'y':
            send2trash.send2trash(Path(key))
            print('File moved to trash')
            reply +=1
        elif r == 'n':
            print('OK')
            continue
        elif r == 'all':
            deleteall = True
            break
            reply +=1
    try:
        for key, value in FD.items():
            if deleteall == True:
                send2trash.send2trash(Path(key))
                print(f'File {key} moved to trash')
                reply +=1
            else:
                break
    except:
        print(f'Error while deleting {e}') # taken from GPT :) - looks kool I guess
    if reply == 0:
        print('File not found')

import os, datetime, time, send2trash, pyperclip
from pathlib import Path
AA = ''
clip = ''

print('Welcome to my foldercleaner, please provide several values before we start to clean up your folder')
print('Please provide path to the folder you would like me to analyze and look for old and big files to be deleted. Either paste it manually after typing "type" or I can take it from your clipboard - type "clip"')
AA = input()
if AA == 'type':
    print('Now type file path here:')
    folder = input()
    if '\\' in folder:
        print('please use "/" as a folder path separator, thanks')
        print('Now type file path here:')
        folder = input()
elif AA == 'clip':
    folder = pyperclip.paste()
    print(f'Your folder is: {folder}')
else:
    print('Wrong input, please type again')
    folder = input()
print('Now please enter the size of the file you would like to to search for(in Megabytes - 100 will mean 100MB) - I will look for this size or bigger files')

while True:
    try:
        S = input()
        S = int(S)
        break
    except:
        print('This has to be a number! Please try again')


print('And finally,how old (in days) those files have to be? I will look for this old and older files (e.g 10 os 10 days old)')
while True:

    try:
        howold = input()
        howold = int(howold)
        break
    except:
        print('This has to be a number! Please try again')
        howold = input()

filecleaner(folder,howold,S)

