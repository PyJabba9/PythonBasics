#Create a program that:

#Starts with an empty list for student names
#Asks for 5 student names (use a for loop)
#Adds each name to the list (use concatenation +, not methods)
#Displays the list with index numbers
#Let user pick a student by index and show that student's name
#Create a new list with only students whose names start with a specific letter


students = []
students2 = []
for i in range(0,5):
    print('Enter students name')
    name = input()
    students = students + [name]

for name in range(len(students)):
    print(str(name) + ' - '+ students[name])


print('pick a student by number')
n = input()
print(students[int(n)])

answer = ''
letter = ''
x = 0
print('do you want to make a list of people out of those in previous list whose names start with selected letter? y/n?')
answer = input()
if answer == 'y':

    print('what letter do you pick?')
    letter = input()

    for name in students:
        x = x + 1
        if name[0] == letter:
            students2 = students2 + [name]
        else:
            print('not applicable name ' + name)
    print('the final new list is:')
    print(students2)

else:
    print('Bye!')



