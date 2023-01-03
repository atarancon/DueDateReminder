
DROP TABLE IF EXISTS bills;

CREATE TABLE bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_name TEXT NOT NULL ,
    month_received TEXT NOT NULL,
    due_date TEXT NOT NULL  ,
    status TEXT NOT NULL ,
    amount INTEGER NOT NULL
);
