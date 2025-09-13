'''
Strong Password Detection
#1 - done
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password has several rules:
it must be at least eight characters long,
contain both uppercase and lowercase characters,
and have at least one digit.
#2 - done
need to add logic for checking same letter being used in password too much - for example AAAAAAAAAAAAAAAAAAAaaa222! is correct from the perspective of my checker
but is it safe? https://www.passwordmonster.com/ -  % of same symbol usage is key - if same symbol used more than say >=50%
of the whole phrase - ask to change pass
#3 - done
check common keyboard combinations - "qwerty" thing for the whole keyboard. - done


'''

import re, pyperclip
PS = []

def passwcheck(passwd):

    seq = '1234567890qwertyuiopasdfghjklzxcvbnm0987654321poiuytrewqlkjhgfdsamnbvcxz'
    passw_pattern_dig = re.compile(r'\d+') #at least 1 digit part goes below

    if re.search(passw_pattern_dig,passwd):
        #print(passw_pattern_dig.findall(passwd))
        dig = True
    else:
        print('No digits found in the password')

    passw_pattern_len = re.compile(r'.{8,}') #at least 8 characters long

    if re.search(passw_pattern_len,passwd):
        #print(passw_pattern_len.findall(passwd))
        _len = True
    else:
        print('You password has to be at least 8 characters long')

    passw_pattern_uplow = re.compile(r'[A-Z]+') #at least 1 uppercase character

    if re.search(passw_pattern_uplow,passwd):
        #print(passw_pattern_uplow.findall(passwd))
        uplow = True
    else:
        print('You password has to have at least 1 uppercase character')
    passw_pattern_low = re.compile(r'[a-z]+') #at least 1 lowercase character

    if re.search(passw_pattern_low,passwd):
        #print(passw_pattern_low.findall(passwd))
        low = True
    else:
        print('You password has to have at least 1 lowercase character')

    passw_pattern_specc = re.compile(r'\S\W') #at least 1 special character

    if re.search(passw_pattern_specc,passwd):
        #print(passw_pattern_specc.findall(passwd))
        specc = True
    else:
        print('You password has to have at least 1 special character')

    passw_pattern_nospace = re.compile(r'\s') #no spaces or tabs

    if re.search(passw_pattern_nospace,passwd):
        print('You password cannot have spaces and tabs')
    else:
        #print(passw_pattern_nospace.findall(passwd))
        nospace = True


    PS = []
    PS = passwd
    PS2 = PS.lower()
    if any(PS2.count(x) >= len(PS2)//2 for x in PS2): # checking duplicated symbols
        nodup = False
        print('Your password has too many same symbols, please make it more complex')
    else:
        #print('Your password is OK')
        nodup = True

    for i in range(len(passwd)):  # checking sequence of the characters in keyboard to avoid EZ crack
        phrase = passwd[i:i+4]

        if phrase.lower() in seq:
            print('Your password contains keyboard sequence that is easy to crack, please avoid those - "QWERTY", etc')
            seqnc = False
            break
        else:
            seqnc = True
    try:
        if (dig and _len and uplow and specc and nospace and low and nodup and seqnc) == True:
            print('Your password is OK, you have it in your clipboard ;)')
            pyperclip.copy(passwd)
        else:
            print('Your have errors in your password, please try new one')
    except:
        print('Your have errors in your password, please try new one')


reply = ''

print('Welcome to my password checking tool!\nPlease type pass and input your password\nAlternatively, please copy your password into clipboard (CTRL+C) and type copy\nBlank input - exit')
while True:
    reply = input()
    if reply == 'pass':
        print('Please type your password here for checking')
        a = input()
        passwcheck(a)
    elif reply == 'copy':
        print('Got your password from the clipboard')
        print(r'Your password is ' + pyperclip.paste())
        a = str(pyperclip.paste())
        passwcheck(a)
    elif reply == '':
        print('Bye')
        break
    else:
        print('Wrong command, please type again')
