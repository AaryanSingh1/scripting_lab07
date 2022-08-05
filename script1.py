from faker import Faker 
import sqlite3
from datetime import datetime

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS table1(name text, address text, email text, age integer, date text)''')

def main():
    content = Faker()
    name = content.name();
    address = content.address();
    email = content.email();
    age = content.random_number(digits=2);
    date = content.date_this_month();

    cur.execute('INSERT INTO table1 VALUES (:name, :address, :email, :age, :date)',
    {'name': name, 'address': address, 'email': email, 'age': age, 'date': date}
    )
    

for i in range (200):
    main()

cur.execute('SELECT * FROM table1')
        
con.commit()
con.close()


