import tkinter as tk
from tkinter import messagebox
from auth_engine import register_user, login_user
from database import create_user_table

def open_register_window():
    reg_win = tk.Toplevel(root)
    reg_win.title("Register")

    tk.Label(reg_win, text="Username").grid(row=0, column=0)
    tk.Label(reg_win, text="Password").grid(row=1, column=0)

    username_entry = tk.Entry(reg_win)
    password_entry = tk.Entry(reg_win, show='*')

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def register():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register_user(username, password)
            messagebox.showinfo("Done", "Registered! Scan QR shown.")
            reg_win.destroy()
        else:
            messagebox.showerror("Error", "Fields can't be empty")

    tk.Button(reg_win, text="Register", command=register).grid(row=2, columnspan=2)

def open_login_window():
    login_win = tk.Toplevel(root)
    login_win.title("Login")

    tk.Label(login_win, text="Username").grid(row=0, column=0)
    tk.Label(login_win, text="Password").grid(row=1, column=0)
    tk.Label(login_win, text="OTP Code").grid(row=2, column=0)

    username_entry = tk.Entry(login_win)
    password_entry = tk.Entry(login_win, show='*')
    otp_entry = tk.Entry(login_win)

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    otp_entry.grid(row=2, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        otp = otp_entry.get()

        if login_user(username, password, otp):
            messagebox.showinfo("Success", "Login Successful ✅")
            login_win.destroy()
        else:
            messagebox.showerror("Failed", "Login Failed ❌")

    tk.Button(login_win, text="Login", command=login).grid(row=3, columnspan=2)

# MAIN WINDOW
root = tk.Tk()
root.title("Secure OS Login")

tk.Label(root, text="Secure Authentication", font=("Helvetica", 16)).pack(pady=10)

tk.Button(root, text="Register", width=20, command=open_register_window).pack(pady=5)
tk.Button(root, text="Login", width=20, command=open_login_window).pack(pady=5)

create_user_table()
root.mainloop()
