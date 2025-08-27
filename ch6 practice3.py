#Say you have a list value like this:

#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all the
#items separated by a comma and a space, with and inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.
#Be sure to test the case where an empty list [] is passed to your function
import copy

def lister(L):
    L = copy.copy(L)
    p = ''


    if '' in L and len(L) == 1:
        print('List is empty!')
    elif '' in L:
        L.remove('')


    if len(L) == 1:
        p = p + L[0]
    elif len(L) == 2:
        p = L[0] + ' and ' + L[1]
    elif len(L) == 3:
        p = L[0] + ', ' + L[-2] + ' and ' + L[-1]
    else:
        for i in L:
            if L.index(i) == L.index(L[-1]):
                p = p + ' and ' + str(i)
            else:
                if L.index(i) == L.index(L[-2]):
                    p = p + str(i)
                else:
                    p = p + str(i) + ', '

    print('Your finished list is:')
    print(p)
    return(p)


LIST = []

o = 0
inpt = ''

print('Provide a list for me, enter 1 by 1')

while True:
    print('Input number ' + str(o))
    o = o +1
    inpt = input()
    LIST.append(inpt)
    if inpt == '':
        break

print('Your list is:')
print(list(LIST))

lister(LIST)


