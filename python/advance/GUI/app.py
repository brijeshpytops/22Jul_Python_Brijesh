import tkinter as tk
import re
from tkinter import messagebox
from myDatabase.insertData import insert_data_from_gui
from myDatabase.checkCredentials import check_credentials

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tops Technologies")
        self.root.geometry("400x400")
        logo_path = "images/logo.ico"
        self.root.iconbitmap(logo_path)

        self.main_screen()

    def main_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Welcome", font=("Arial", 20, "bold"), fg="red")
        title.pack(pady=20)

        register_button = tk.Button(self.root, text="Register", font=("Arial", 15), command=self.register_screen)
        register_button.pack(pady=10)

        login_button = tk.Button(self.root, text="Login", font=("Arial", 15), command=self.login_screen)
        login_button.pack(pady=10)

    def register_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Register", font=("Arial", 20, "bold"), fg="red")
        title.pack()

        username_label = tk.Label(self.root, text="Username:", font=("Arial", 15))
        username_label.pack()
        self.username_entry = tk.Entry(self.root, font=("Arial", 15))
        self.username_entry.pack()

        email_label = tk.Label(self.root, text="Email:", font=("Arial", 15))
        email_label.pack()
        self.email_entry = tk.Entry(self.root, font=("Arial", 15))
        self.email_entry.pack()

        password_label = tk.Label(self.root, text="Password:", font=("Arial", 15))
        password_label.pack()
        self.password_entry = tk.Entry(self.root, font=("Arial", 15), show="*")
        self.password_entry.pack()

        confirm_password_label = tk.Label(self.root, text="Confirm Password:", font=("Arial", 15))
        confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(self.root, font=("Arial", 15), show="*")
        self.confirm_password_entry.pack()

        submit_button = tk.Button(self.root, text="Submit", font=("Arial", 15), command=self.submit_handler)
        submit_button.pack(pady=20)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 15), command=self.main_screen)
        back_button.pack()

    def login_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Login", font=("Arial", 20, "bold"), fg="red")
        title.pack()

        email_label = tk.Label(self.root, text="Email:", font=("Arial", 15))
        email_label.pack()
        self.login_email_entry = tk.Entry(self.root, font=("Arial", 15))
        self.login_email_entry.pack()

        password_label = tk.Label(self.root, text="Password:", font=("Arial", 15))
        password_label.pack()
        self.login_password_entry = tk.Entry(self.root, font=("Arial", 15), show="*")
        self.login_password_entry.pack()

        login_button = tk.Button(self.root, text="Login", font=("Arial", 15), command=self.login_handler)
        login_button.pack(pady=20)

        back_button = tk.Button(self.root, text="Back", font=("Arial", 15), command=self.main_screen)
        back_button.pack()

    def validate_fields(self):
        username = self.username_entry.get() if hasattr(self, 'username_entry') else None
        email = self.email_entry.get() if hasattr(self, 'email_entry') else self.login_email_entry.get()
        password = self.password_entry.get() if hasattr(self, 'password_entry') else self.login_password_entry.get()
        confirm_password = self.confirm_password_entry.get() if hasattr(self, 'confirm_password_entry') else None

        if not username and hasattr(self, 'username_entry'):
            messagebox.showerror("Error", "Username cannot be empty.")
            return False
        if not email:
            messagebox.showerror("Error", "Email cannot be empty.")
            return False
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email address.")
            return False
        
        if not password:
            messagebox.showerror("Error", "Password cannot be empty.")
            return False
        
        if hasattr(self, 'password_entry') and not self.validate_password(password):
            messagebox.showerror("Error", "Password does not meet the requirements.")
            return False
        
        if confirm_password and password != confirm_password:
            messagebox.showerror("Error", "Password and confirm password do not match.")
            return False

        return True

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return re.match(pattern, password) is not None

    def submit_handler(self):
        if self.validate_fields():
            username = self.username_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()

            data = {'username': username, 'email': email, 'password': password}
            insert_data_from_gui(data)

            messagebox.showinfo("Success", "Registration successful.")
            self.main_screen()

    def login_handler(self):
        email = self.login_email_entry.get()
        password = self.login_password_entry.get()

        # Validate fields first
        if not email or not password:
            messagebox.showerror("Error", "Email and password cannot be empty.")
            return

        # Check credentials against the database
        if check_credentials(email, password):
            messagebox.showinfo("Success", "Login successful.")
            self.main_screen()  # Redirect to the main screen after successful login
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
