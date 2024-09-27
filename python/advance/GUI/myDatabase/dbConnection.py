import mysql.connector

db = mysql.connector.connect(
    user='root', 
    password='root',  
    host='127.0.0.1',
    database='tops'
)

cursor = db.cursor()