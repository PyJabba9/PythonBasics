#Practice Challenge 2: Number List Processor
#Build a program that:

#Creates a list of 10 random numbers (1-100) done
#Prints the original list -done
#Shows specific slices: first 3, last 3, middle elements -done
#Finds and prints all numbers greater than 50 (using for loop + if) - done
#Replaces any number at index 5 with 999 - updated a little to make it nicer and DONE
#Creates a new list by concatenating the original with [0, 0, 0]

import random

randomlist = []
randomlist1 = []
for i in range(10):
    R = random.randint(1,100)
    randomlist = randomlist + [R]

print(randomlist)

print('1st 3 elements are:')
print(randomlist[0:3])
print('last 3 elements are:')
print(randomlist[-3:])
print('middle 4 elements are:')
print(randomlist[3:-3])
x = 0
for i in randomlist:
    if int(i) >=50:
        print(i)
    else:
        x = x + 1

if x == 10:
    print('There were no numbers over 50 in the list')


print('Do you wish to update the list? y/n?')
yn = 0
yn = input()
if yn == str('y'):
    print('Please enter the number and the position in the list, where you want to paste it')
    n = input('Number:')
    pos = input('Position:')
    randomlist[int(pos)] = int(n)
    print('Updated list looks like that:')
    print(randomlist)
else:
    print('Bye!')

print('Your newest updated list is concatenated and now looks like that:')
randomlist1 = randomlist + [0,0,0]
print(randomlist1)
