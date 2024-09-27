from .dbConnection import cursor

def read_data():
    # QuerySet = "select * from students"
    # QuerySet = "select email, password from students"
    # QuerySet = "select email, password from students order by username"
    # QuerySet = "select email, password from students order by username DESC"
    # QuerySet = "select student_id from students order by student_id DESC limit 5"
    # QuerySet = "select student_id from students order by student_id"
    # QuerySet = "select student_id from students where student_id < 10"
    QuerySet = "select student_id from students where student_id < 10 and student_id > 5"
    cursor.execute(QuerySet)

    for student in cursor.fetchall():
        print(student)
