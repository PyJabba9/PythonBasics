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

def totalsum(employeeDB):
    print('Total sales are:')
    print(sum(employeeDB.values()))

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
def showmeMAX(employeeDB):
    print('Biggest amount of sales is:')
    print(max(employeeDB.values()))
    keys = [key for key, val in employeeDB.items() if val == max(employeeDB.values())]
    print('The top performer is:')
    print(keys)
employeeDB = {'Anna':30,'Govno':10,'Zaloopa':15}
while True:
    print('Please enter Employee Name(empty input = exit):')
    n = input()
    if n == '':
        break
    print('Please enter sales amount(empty input = exit):')
    s = input()
    s = int(s)
    if s == '':
        break
    if n in employeeDB:
        employeeDB[n] += s
    employeeDB.setdefault(n,s)
print(employeeDB)

totalsum(employeeDB)
avgperEMP(employeeDB)
showmeMAX(employeeDB)


