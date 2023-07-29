import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_and_show_password():
    try:
        length = int(length_var.get())
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        password = generate_password(length, use_digits, use_special_chars)

        result_var.set(password)
    except ValueError: 
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

# GUI elements
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include digits", variable=digits_var, onvalue=True, offvalue=False)
digits_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var, onvalue=True, offvalue=False)
special_chars_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_show_password)
generate_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=250)
result_label.pack()

# Start the main event loop
root.mainloop()

