#program tasks to 4th chapter
#task 1 -Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
#Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer; sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)

def collatz(number):

    if number % 2 == 0:
        number = number // 2
        return number
    elif number % 2 == 1:
        number = (number * 3) + 1
        return number


while True:
    print('enter your number into collatz!')
    try:
        number = int(input('>')) # I did it! this part is calling the function on itself updating number as it goes another iteration. At the end it shows 2, and runs another run that turns 2 into 1 and function breaks!!!
        while number != 1:
            number = collatz(number)
            print(number)
        print('End')
        break # added outer while loop to make the program loop if case if user enters letters instead of numbers. If number entered - all OK, program executes and exits, if letter - it loops with error message until number is entered
    except:
        print('Please enter a number, not some BS')


