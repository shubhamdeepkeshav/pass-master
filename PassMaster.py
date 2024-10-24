import random
import tkinter as tk
from tkinter import scrolledtext

def generate_passwords():
    MY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=.,?0123456789'
    a = int(num_passwords_entry.get())
    b = int(password_length_entry.get())
    passwords = []

    for _ in range(a):
        s = ''.join(random.choice(MY) for _ in range(b))
        passwords.append(s)
    
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, '\n'.join(passwords))  # Insert new passwords

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entries for number of passwords and length
tk.Label(root, text="Number of Passwords:").grid(row=0, column=0)
num_passwords_entry = tk.Entry(root)
num_passwords_entry.grid(row=0, column=1)

tk.Label(root, text="Password Length:").grid(row=1, column=0)
password_length_entry = tk.Entry(root)
password_length_entry.grid(row=1, column=1)

# Create a button to generate passwords
generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.grid(row=2, columnspan=2)

# Create a scrolled text area to display passwords
output_text = scrolledtext.ScrolledText(root, width=40, height=10)
output_text.grid(row=3, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
