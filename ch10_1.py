'''
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add their own VERB text anywhere the word ADJECTIVE, NOUN, ADVERB,
or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace them:

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
It would then create the following text file:

The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.
The program should print the results to the screen in addition to saving them to a new text file.# Write your code here :-)
'''


from pathlib import Path
import re
p = Path.cwd()
filepath = list(p.glob('*.txt'))
filename = 'Mad Libs.txt'
l = ''
with open(r'C:/Users/junke/mu_code/'+filename,'r', encoding='UTF-8') as MadLibs: # added filepath but make it dynamic or some search logic
    for words in MadLibs:
        l += words



for i in l:
    Vpattern = re.compile(r'VERB') #this part can change - now we need to FIND
    Vresult = Vpattern.findall(l)
    if Vresult:                         #added this as 'looker'
        for k in range(len(Vresult)):
            print('input VERB')
            x = input()
            l = Vpattern.sub(x,l)
            print(l)
    Apattern = re.compile(r'ADJECTIVE')
    Aresult = Apattern.findall(l)
    if Aresult:
        for k in range(len(Aresult)):
            print('input ADJECTIVE')
            x = input()
            l = Apattern.sub(x,l)
            print(l)
    Npattern = re.compile(r'NOUN')
    Nresult = Npattern.findall(l)
    if Nresult:
        for k in range(len(Nresult)):
            print(Nresult[k])
            print('input NOUN')
            x = input()
            l = Npattern.sub(x,l, count=k+1)
            print(l)
    ADVpattern = re.compile(r'ADVERB')
    ADVresult = ADVpattern.findall(l)
    if ADVresult:
        print('input ADVERB')
        x = input()
        l = ADVpattern.sub(x,l)
        print(l)

with open(r'C:/Users/junke/mu_code/'+'_processed_'+filename ,'w', encoding='UTF-8') as MadLibs: # writing as new file
    MadLibs.write(l)
