abc = []
abc += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,. abcdefghijklmnopqrstuvwxyz')
ABC = {}

#this is our dictionary - every letter or digit is a 3-digit code, digits with 2 letters are transformed into 3 digit variants to avoid problems with decryption
for i in abc:

    ABC.update({str(i):str(ord(i))})

for k,v in ABC.items():
    if len(str(v)) == 2:
        v = str(v) + '0'
        ABC[k] = v



#Encryption stage
text = ''
def encryptor(text):
    print('Please paste your message for encryption:')
    text = input()
    ENC = []
    for i in list(text):
        if i in ABC.keys():
            ENC += str(ABC[i])

    print(f'Your encoded message is {"".join(ENC)}')
    return(''.join(ENC))


#Decryption stage
def decryptor(text):
    print('Enter the text you would like to decrypt:')
    text = input()
    TEXT = []
    s = 3

    TEXT = [text[y:y+s] for y in range(0, len(text), s)] # awesome googled line, I was about to write something with for statement as well but this one is super nice :)
    #print(TEXT)

    DEC = []


    for i in TEXT:
        result = [key for key, value in ABC.items() if str(value) == str(i)] #at last this one works!!!!!
        DEC += result
    print(f'Your decoded message is {"".join(DEC)}')
    return(DEC)
while True:
    print('Welcome to my little entryption tool!\n If you would like to encrypt a message, paste enc\n If you would like to decrypt a message, paste dec')
    z = input()
    if z == 'enc':
        encryptor(text)
    elif z == 'dec':
        decryptor(text)
    elif z == '':
        print('Bye!')
        break


