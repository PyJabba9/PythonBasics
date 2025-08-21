
while True:
    print('Who are you?')
    name = input('>')

    if name =='Toad':
        print('Hello '+ name +' What is the password?')
        password = input('>')
        if password =='frog':
            print('Access granted ' + name)
            break
        else:
            print('Wrong password, you are not ' + name)
    else:
        print('I dont know you')
