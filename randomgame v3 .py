import random, sys
print('Lets play the game')
print('Continue? y/n')
A = input('>')
Q = 0
def comparator(numba,N): #function logic with simple comparing of random number versus user input

    if numba > N:
        return 'Too low'


    elif numba < N:
        return 'Too high'


    else:
        return 'You Won!'





while A == 'y':
    numba = random.randint(1, 10)
    I = 10
    C = 0

    print('Im thinking of a number between 1 and 10, guess it ' + str(numba))
    for I in range (11,1,-1):
        C = C+1
        try: #added my first error handling here
            N = int(input('>'))
        except: # If someone tries to enter not a number, it will ask you provide a number and program will start again
            print('Please provide a number!')
            break

        result = comparator(numba,N) #my first function working over here!!!!
        if result == 'You Won!':
            Q = Q+1
            print(result)
            print('You earned ' + str(Q) + ' points, good Job!')
            break
        else:
            print(result)
            print('You have ' + str(I-2) + ' tries left')
    else:
        A = 'n'
    print('Do you want to play again? y/n?')
    A = input('>')
    #print('You earned '+ str(Q) + ' points total, good Job!')

