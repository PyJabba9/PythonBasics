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

S = '''John Smith: phone 123-456-7890, email john.smith@company.com
Maria Garcia: phone 987-654-3210, email maria.garcia@company.com
Bob Johnson: phone 555-123-4567, email bob.johnson@company.com'''

name_pattern_obj = re.compile(r'(?:(?!:).)*') # had to google this one
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
    print(ph.group())

    eml = email_pattern_obj.search(i)
    print(eml.group())

    nm = name_pattern_obj.search(i)
    print(nm.group())
