import tkinter as tk
import re

screen = tk.Tk()

screen.title("Tops techjnologies")

screen.geometry("400x400")

logo_path = "images/logo.ico"

screen.iconbitmap(logo_path)

title = tk.Label(screen, text="Register", font=("Arial", 20, "bold"), fg="red")
title.pack()

# Create a frame as the underline
underline = tk.Frame(screen, height=2, width=title.winfo_reqwidth(), bg="red")
underline.pack()

# Adjust underline width after the label is displayed
def adjust_underline():
    underline.config(width=title.winfo_width())

screen.after(10, adjust_underline)

# Entry fields

username_label = tk.Label(screen, text="Username:", font=("Arial", 15))
username_label.pack()
username_entry = tk.Entry(screen, font=("Arial", 15))
username_entry.pack()

email_label = tk.Label(screen, text="Email:", font=("Arial", 15))
email_label.pack()
email_entry = tk.Entry(screen, font=("Arial", 15))
email_entry.pack()

password_label = tk.Label(screen, text="Password:", font=("Arial", 15))
password_label.pack()
password_entry = tk.Entry(screen, font=("Arial", 15), show="*")
password_entry.pack()

confirm_password_label = tk.Label(screen, text="Confirm Password:", font=("Arial", 15))
confirm_password_label.pack()
confirm_password_entry = tk.Entry(screen, font=("Arial", 15), show="*")
confirm_password_entry.pack()

def validate_fields():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    def validate_email(email):
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password) is not None

    if not username:
        tk.messagebox.showerror("Error", "Username cannot be empty.")
        return False
    if not email:
        tk.messagebox.showerror("Error", "Email cannot be empty.")
        return False
    
    if not validate_email(email):
        tk.messagebox.showerror("Error", "Invalid email address.")
        return False
    
    if not password:
        tk.messagebox.showerror("Error", "Password cannot be empty.")
        return False
    
    if not validate_password(password):
        tk.messagebox.showerror("Error", "Password does not meet the requirements.")
        return False
    
    if password!= confirm_password:
        tk.messagebox.showerror("Error", "Password and confirm password do not match.")

    return True

def submit_handler():
    if validate_fields():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Confirm Password: {confirm_password}")

        print("Form submitted successfully")

    
    
submit_button = tk.Button(screen, text="Submit", font=("Arial", 15), command=submit_handler)
submit_button.pack()

# Placeholder for validation



screen.mainloop()