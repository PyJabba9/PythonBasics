"""
For practice, write a function named printTable() that takes a
list of lists of strings and displays it in a well-organized table with each column right- justified.
Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

""" has to print following output:
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""

#print(tableData[0][0] + tableData[1][0] + tableData[2][0]) # accessing specific item inside list of lists - trying to understand how to do this iteration
#print(tableData[0][1] + tableData[1][1] + tableData[2][1])
# and so on
# we need to variables 1st one will jump from n to max(len(tableData)) and second one m will go from m to max(len(tableoftableData))
#print(''.join(str(tableData)))
def TransposeT(tableData):

    inner = len(tableData[0])

    outer = len(tableData)

    lst = ''

    for m in range(0,inner):
        for n in range(0,outer):
            lst += ' ' + tableData[n][m]

        lst = (lst + '\n')
    print(lst.rjust(25))


TransposeT(tableData)
