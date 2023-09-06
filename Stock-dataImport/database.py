import sqlite3

conn=sqlite3.connect('stock.db')
c=conn.cursor()
sq_text='''CREATE TABLE stockCode(id INTEGER PRIMARY KEY AUTOINCREMENT,code TEXT,code_name TEXT,update_date TEXT)'''
c.execute(sq_text)
conn.commit()
conn.close()
