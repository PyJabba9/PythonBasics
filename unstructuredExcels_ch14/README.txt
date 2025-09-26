📊 Excel ETL Cleaner
🔎 About the project

This script takes several messy Excel workbooks (multiple sheets, inconsistent formats) and produces one clean, merged workbook.
It demonstrates a mini-ETL pipeline built in Python using openpyxl and dateutil.

⚙️ Features

Input: 3 Excel files with two sheets each (Sales, Returns)

Transformations:

Normalize dates with dateutil.parser → DD/MM/YYYY format

Clean strings (strip spaces, capitalize names)

Convert amounts to numeric values

Generate a temporary “hash column” to detect duplicates

Load: Merge all sheets into one final workbook with:

Sales sheet → combined Q1 + Q2 + Q3 sales

Returns sheet → combined Q1 + Q2 + Q3 returns

Removed duplicates

Headers re-added

Output: Sales_Processed.xlsx in the Processed folder

🛠️ Tools used

openpyxl → read/write Excel files

dateutil.parser → robust parsing of inconsistent date formats

Python lists + set() → deduplication logic

📂 Folder structure
unstructuredExcels_ch14/
│
├── Sales_Q1.xlsx
├── Sales_Q2.xlsx
├── Sales_Q3.xlsx
│
├── Temp/          # intermediate files with cleaned data
└── Processed/     # final merged file: Sales_Processed.xlsx

▶️ How to run
python excel_cleaner.py

📈 Example

Before (Q1 Sales):

Transaction Date | product   |  Country | AmountUSD
2025/01/05       |  Phone    | Germany  |  1823
05-02-25         | tablet    |  France  |  742


After (merged Sales):

Transaction Date | Product | Country | AmountUSD
05/01/2025       | Phone   | Germany | 1823
05/02/2025       | Tablet  | France  | 742
...

💡 Notes

The script is written as a learning exercise from Automate the Boring Stuff with Python (chapter 14).

It is not optimized for large files (>10k rows). For production workloads, use pandas + read_excel/to_excel.