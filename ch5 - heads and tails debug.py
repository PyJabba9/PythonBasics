#The following program is meant to be a simple coin toss guessing game. The player gets two guesses. (It’s an easy game.) However, the program has multiple bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.
# I would also move comparison in a separate function, which I did in this script
import random
guess = ''

def headsTails(guess):

    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    if toss == 1:  #the game didnt have a translation from 0 and 1 to heads and tails, so I had to add this, before the actual comparison is started
        toss = 'heads'
    else:
        toss = 'tails'
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')



while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    headsTails(guess)



