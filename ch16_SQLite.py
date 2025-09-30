import sqlite3, csv
from pathlib import Path

folder = Path('C:/Users/junke/mu_code/pythonScripts/SQLite_ch16/')
conn = sqlite3.connect(f'{folder}.ch16.SQLite_practice.db', isolation_level = None)
cur = conn.cursor()
'''
conn.execute('CREATE TABLE IF NOT EXISTS products (product_id NUMERIC NOT NULL,product_name TEXT, category TEXT, price NUMERIC)') # unfortunately STRICT parameter could not be used as MuCode is no longer supported :(




#conn.execute('DELETE FROM sales')

#conn.execute('DELETE FROM sales')
with open('C:/Users/junke/mu_code/pythonScripts/SQLite_ch16/sales.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['sale_id'],i['product_id'],i['customer_id'],i['quantity'],i['sale_date'],i['amount']) for i in dr]

cur.executemany('INSERT INTO sales (sale_id,product_id,customer_id,quantity,sale_date,amount) VALUES(?,?,?,?,?,?);', to_db)
conn.commit()
with open('C:/Users/junke/mu_code/pythonScripts/SQLite_ch16/products.csv','r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['product_id'],i['product_name'],i['category'],i['price']) for i in dr]

cur.executemany('INSERT INTO products (product_id,product_name,category,price) VALUES(?,?,?,?);', to_db)
conn.commit()

#print(conn.execute('SELECT product_id, SUM(amount) as ["Total sales"] FROM sales WHERE product_id = "39"').fetchall())
print(conn.execute('SELECT products.product_name, SUM(sales.amount) as ["Total sales"] FROM sales INNER JOIN products ON sales.product_id = products.product_id  GROUP BY products.product_name ').fetchall())
'''
print(conn.execute('SELECT customers.segment, SUM(sales.amount) as ["Sales by segment"] FROM sales INNER JOIN customers ON sales.customer_id = customers.customer_id  GROUP BY customers.segment ').fetchall())
