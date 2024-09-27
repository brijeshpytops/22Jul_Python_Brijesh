from .dbConnection import cursor

def create_table():
    QuerySet = "create table students (student_id int primary key auto_increment, username varchar(255), email varchar(255), password varchar(255));"
    cursor.execute(QuerySet)


# alter table
# alter table students modify username varchar(255) not null unique;