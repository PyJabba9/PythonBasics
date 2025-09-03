# TASK 1: Data Collection
# Create a program that:
# - Asks for employee name  - DONE
# - Asks for sales amount - DONE
# - If employee already exists - adds amount to previous total - DONE
# - If new employee - creates new record - DONE
# - Stops when empty input is entered - DONE

# TASK 2: Analytics
# Add functionality to:
# - Show TOP salesperson (highest total amount)
# - Show AVERAGE amount per employee
# - Show TOTAL sum of all sales

# TASK 3: Search
# Allow user to:
# - Enter employee name
# - Display their results
# - If not found - show "Employee not found"

def employeeFinder(employeeDB):
    print('In order to find specific employee, please type his name:')
    nn = input()
    if nn in employeeDB:
        print('Employee ' + str(nn) + ' made:')
        print(employeeDB[nn])
        return(employeeDB[nn])
    else:
        print(str(employeeDB.get(nn,'There is no people named ' + str(nn) + ' in the database')))
        print('Would you like to add new employee? y/n')
        a = input()
        if a == 'y':
            addingusers(employeeDB)
        else:
            print('OK,bye')

def totalsum(employeeDB):
    print('Total sales are:')
    print(sum(employeeDB.values()))
    return(sum(employeeDB.values()))

def avgperEMP(employeeDB):
    counter = 0
    summa = 0
    for n in employeeDB:
        counter = counter + 1
    for s in employeeDB:
        summa = sum(employeeDB.values())
    res = summa / counter
    print('Average number of sales per employee is:')
    print(res)
    return(res)

def showmeMAX(employeeDB):
    print('Biggest amount of sales is:')
    print(max(employeeDB.values()))
    keys = [key for key, val in employeeDB.items() if val == max(employeeDB.values())]
    print('The top performer is:')
    print(keys)
    return(keys)

def addingusers(employeeDB):
    while True:
        print('Please enter Employee Name(empty input = exit):')
        n = input()
        if n == '':
            break
        if n[0] not in ABC:
            print('Is it even a name?...')
            print('Enter a PROPER name, with letters:')
            n = input()
        if n[-1:] == str(' '):
            n = n[:-1]

        print('Please enter sales amount(empty input = exit):')
        s = input()
        try:
            s = int(s)
        except:
            print('Only numbers supported')
            print('Please enter sales amount(empty input = exit):')
            s = input()

        if s == '':
            break
        if n in employeeDB:
            employeeDB[n] += s
        employeeDB.setdefault(n,s)
    print('Your sales database has this values:')
    print(employeeDB)
    return(employeeDB)

import string
ABC = []
ABC += list('abcdefghijklmnopqrstuvwxyz')

employeeDB = {'Anna':30,'Susan':10,'George':15}
while True:
    print('Welcome to my small database of sales reps and sales, here you can store sales data for specific salespeople')
    print('In order to start, please select what would you like to do:\n 1. In order to add new users, please type "add"\n 2. In order to show total sum of all sales made by salespeople, please type "total".\n 3. To get average number of sales, type "avg". \n 4. To get top salesperson, type "top".\n 5. In order to find specific employee, type "find". \n For Exit - type exit')
    aa = input()
    if aa == 'add':
        addingusers(employeeDB)
    elif aa == 'total':
        totalsum(employeeDB)
    elif aa == 'avg':
        avgperEMP(employeeDB)
    elif aa == 'top':
        showmeMAX(employeeDB)
    elif aa == 'find':
        employeeFinder(employeeDB)
    elif aa == 'exit':
        print('Bye')
        break

#addingusers(employeeDB)
#totalsum(employeeDB)
#avgperEMP(employeeDB)
#showmeMAX(employeeDB)
#employeeFinder(employeeDB)
