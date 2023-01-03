import random
import datetime

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

print(bills[0])
