from app import app
from flask import render_template, request, redirect
import sqlite3
import datetime

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return "HELLO"


@app.route('/table')
def show_table():
    # retrieve billing due dates from database or file
    bills = get_billing_due_dates()
    for bill in bills:
        print("Id: ",bill[0])
        print("Name: ",bill[1])
        print("Email: ",bill[2])
        print("Salary: ",bill[3])
        print("\n")

    # render table page with due dat
    return render_template('table.html', bills=bills)

@app.route('/update_due_date', methods=['POST'])
def update_due_date():
    # retrieve form data
    billing_id = request.form['billing_id']
    new_due_date = request.form['due_date']

    # update due date in database or file
    update_billing_due_date(billing_id, new_due_date)

    # redirect to table page to refresh the table
    return redirect('/')


@app.route('/add_bill', methods=['GET', 'POST'])
def add_bill():
    if request.method == 'POST':
        # get the form data
        bill_name = request.form['bill_name']
        month_received = request.form['month_received']
        due_date = request.form['due_date']
        status = request.form['status']
        amount = request.form['amount']

        # create a connection to the database
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()

        # insert the bill into the database
        cursor.execute(
            'INSERT INTO bills (bill_name, month_received, due_date, status, amount) VALUES (?, ?, ?, ?, ?)',
            (bill_name, month_received, due_date, status, amount)
        )

        # commit the transaction
        conn.commit()

        # close the connection
        conn.close()

        # redirect to the bills page
        return redirect(url_for('show_bills'))
    else:
        # render the form template
        return render_template('add_bill.html')


def get_billing_due_dates():
     # create a connection to the database
    conn = get_db_connection()
    cursor= conn.cursor()

    # fetch the records from the database
    bills = conn.execute("SELECT * FROM bills").fetchall()

    # close the connection
    return bills
    # check if the table exists



def is_due_soon(due_date, days_before=5):
    # calculate the date X days before the due date
    threshold_date = due_date - datetime.timedelta(days=days_before)
    # check if the current date is within the threshold
    return threshold_date <= datetime.date.today() <= due_date

def check_due_dates():
    # create a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # fetch the bills from the database
    cursor.execute('SELECT * FROM bills WHERE status=?', ('Unpaid',))
    bills = cursor.fetchall()

    # close the connection
    conn.close()

    # check if any bills are due soon
    for bill in bills:
        due_date = bill['due_date']
        if is_due_soon(due_date):
            print(f'Bill "{bill["bill_name"]}" is due soon!')
