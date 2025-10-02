

import sqlite3, csv, os, shutil, datetime, sys
from pathlib import Path

#-----------------------------------------------------------
current_dateTime = datetime.datetime.today().strftime('%Y-%m-%d') # actual datetime_ to be added into filename for archiving
#-----------------------------------------------------------
folder = Path('C:/Users/junke/mu_code/pythonScripts/Project_1_ETL_Tool/')

Path(f'{folder}/Archive').mkdir(parents=True, exist_ok=True)
folder_arch = Path('C:/Users/junke/mu_code/pythonScripts/Project_1_ETL_Tool/Archive/')
#-----------------------------------------------------------
conn = sqlite3.connect(f'{folder}/SQLite_ETL.db', isolation_level = None)
cur = conn.cursor()
conn_0 = sqlite3.connect(f'{folder}/SQLite_dummy_reference.db', isolation_level = None)
cur_0 = conn_0.cursor()
#-----------------------------------------------------------
CSV_file = list(folder.glob('*.csv')) # very important thing - if .glob used without list - it will contain a path value untill first use, after that it is erased - this caused my archiving to break
folder_arch_A = folder_arch.glob('*.csv')
#-----------------------------------------------------------


def DQ_check(conn, cur): # DQ query - have to adjust for every concrete csv ingested

    sqlQuery = "select dt, SUM(vol), COUNT(dt) from temp_temp GROUP BY dt"
    sqlQuery_0 = "select SUM(vol)/COUNT(DISTINCT(dt)), COUNT(dt)/COUNT(DISTINCT(dt)) from master_temp"
    cur_0.execute(sqlQuery_0)
    K = cur_0.fetchall()
    for x,v in K: # Getting average meanings for num of rows and gross vol from benchmark DB
        #print(f'Average Gross Volume: {x} Number of rows: {v}')
        None
    cur.execute(sqlQuery)
    L = cur.fetchall()
    for i,k,c in L:

        if ((k/x)-1)*100 >= 25:
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

        elif ((c/v)-1)*100 >= 25:
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

        elif ((k/x)-1)*100 <= -25:
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

        elif ((c/v)-1)*100 <= -25:
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

    cur.close() #- to be closed after all operations done
    conn.close() #- to be closed after all operations done

# loading data into temp_temp table by default - to have something for DQ_check to work with
DT = []



for file in list(CSV_file):


    with open(file,'r') as fin:

        dr = csv.DictReader(fin, delimiter='\t')
        to_db = [(i['Category'] ,i['level'] ,i['distribution_channel'] ,i['period'] ,i['dt'] ,i['manufacturer'] ,i['brand'] ,i['BBSKU'] ,i['NAMESKU'] ,i['ean'] ,i['segment'] ,i['format'] ,i['tar_rmce'] ,i['vol'] ,i['val'] ,i['rcnt'] ,i['qty'] ,i['shvol'] ,i['shval'] ,i['shrcnt'] ,i['shqty'] ,i['dntot'] ,i['dn'] ,i['dnvol'] ,i['dnval'] ,i['dwqty'] ,i['dwvaltot'] ,i['shsvol'] ,i['shsval'] ,i['avp'] ,i['avpjm'] ,i['avtvol'] ,i['avtval'] ,i['avtqty'] ,i['avsvol'] ,i['avsval'] ,i['avsrcnt'] ,i['avsqty'] ,i['avgsku']) for i in dr]

cur.executemany('INSERT INTO temp_temp (Category ,level ,distribution_channel ,period ,dt ,manufacturer ,brand ,BBSKU ,NAMESKU ,ean ,segment ,format ,tar_rmce ,vol ,val ,rcnt ,qty ,shvol ,shval ,shrcnt ,shqty ,dntot ,dn ,dnvol ,dnval ,dwqty ,dwvaltot ,shsvol ,shsval ,avp ,avpjm ,avtvol ,avtval ,avtqty ,avsvol ,avsval ,avsrcnt ,avsqty ,avgsku) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', to_db)
conn.commit()


repl = DQ_check(conn, cur)

if repl == 'n':
    #print('this is my temp file that will go further into temp table of SSMS and will be processed further, it has to contain only dates to be loaded - 14-18')
    #print(conn.execute('select dt, SUM(vol), COUNT(dt) from master_temp_destination GROUP BY dt').fetchall()) #- checking result of loading
    #conn.execute('DELETE from master_temp')
    #print(conn.execute("select dt, SUM(vol), COUNT(dt) from master_temp GROUP BY dt").fetchall())
    #conn.execute('DELETE from temp_temp')
    try:
        sys.exit()
    except:
        print('Exiting')
    cur.close()
    conn.close()
elif repl == 'y':
    print('Loading started')

    conn.execute("INSERT INTO master_temp SELECT * FROM temp_temp")
    conn.execute('DELETE from temp_temp')
    conn.commit()
    cur.close()
    conn.close()
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




