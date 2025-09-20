'''
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB AND HAVENT BEEN UPDATED FOR 3 MONTHS
(Remember that, to get a file’s size, you can use os.path.getsize() from the os module.)
Print these files with their absolute path to the screen.


1. It will be a function - so I can pass a folder path and it runs through it printing all files with set conditions (over 100MB + last change >= 90 days from today)
2. logic for storing matches? list? dictionary? how to relate and delete later? - if dictionary - can store path (and call by name to delete if needed)
key = path; value = list of size and datetime




'''
import os, datetime, time
from pathlib import Path
folder = 'C:/Users/junke/Downloads'
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
    delta = (datetime.datetime.now() - datetime.timedelta(days=9000)).date()


    if size >= 100 and dt <= delta:
        targetfilesize = size
        targetfilename = files
        targetfiledate = DT
        FD.setdefault('File: '+str(targetfilename),['Size: '+str(int(targetfilesize))+' MB','Date of creation: '+str(DT.date())])





for key, value in FD.items():
    if value:
        print('Files found!')
        print(f'{key}:{value}')
        print('Do you want to delete those elements?')
        print(FD)
        reply +=1



if reply == 0:
    print('File not found')
