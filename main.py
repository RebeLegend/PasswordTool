import tkinter as tk
from tkinter import messagebox
import re

#Search txt file for common passwords
def is_common_password(password, common_passwords_file='10k-most-common.txt'):
    with open(common_passwords_file, 'r') as file:
        common_passwords = {line.strip() for line in file.readlines()}
    return password in common_passwords

def check_password_strength(password):
    if is_common_password(password):
        return "Very Weak (Common Password)"

    # Criteria for password strength
    min_length = 8
    contains_upper = re.search(r"[A-Z]", password) is not None
    contains_lower = re.search(r"[a-z]", password) is not None
    contains_digit = re.search(r"[0-9]", password) is not None
    contains_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Checking the password strength
    strength = 0
    if len(password) >= min_length:
        strength += 1
    if contains_upper:
        strength += 1
    if contains_lower:
        strength += 1
    if contains_digit:
        strength += 1
    if contains_special:
        strength += 1

    # Evaluating overall strength
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    else:
        return "Weak"

def on_submit():
    password = password_entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"The password strength is: {strength}")

# Setting up the GUI window
window = tk.Tk()
window.title("Password Strength Checker")

# Creating widgets
tk.Label(window, text="Enter your password:").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()
tk.Button(window, text="Check Strength", command=on_submit).pack()

# Run the application
window.mainloop()
