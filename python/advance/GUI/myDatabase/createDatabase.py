from .dbConnection import cursor

def create_database():
    database_name = input("Enter a database name: ")
    QuerySet = f"create database {database_name}"
    cursor.execute(QuerySet)
