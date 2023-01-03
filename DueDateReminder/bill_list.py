import sqlite3

import random
import datetime

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor= connection.cursor()

#cursor.execute("create table bills (id INTEGER PRIMARY KEY AUTOINCREMENT, bill_name TEXT,\
#month_received TEXT,\
#due_date TEXT,\
#status TEXT,\
#amount INTEGER)")


## generate dummy data

bills = []

bill_names = ['Electricity', 'Water', 'Gas', 'Internet', 'Cable', 'Phone', 'Rent', 'Mortgage', 'Insurance', 'Subscription']
statuses = ['Paid', 'Unpaid']

for i in range(10):
    bill = {}
    bill['bill_name'] = random.choice(bill_names)
    bill['month_received'] = datetime.date.today().strftime('%B')
    bill['due_date'] = datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))
    bill['status'] = random.choice(statuses)
    bill['amount'] = random.randint(50, 500)
    bills.append(bill)

print(bills)

# insert each record into the database
for bill in bills:
    cursor.execute(
        'INSERT INTO bills (bill_name, month_received, due_date, status, amount) VALUES (?, ?, ?, ?, ?)',
        (bill['bill_name'], bill['month_received'], bill['due_date'], bill['status'], bill['amount'])
    )

connection.commit()
connection.close()
