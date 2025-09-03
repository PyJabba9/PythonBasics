abc = []
abc += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,. abcdefghijklmnopqrstuvwxyz')
ABC = {}

#this is our dictionary - every letter or digit is a 3-digit code, digits with 2 letters are transformed into 3 digit variants to avoid problems with decryption
for i in abc:

    ABC.update({str(i):ord(i)})

for k,v in ABC.items():
    if len(str(v)) == 2:
        v = str(v) + '0'
        ABC[k] = v



#Encryption stage
text = ''
def encryptor(text):
    ENC = []
    for i in list(text):
        if i in ABC.keys():
            ENC += str(ABC[i])

    print(f'Your encoded message is {"".join(ENC)}')
    return(''.join(ENC))

print('Enter your message for encryption:')
text = input()

encryptor(text)
