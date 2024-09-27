from .dbConnection import db, cursor

def check_credentials(email, password):
    # Use a parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM students WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()  # Fetch one user record
    cursor.close()  # Close the cursor
    return user is not None  # Return True if user exists, else False
