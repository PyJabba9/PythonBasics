'''
For this task I will have 3 excel files with 2 sheets for each with data in an unstructured format - different date formats, different formatting and data types.
I will need to structure the data in every sheet in those 3 workbooks, merge them into one workbook and check for duplicated data (and remove it)

steps I plan:

1. Investigate ways to load data from the set folder -will take logic from previous practice on ch11 - taking folder form clipboard.
2. Create a loop that will:
    - open the 1st excel file
    - iterate through column 1 - fixing date (datetime) - probably I will have to go to ch19 check how can I easily change it as there are all sorts of different date formats present.
    - iterate through column 2 - fixing product (string)
    - iterate through column 3 - fixing country (string)
    - iterate through column 4 - fixing amoun (integer)
    example of the table below:
Transaction Date	product 	 Country	AmountUSD
2025/03/29	        Phone	    Germany	       1823
2025/02/14	        Tablet 	    Germany	        742


date uniforming task seems to be the hardest one - SO I USE DATEUTIL :D, date format DD-MM-YYYY


next - add all data into 1 folder
next - remove duplicates (at the end as we need all data together)


'''


import os, datetime, time, pyperclip, openpyxl

from dateutil.parser import *
from pathlib import Path

folder = Path('C:/Users/junke/mu_code/pythonScripts/unstructuredExcels_ch14')



Path('C:/Users/junke/mu_code/pythonScripts/unstructuredExcels_ch14/Processed').mkdir(parents=True, exist_ok=True)
folderv = Path('C:/Users/junke/mu_code/pythonScripts/unstructuredExcels_ch14/Processed')
Path('C:/Users/junke/mu_code/pythonScripts/unstructuredExcels_ch14/Temp').mkdir(parents=True, exist_ok=True)
tempfile = Path('C:/Users/junke/mu_code/pythonScripts/unstructuredExcels_ch14/Temp')


co = 0
m = 0
DL = []
PL = []
CL = []
AL = []
AF = []
FL = []
AFF = []

for files in list(folder.glob('*.xlsx')): # go through files iterator - for now I will set this aside as I will do all the steps separately to test

    wb = openpyxl.load_workbook(files)
    wbf = openpyxl.Workbook()
    sheet = wb.active


    for s,n in enumerate(wb.worksheets):
        wbf.create_sheet(index = s, title = n.title) # add iteration name through the worksheets instead of number



    for S in wb.worksheets:

        for i in range(2,int(S.max_row)+1): # this approach gives correct column contents without name of the column
            try:
                d = parse(S.cell(row=i,column=1).value,dayfirst=True)
                D = d.strftime('%d/%m/%Y')# good date format
                DL.append(D)

            except:
                print(f'Error - very weird date - {S.cell(row=i,column=1)}')

        PD = (((S.cell(row=1,column=1).value).strip()).capitalize())
        #DL.insert(0,PD) # adding column name back

        wbf.active = wbf[S.title]

        for pos,val in enumerate(DL):
            wbf.active.cell(row=pos+1, column = 1).value = val
            DL = []

        for i in range(2,int(S.max_row)+1):
            p = (S.cell(row=i,column=2).value).lower()
            P = (p.strip()).capitalize()
            PL.append(P)

        PH = (((S.cell(row=1,column=2).value).strip()).capitalize())
        #PL.insert(0,PH)
        for pos,val in enumerate(PL):
            wbf.active.cell(row=pos+1, column = 2).value = val
            PL = []


        for i in range(2,int(S.max_row)+1):
            c = (S.cell(row=i,column=3).value).lower()
            C = (c.strip()).capitalize()
            CL.append(C)

        CH = (((S.cell(row=1,column=3).value).strip()).capitalize())
        #CL.insert(0,CH)
        for pos,val in enumerate(CL):
            wbf.active.cell(row=pos+1, column = 3).value = val
            CL = []



        for i in range(2,int(S.max_row)+1): # this approach gives correct column contents without name of the column
            try:
                a = S.cell(row=i,column=4).value
                A = float(a)
                AL.append(A)
            except:
                print(f'wrong numerical format for {a}')

        AH = ((S.cell(row=1,column=4).value).strip())
        #AL.insert(0,AH)
        for pos,val in enumerate(AL):
            wbf.active.cell(row=pos+1, column = 4).value = val
            AL = []

        for i in range(2,int(S.max_row)+1):
            AF.append(wbf.active.cell(row=i-1, column = 1).value + wbf.active.cell(row=i-1, column = 2).value + wbf.active.cell(row=i-1, column = 3).value + str(wbf.active.cell(row=i-1, column = 4).value))
            AFF.append(wbf.active.cell(row=i-1, column = 1).value + wbf.active.cell(row=i-1, column = 2).value + wbf.active.cell(row=i-1, column = 3).value + str(wbf.active.cell(row=i-1, column = 4).value))
        for pos,val in enumerate(AF):
            wbf.active.cell(row=pos+1, column = 5).value = val

            AF = []

    m +=1
    savefile_temp = (f'{tempfile}\\{m}.xlsx')
    del wbf['Sheet']
    wbf.save(savefile_temp)

#---------------------------------------------------------------------------- start of phase 2 - combining finalized file
wbff = openpyxl.Workbook()
sheet = wbff.active

for s,n in enumerate(wbf.worksheets):

    wbff.create_sheet(index = s, title = n.title) # add iteration name through the worksheets instead of number


for files in list(tempfile.glob('*.xlsx')): # iterating temp files (with E column for checking duplicates)

    wbf = openpyxl.load_workbook(files)
    for S in wbf.worksheets:

        if S.title == 'Sales':
            wbff.active = wbff[S.title]
            for i in range(1,int(S.max_row)+1): # problem in s.max_row - it does not add up !!!!

                wbff.active.append([S.cell(row=i,column=1).value,S.cell(row=i,column=2).value,S.cell(row=i,column=3).value,S.cell(row=i,column=4).value,S.cell(row=i,column=5).value])
                FL.append(S.cell(row=i,column=5).value)
        elif S.title == 'Returns':
            wbff.active = wbff[S.title]
            for i in range(1,int(S.max_row)+1):

                wbff.active.append([S.cell(row=i,column=1).value,S.cell(row=i,column=2).value,S.cell(row=i,column=3).value,S.cell(row=i,column=4).value,S.cell(row=i,column=5).value])
                FL.append(S.cell(row=i,column=5).value)

#---------------------------------------------------------------fix duplicates - got it from nice guy here https://www.youtube.com/watch?v=iY0L04QwzEY
        unique_rows = set()
        for row in wbff.active.iter_rows(1,values_only = True):
            unique_rows.add(tuple(row))
        wbff.active.delete_rows(1,wbff.active.max_row)
        for unique_row in unique_rows:
            wbff.active.append(unique_row)

#------------------------------------------------------------- adding headers back and removing tech column
for S in wbff.worksheets:
    S.insert_rows(idx=1,amount=1)
    S.cell(row = 1, column = 1).value = PD
    S.cell(row = 1, column = 2).value = PH
    S.cell(row = 1, column = 3).value = CH
    S.cell(row = 1, column = 4).value = AH
    S.delete_cols(idx=5,amount=1)
del wbff['Sheet']
wbff.save(folderv/'Sales_Processed.xlsx')




