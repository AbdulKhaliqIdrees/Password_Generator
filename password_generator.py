#Import Modules
import tkinter as a
from tkinter import ttk
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, complexity):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not characters:
        return "Error: No character types selected."
    if complexity == "weak":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "strong":
        pass
    else:
        characters += string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def generate_password_and_display():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        complexity = complexity_var.get()
        if length <= 0:
            password_label.config(text="Length must be greater than zero. Please try again.", fg="red")
        else:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special, complexity)
            password_label.config(text=f"Generated Password: {password}", fg="black")
    except ValueError:
        password_label.config(text="Invalid input. Please enter a valid number.", fg="red")
root = a.Tk()
root.title("Password Generator")
length_label = a.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=10)
length_entry = a.Entry(root, width=30)
length_entry.pack()
complexity_frame = ttk.LabelFrame(root, text="Password Complexity")
complexity_frame.pack(pady=10)
uppercase_var = a.BooleanVar()
uppercase_check = ttk.Checkbutton(complexity_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(anchor=a.W)
lowercase_var = a.BooleanVar()
lowercase_check = ttk.Checkbutton(complexity_frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack(anchor=a.W)
digits_var = a.BooleanVar()
digits_check = ttk.Checkbutton(complexity_frame, text="Include Digits", variable=digits_var)
digits_check.pack(anchor=a.W)
special_var = a.BooleanVar()
special_check = ttk.Checkbutton(complexity_frame, text="Include Special Characters", variable=special_var)
special_check.pack(anchor=a.W)
complexity_var = a.StringVar()
complexity_var.set("normal")
complexity_label = a.Label(root, text="Select Complexity Level:")
complexity_label.pack()
weak_radio = ttk.Radiobutton(root, text="Weak", variable=complexity_var, value="weak")
weak_radio.pack(anchor=a.W)
normal_radio = ttk.Radiobutton(root, text="Normal", variable=complexity_var, value="normal")
normal_radio.pack(anchor=a.W)
strong_radio = ttk.Radiobutton(root, text="Strong", variable=complexity_var, value="strong")
strong_radio.pack(anchor=a.W)
generate_button = a.Button(root, text="Generate Password", command=generate_password_and_display)
generate_button.pack(pady=10)
password_label = a.Label(root, text="", wraplength=300)
password_label.pack()
root.mainloop()