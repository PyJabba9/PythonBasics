'''
I will recreate part of my routine at work, loading csv into SSMS, but as I dont have work SSMS available, I will load data into SQLite and later on I will modify the script with pyodbc as syntax stays the same.
Task:
Extract data from .csv file in the folder into SQLite (and after that to SSMS - as I have it at work :) )

- check folder for .csv file. +
- ask user if this is the file to be loaded, provide min(DT)/max(DT) from file contents
- if no - exit
- if yes - read the file, load into SQLite table (create one if doesnt exist)
- save SQLite+
- move file into /Archive folder+

DQ check before loading:
1. Takes sqlite table
2. Outputs number of rows per date AND sum of volume per date
3. Compares it to average number and sum of volume
4. If difference is > 25% - inform user
5. If all OK - copy data from master_temp into master table and delete master_temp contents
---------------------------------------------------------------------------------------
 hashed out data loading procedure - last time used to ingest DUMMY REFERENCE FILE
conn_0.execute('CREATE TABLE IF NOT EXISTS master_temp (category TEXT NULL,level TEXT NULL, distribution_channel TEXT NULL, period TEXT NULL, dt TEXT NULL, manufacturer TEXT NULL, brand TEXT NULL, BBSKU TEXT NULL, NAMESKU TEXT NULL, ean TEXT NULL, segment TEXT NULL, format TEXT NULL, tar_rmce TEXT NULL, vol NUMERIC NULL, val NUMERIC NULL, rcnt NUMERIC NULL, qty NUMERIC NULL, shvol NUMERIC NULL, shval NUMERIC NULL, shrcnt NUMERIC NULL, shqty NUMERIC NULL, dntot NUMERIC NULL, dn NUMERIC NULL, dnvol NUMERIC NULL, dnval NUMERIC NULL, dwqty NUMERIC NULL, dwvaltot NUMERIC NULL, shsvol NUMERIC NULL, shsval NUMERIC NULL, avp NUMERIC NULL, avpjm NUMERIC NULL, avtvol NUMERIC NULL, avtval NUMERIC NULL, avtqty NUMERIC NULL, avsvol NUMERIC NULL, avsval NUMERIC NULL, avsrcnt NUMERIC NULL, avsqty NUMERIC NULL, avgsku NUMERIC NULL )')

for file in list(CSV_file):
    CSV = open(file)
    CSV_dict_reader = csv.DictReader(CSV,delimiter = '\t')
    dict_data = list(CSV_dict_reader)

with open(file,'r') as fin:
    dr = csv.DictReader(fin, delimiter='\t')
    to_db = [(i['Category'] ,i['level'] ,i['distribution_channel'] ,i['period'] ,i['dt'] ,i['manufacturer'] ,i['brand'] ,i['BBSKU'] ,i['NAMESKU'] ,i['ean'] ,i['segment'] ,i['format'] ,i['tar_rmce'] ,i['vol'] ,i['val'] ,i['rcnt'] ,i['qty'] ,i['shvol'] ,i['shval'] ,i['shrcnt'] ,i['shqty'] ,i['dntot'] ,i['dn'] ,i['dnvol'] ,i['dnval'] ,i['dwqty'] ,i['dwvaltot'] ,i['shsvol'] ,i['shsval'] ,i['avp'] ,i['avpjm'] ,i['avtvol'] ,i['avtval'] ,i['avtqty'] ,i['avsvol'] ,i['avsval'] ,i['avsrcnt'] ,i['avsqty'] ,i['avgsku']) for i in dr]

    cur_0.executemany('INSERT INTO master_temp (Category ,level ,distribution_channel ,period ,dt ,manufacturer ,brand ,BBSKU ,NAMESKU ,ean ,segment ,format ,tar_rmce ,vol ,val ,rcnt ,qty ,shvol ,shval ,shrcnt ,shqty ,dntot ,dn ,dnvol ,dnval ,dwqty ,dwvaltot ,shsvol ,shsval ,avp ,avpjm ,avtvol ,avtval ,avtqty ,avsvol ,avsval ,avsrcnt ,avsqty ,avgsku) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', to_db)
    conn_0.commit()



------------------------------------------------------------------------------------------
'''

import sqlite3, csv, os, shutil, datetime
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
CSV_file = folder.glob('*.csv')
folder_arch_A = folder_arch.glob('*.csv')
#-----------------------------------------------------------


def DQ_check(conn, cur): # DQ query - have to adjust for every concrete csv ingested

    sqlQuery = "select dt, SUM(vol), COUNT(dt) from master_temp GROUP BY dt"
    sqlQuery_0 = "select SUM(vol)/COUNT(DISTINCT(dt)), COUNT(dt)/COUNT(DISTINCT(dt)) from master_temp"
    cur_0.execute(sqlQuery_0)
    K = cur_0.fetchall()
    for x,v in K:
        print(f'Average Gross Volume: {x} Number of rows: {v}')

    cur.execute(sqlQuery)
    L = cur.fetchall()
    for i,k,c in L:
        print(f'Date: {i} Gross Volume: {k} Number of rows: {c}')

    cur.close() #- to be closed after all operations done
    conn.close() #- to be closed after all operations done

DQ_check(conn, cur)

# TODO NEXT - I HAVE CLEAN REFERENCE TABLE - LOAD IT AS SEPARATE *FINAL* TABLE TO DIFFERENT SQLite DB to simulate different connection and working with 2 opened connections to compare SUM and COUNT rows for loading new data - ok
# 1.create new DB and load there new csv - ok
# 2.load separately to DQ_check and compare SUM(vol) and COUNT(dt) for other dates, alert if something is exceeding 25% threshold in both directions



'''
conn.execute('CREATE TABLE IF NOT EXISTS master_temp (category TEXT NULL,level TEXT NULL, distribution_channel TEXT NULL, period TEXT NULL, dt TEXT NULL, manufacturer TEXT NULL, brand TEXT NULL, BBSKU TEXT NULL, NAMESKU TEXT NULL, ean TEXT NULL, segment TEXT NULL, format TEXT NULL, tar_rmce TEXT NULL, vol NUMERIC NULL, val NUMERIC NULL, rcnt NUMERIC NULL, qty NUMERIC NULL, shvol NUMERIC NULL, shval NUMERIC NULL, shrcnt NUMERIC NULL, shqty NUMERIC NULL, dntot NUMERIC NULL, dn NUMERIC NULL, dnvol NUMERIC NULL, dnval NUMERIC NULL, dwqty NUMERIC NULL, dwvaltot NUMERIC NULL, shsvol NUMERIC NULL, shsval NUMERIC NULL, avp NUMERIC NULL, avpjm NUMERIC NULL, avtvol NUMERIC NULL, avtval NUMERIC NULL, avtqty NUMERIC NULL, avsvol NUMERIC NULL, avsval NUMERIC NULL, avsrcnt NUMERIC NULL, avsqty NUMERIC NULL, avgsku NUMERIC NULL )')

#conn.execute('DROP TABLE master_temp')

#loading CSV in DT list for further load into SQLite
DT = []
for file in list(CSV_file):
    CSV = open(file)
    CSV_dict_reader = csv.DictReader(CSV,delimiter = '\t')
    dict_data = list(CSV_dict_reader)

#little date check - not needed as doesnt show actual DQ situation
    for row in dict_data:
        DT.append(row['dt'])
        #DT.append(datetime.datetime.strptime(row['dt'],"%m/%d/%Y"))

#print(f'Loaded data has dates: {set(DT)}, would you like to load it?')





    #execute below code only once to avoid duplication in SQLite table
    with open(file,'r') as fin:
        dr = csv.DictReader(fin, delimiter='\t')
        to_db = [(i['Category'] ,i['level'] ,i['distribution_channel'] ,i['period'] ,i['dt'] ,i['manufacturer'] ,i['brand'] ,i['BBSKU'] ,i['NAMESKU'] ,i['ean'] ,i['segment'] ,i['format'] ,i['tar_rmce'] ,i['vol'] ,i['val'] ,i['rcnt'] ,i['qty'] ,i['shvol'] ,i['shval'] ,i['shrcnt'] ,i['shqty'] ,i['dntot'] ,i['dn'] ,i['dnvol'] ,i['dnval'] ,i['dwqty'] ,i['dwvaltot'] ,i['shsvol'] ,i['shsval'] ,i['avp'] ,i['avpjm'] ,i['avtvol'] ,i['avtval'] ,i['avtqty'] ,i['avsvol'] ,i['avsval'] ,i['avsrcnt'] ,i['avsqty'] ,i['avgsku']) for i in dr]

    cur.executemany('INSERT INTO master_temp (Category ,level ,distribution_channel ,period ,dt ,manufacturer ,brand ,BBSKU ,NAMESKU ,ean ,segment ,format ,tar_rmce ,vol ,val ,rcnt ,qty ,shvol ,shval ,shrcnt ,shqty ,dntot ,dn ,dnvol ,dnval ,dwqty ,dwvaltot ,shsvol ,shsval ,avp ,avpjm ,avtvol ,avtval ,avtqty ,avsvol ,avsval ,avsrcnt ,avsqty ,avgsku) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', to_db)
    conn.commit()

    #print(conn.execute('SELECT * FROM master_temp').fetchall())


#archiving
for f in list(CSV_file): # moving file into archive folder
    CSV_file_name = os.path.basename(f)
    print(CSV_file_name)
    shutil.move(folder/CSV_file_name,folder_arch/CSV_file_name)


for F in list(folder_arch_A): #renaming in the archived folder
    CSV_file_name = os.path.basename(F)
    CSV_file_name_F = str(CSV_file_name[:-4])
    archiveName = str(CSV_file_name_F)+'_'+ str(current_dateTime+'.csv')
    shutil.move(folder_arch/F,folder_arch/archiveName)
'''


