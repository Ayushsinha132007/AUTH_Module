import ctypes
import sys
import os
from tkinter import messagebox
from gui import open_login_window  # Reuse your GUI login screen

# Windows lock function
def lock_windows():
    ctypes.windll.user32.LockWorkStation()

def main():
    # Reuse your existing GUI Login function
    try:
        open_login_window()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        lock_windows()

if __name__ == "__main__":
    main()
