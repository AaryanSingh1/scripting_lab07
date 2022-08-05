import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

var = cur.fetchall()

requirement = cur.execute('SELECT name, age FROM table1 WHERE age > 50')

for x in requirement:
    print(f'{x} years old')

con.commit()
con.close()