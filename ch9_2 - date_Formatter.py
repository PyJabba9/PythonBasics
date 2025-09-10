'''Clean up dates in different date formats (such as 3/14/2030, 03-14-2030, and 2030/3/14)
by replacing them with dates in a single, standard format.
This is a common pain point for myself at my daily job so I will create something usefull (for me at last :D)

in general, it has to do following things:
1.Get text (probably I will try to go with the book example, where he was using  pyperclip to do all the work without playing around width - DONE
entering data into lists or strings explicitly.
2. Prepare regex logic:
    - Has to work with different date formats, as many as possible but we will start with simple ones like YYYY/MM/DD, MM/DD/YYYY, DD/MM/YYYY
    - Has to understand different date separators as well (-,/,.,) - for now will suffice, if anything weird comes up - will adjust
3. Make the program iterate through the text, substituting matched dates with correct ones
4. Substituting clipboard text with the list (separated into strings with \n every item from the list)
5. !!!!!!!!!!!!!!! optionally add some script to update date from 01/05/25 to 01/05/2025 format (for further correction) - TBD
'''

import pyperclip, re #kek works as inteded -copy something in the clipboard and get it printed - nice
'''

text = pyperclip.paste()

pyperclip.copy(text)
print(text)
'''
Y = 0
M = 0
D = 0
pos = 0
v = ''

DATELIST = []
DL = []
TEST_text = str(pyperclip.paste())
pattern = re.compile(r'''(
    (\d{4}|\d{2}) #2
    (\s|/|-|\.)
    (\d{4}|\d{2}) #4
    (\s|/|-|\.)
    (\d{4}|\d{2}) #6
    )''', re.VERBOSE)


for d in pattern.findall(TEST_text): #this part iterates through text and lists every match
    date = '/'.join([d[1],d[3],d[5]]) # its more fake it till you make it approach, I took it from the book :(
    DATELIST.append(date)

counter = 0


for i in DATELIST:
    print(i)
    for o,n in enumerate(i.split('/')): #Good one, taken from conversation with Claude, haven't thought about iterating it this way
        #print(o,n)

        if int(n) > 12 and len(n) != 4:
            DL.append(n)
            #print('DD position found')
            #print(o)
            if o == 0:
                v = '1st'
            elif o == 1:
                v = '2nd'
            elif o == 2:
                v = 'lst'
            continue
        elif len(n) == 4:
            #print('YYYY position found')
            #print(o)
            pos = o
        elif int(n) <= 12:
            DL.append(n)
            #print('MM position found')
            #print(o)



if int(max(DL)) <= 12: #error here

    print('What format do you think is in the text?:\n1.DD/MM/YYYY - input a \n2.MM/DD/YYYY - input b \n3.YYYY/DD/MM - input c \n4.YYYY/MM/DD - input d ')
    c = input()
    if c == 'a':
        v = '1st'
    if c == 'b':
        v = '2nd'
    if c == 'c':
        v = 'aftY'
    if c == 'd':
        v = 'lst'


#getting everything in the clipboard again

if v == '1st':
    print('All good, date is in  DD/MM/YYYY (EU) format')
    #pattern.sub(r'\2/\4/\6',TEST_text)
    pyperclip.copy(pattern.sub(r'\2/\4/\6',TEST_text))
elif v == '2nd':
    #pattern.sub(r'\4/\2/\6',TEST_text)
    pyperclip.copy(pattern.sub(r'\4/\2/\6',TEST_text))
elif v == 'aftY':
    #pattern.sub(r'\4/\6/\2',TEST_text)
    pyperclip.copy(pattern.sub(r'\4/\6/\2',TEST_text))
elif v == 'lst':
    #pattern.sub(r'\6/\4/\2',TEST_text)
    pyperclip.copy(pattern.sub(r'\6/\4/\2',TEST_text))

