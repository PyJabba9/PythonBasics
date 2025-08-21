import random, sys

print('Lets play the game')
print('Continue? y/n')
A = input('>')
Q = 0
while A == 'y':
    numba = random.randint(1, 10)
    I = 10
    C = 0

    print('Im thinking of a number between 1 and 10, guess it ' + str(numba))
    for I in range (11,1,-1):
        C = C+1
        N = int(input('>'))
        if numba > N:
            print('too low')
            print('You have ' + str(I-2)  + ' tries left')
        elif numba < N:
            print('too high')
            print('You have ' + str(I-2)  + ' tries left')
        else:
            print('You won!')
            print('You have used ' + str(C)  + ' tries')
            if I == 11:
                Q = Q + 2
                print('You earned ' + str(Q) + ' points, because you guessed correct number from the 1st try!')
            else:
                Q = Q + 1
                print('You earned ' + str(Q) + ' points, good Job!')
            break
    else:
        A = 'n'
    print('Do you want to play again? y/n?')
    A = input('>')
    print('You earned '+ str(Q) + ' points total, good Job!')

