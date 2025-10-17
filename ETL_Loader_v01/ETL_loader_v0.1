import sqlite3, csv, os, shutil, datetime, sys, pyodbc, decimal, subprocess, re
from pathlib import Path
current_dateTime = datetime.datetime.today().strftime('%Y-%m-%d') # actual datetime_ to be added into filename for archiving
folder = Path('C:/Users/***/LOAD_PY/') # set to variable later
Path(f'{folder}/Archive').mkdir(parents=True, exist_ok=True)
folder_arch = Path('C:/Users/***/LOAD_PY/Archive/') #set to variable later
folder_SQL_Scripts = Path('C:/Users/***/LOAD_PY/SQL_Scripts/') #set to variable later
sql_file = list(folder_SQL_Scripts.glob('*TEST.sql'))

# data reference connection as well as final destination for data load (final_table_temp)
conn_0 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=***;"
                      "Database=M_E;"
                      "Trusted_Connection=yes;")
cur_0 = conn_0.cursor()
CSV_file = list(folder.glob('*.csv')) # very important thing - if .glob used without list - it will contain a path value untill first use, after that it is erased - this caused my archiving to break
folder_arch_A = folder_arch.glob('*.csv')
print(CSV_file)
for f in CSV_file:
    CSV_file_name = os.path.basename(f)
    print(CSV_file_name)

#in case of bulk load, could stay for later to iterate through files - filename to be filtered as 2 files are being loaded per iteration
for f in sql_file:
    sql_path = f
    sql_f = os.path.basename(f)
    print(sql_f)
# executing powershell loader with subprocess library
ps_script = r"C:\Users\***\LOAD_PY\CL.ps1" # change to relative path later
function = "W" # change to variable for scaling later, W-weekly, M- monthly
# params add here
cmd = [
    "powershell.exe",
    "-ExecutionPolicy", "Bypass",
    "-Command",
    f'. "{ps_script}"; {function}'

]

# run
result = subprocess.run(cmd, capture_output=True, text=True)

# read shell reply
print("=== STDOUT ===")
print(result.stdout)
print("=== STDERR ===")
print(result.stderr)
print("Exit code:", result.returncode)

def DQ_check(conn, cur): # DQ query - have to adjust for every concrete csv ingested

    sqlQuery = "SELECT SUM(cast(vol AS NUMERIC))/COUNT(DISTINCT(dt)),COUNT(dt)/COUNT(DISTINCT(dt)), dt FROM [Database_name].[dbo].[temp_temp] WHERE period = 'week' AND dt <(SELECT MAX(dt) FROM [Database_name].[dbo].[temp_temp])  group by dt"
    sqlQuery_0 = "SELECT SUM(cast(vol AS NUMERIC))/COUNT(DISTINCT(dt)),COUNT(dt)/COUNT(DISTINCT(dt)) FROM [Database_name].[dbo].[0master] WHERE period = 'week' and dt <(select max(dt) from [Database_name].[dbo].[0master]) and dt>= DATEADD(DAY, -90, GETDATE())"
    cur_0.execute(sqlQuery_0)
    K = cur_0.fetchall()

    for x,v in K: # Getting average meanings for num of rows and gross vol from benchmark DB
        #print(f'Average Gross Volume: {x} Number of rows: {v}')
        print(x,v) # delete after debug
        #None - remove hash after debug
    cur_0.execute(sqlQuery)
    L = cur_0.fetchall()
    for k,c,i in L:


        if ((decimal.Decimal(k)/x)-1)*100 >= 25:
            print(f'Gross Volume ({k}) is higher than average meaning ({x}) for more than 25%, please review date from {i}')
            print('Do you want to continue loading? y/n')
            while True:
                answer = input()
                if answer == 'y':
                    return(answer)
                    break
                if answer == 'n':
                    return(answer)
                    break
                else:
                    print('Please provide correct answer, y/n')

        elif ((float(c)/v)-1)*100 >= 25:
            print(f'Number of rows ({k}) is higher than average meaning ({v}) for more than 25%, please review date from {i}')
            print('Do you want to continue loading? y/n')
            while True:
                answer = input()
                if answer == 'y':
                    return(answer)
                    break
                if answer == 'n':
                    return(answer)
                    break
                else:
                    print('Please provide correct answer, y/n')

        elif ((decimal.Decimal(k)/x)-1)*100 <= -25:
            print(f'Gross Volume ({k}) is lower than average meaning ({x}) for more than 25%, please review date from {i}')
            print('Do you want to continue loading? y/n')
            while True:
                answer = input()
                if answer == 'y':
                    return(answer)
                    break
                if answer == 'n':
                    return(answer)
                    break
                else:
                    print('Please provide correct answer, y/n')

        elif ((float(c)/v)-1)*100 <= -25:
            print(f'Number of rows ({k}) is lower than average meaning ({v}) for more than 25%, please review date from {i}')
            print('Do you want to continue loading? y/n')
            while True:
                answer = input()
                if answer == 'y':
                    return(answer)
                    break
                if answer == 'n':
                    return(answer)
                    break
                else:
                    print('Please provide correct answer, y/n')

        else:
            print(f'Date: {i} Gross Volume: {k} Number of rows: {c}')
    print('Do you want to continue loading? y/n')
    while True:
        answer = input()
        if answer == 'y':
            return(answer)
            break
        if answer == 'n':
            return(answer)
            break
        else:
            print('Please provide correct answer, y/n')

    cur_0.close() #- to be closed after all operations done
    conn_0.close() #- to be closed after all operations done



repl = DQ_check(conn_0, cur_0)

if repl == 'n':
    #hashed prints and conn.execute below are debug checks I used to confirm that data was loaded into temp_temp table
    #print('this is my temp file that will go further into temp table of SSMS and will be processed further, it has to contain only dates to be loaded - 14-18')
    #print(conn.execute('select dt, SUM(vol), COUNT(dt) from master_temp_destination GROUP BY dt').fetchall()) #- checking result of loading
    #conn.execute('DELETE from master_temp')
    #print(conn.execute("select dt, SUM(vol), COUNT(dt) from master_temp GROUP BY dt").fetchall())
    #conn.execute('DELETE from temp_temp')
    try:
        sys.exit()
    except:
        print('Exiting')
    cur_0.close()
    conn_0.close()
elif repl == 'y':
    print('Loading started')

    cur_0.execute("INSERT INTO [Database_name].[dbo].[final_table] SELECT * FROM [Database_name].[dbo].[temp_temp]")
    cur_0.execute('DELETE from [Database_name].[dbo].[temp_temp]')
    cur_0.commit()
    cur_0.close()
    conn_0.close()
    print('Data loaded, archiving files')
    for f in list(CSV_file): # moving file into archive folder
        CSV_file_name = os.path.basename(f)
        print(CSV_file_name)
        shutil.move(folder/CSV_file_name,folder_arch/CSV_file_name)


    for F in list(folder_arch_A): #renaming in the archived folder
        CSV_file_name = os.path.basename(F)
        CSV_file_name_F = str(CSV_file_name[:-4])
        archiveName = str(CSV_file_name_F)+'_'+ str(current_dateTime+'.csv')
        shutil.move(folder_arch/F,folder_arch/archiveName)
    print('Archivisation complete')




def exec_sql_file(cur_0, sql_file):
    print ("\n[INFO] Executing SQL script file: '%s'" % (sql_file))
    statement = ""



    for line in open(sql_file,'r',encoding='utf-8'):

        print(line)

        if re.match(r'--', line):  # ignore sql comment lines
            continue
        if not re.search(r';$', line):  # keep appending lines that don't end in ';'
            statement = statement + line

        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line

            print ("\n\n[DEBUG] Executing SQL statement:\n%s" % (statement))
            try:

                cur_0.execute(statement)
                conn_0.commit()
            except (OperationalError, ProgrammingError) as e:
                print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))

            statement = ""

exec_sql_file(cur_0,sql_path)

cur_0.close()
conn_0.close()
