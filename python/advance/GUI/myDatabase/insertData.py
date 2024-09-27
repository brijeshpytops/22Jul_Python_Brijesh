from .dbConnection import cursor, db

# def insert_data():
#     QuerySet = "insert into students(username, email, password) values ('brijesh07', 'brijesh@gmail.com', 'test@123');"
#     cursor.execute(QuerySet)
#     db.commit()

# show all the data from specific table
# select * from table_name;

def insert_data_from_gui(data):
    print(data)
    QuerySet = f"insert into students(username, email, password) values ('{data['username']}', '{data['email']}', '{data['password']}');"
    cursor.execute(QuerySet)
    db.commit()
