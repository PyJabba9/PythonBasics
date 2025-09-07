# this is all for today - next will work on adding results into dictionary and some UI to search dictionary
# creating regex pattern to parse names, phones and emails of coworkers with some nice additions (task from claude LLM)

"""
John Smith: phone 123-456-7890, email john.smith@company.com
Maria Garcia: phone 987-654-3210, email maria.garcia@company.com
Bob Johnson: phone 555-123-4567, email bob.johnson@company.com
has to be transformed into
# Group 1: Name (John Smith)
# Group 2: Phone (123-456-7890)
# Group 3: Email (john.smith@company.com)
3. add everything into dictionary
4. additional UI like finder, etc
"""

import re
namebase = {'Name':'','Email':'','Phone':''}
DB = []
S = '''John Smith: phone 123-456-7890, email john.smith@company.com
Maria Garcia: phone 987-654-3210, email maria.garcia@company.com
Bob Johnson: phone 555-123-4567, email bob.johnson@company.com'''

name_pattern_obj = re.compile(r'(?:(?!:).)*') # had to google this one, constantly had a problem with : included in the name (then I found this solution)
phone_pattern_num_obj = re.compile(r'\d{3}-\d{3}-\d{4}') #works - EZ one as this regex was in the book
email_pattern_obj = re.compile(r'\w+[.]\w+@+\w+[.]+\w+') #EZ

ph = phone_pattern_num_obj.search(S)
#print(ph.group())

eml = email_pattern_obj.search(S)
#print(eml.group())

nm = name_pattern_obj.search(S)
#print(nm.group())

N = S.split('\n') # splitting multiline string by newlines
#print(N)



for i in N:

    ph = phone_pattern_num_obj.search(i)
    namebase.update({'Phone': ph.group()})

    eml = email_pattern_obj.search(i)
    namebase.update({'Email': eml.group()})

    nm = name_pattern_obj.search(i)
    s = nm.group()
    s = s.lower()
    namebase.update({'Name': s })

    DB += [namebase]
    namebase = {} # i figured out that you have to clear the dictionary after every iteration.
#print(DB)  # it works - 3 dictionaries in one list

#print(DB)

def printall():

    for o in DB:
        print('-------------------------')
        print(o['Name'].title())
        print(o['Email'])
        print(o['Phone'])


def databasefinder(): # databasefinder - workis with any case (upper or lower will be transformed into lower and then back to title once printed.
    print('Enter Email (name.surname@company.com) \n either (Name Surname) \n Or phone number (xxx-xxx-xxxx format)')
    x = input()   #this is working finder !!!! + add into UI as soon as other is done
    x = str(x.lower())



    outcome = 0
    for o in DB:
        for m in range(len(o.items())):
            if x in o.values():
                outcome += 1
                print(o['Name'].title())
                print(o['Email'])
                print(o['Phone'])
                break

    if outcome == 0:
        print('Not found')



while True:
    print('Welcome to my database of workers, in order to look for someone, please input "find"\n In order to print whole database, input "all"\n to exit the program, input "exit"')
    b = input()
    if b == 'find':

        databasefinder()
    elif b == 'all':
        printall()
    elif b == 'exit':
        break

databasefinder()
