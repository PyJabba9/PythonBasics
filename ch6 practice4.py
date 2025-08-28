#Write a program to find out how often a streak of six heads or a streak of six tails comes up
#in a randomly generated list of 100 heads and tails. Your program should break
#up the experiment into two parts: the first part generates a list of 100 randomly
#selected 'H' and 'T' values, and the second part checks if there is a streak in it.
#Put all of this code in a loop that repeats the experiment 10,000 times so that you
#can find out what percentage of the coin flips contains a streak of six heads or six
#tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value
#50 percent of the time and a 1 value the other 50 percent of the time.


import random
nos = 0
for experiment_number in range(10000):  # Run 10,000 experiments total.

    FLIPS = []
    r = ''
    i = ''
    c = 0
    x = ''
    for i in range(1,101):
        r = random.randint(0,1)
        if r == 1:
                r = 'H'
        else:
                r = 'T'
        FLIPS.append(r)
    #print(FLIPS)



    for n in range(len(FLIPS) -1):
        if FLIPS[n] == FLIPS[n + 1]:
            c = c + 1
            if c == 5:
                #print('we have a streak!')
                nos = nos + 1
                break
            else:

                continue
        else:
            c = 0



print('Chance of streak: %s%%' % (nos * 100/ 10000))
