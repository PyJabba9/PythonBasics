
I will recreate part of my routine at work, loading csv into SSMS, but as I dont have work SSMS available, I will load data into SQLite and later on I will modify the script with pyodbc as syntax stays the same.
Task:
Extract data from .csv file in the folder into SQLite (and after that to SSMS - as I have it at work :) )

- check folder for .csv file. +
- load csv for the analysis into temp_temp table +
- ask user if this is the file to be loaded, provide min(DT)/max(DT) from file contents+
- if no - exit AND delete temp_temp contents +
- if yes - copy temp_temp into master_temp for further processing within SQL and loading into final tables (out of scope) +
- save SQLite+
- move file into /Archive folder?????

DQ check before loading:
1. Takes sqlite table +
2. Outputs number of rows per date AND sum of volume per date +
3. Compares it to average number and sum of volume +
4. If difference is > 25% - inform user +
5. If all OK - copy data from temp_temp into master_temp table and delete temp_temp contents
