import tkinter as tk
from tkinter import messagebox
import json
import os
import uuid
import subprocess

# File paths
student_data_file = "student_info.json"
student_id_file = "student_ids.txt"

# Load existing student data
if os.path.exists(student_data_file):
    with open(student_data_file, "r") as f:
        student_info = json.load(f)
else:
    student_info = {}

# Save student info to files
def save_student_info(student_id, info):
    student_info[student_id] = info
    with open(student_data_file, "w") as f:
        json.dump(student_info, f, indent=4)
    with open(student_id_file, "a") as f:
        f.write(student_id + "\n")

# Open dashboard as new script
def show_dashboard():
    try:
        subprocess.Popen(["python", "Dashboard.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open dashboard: {e}")

# Sign-up window
def signup():
    def submit_signup():
        name = entry_name.get()
        father_name = entry_father.get()
        email = entry_email.get()
        age = entry_age.get()
        gender = gender_var.get()
        password = entry_password.get()

        if not (name and father_name and email and age and gender and password):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        student_id = str(uuid.uuid4())[:8]

        info = {
            "name": name,
            "father_name": father_name,
            "email": email,
            "age": age,
            "gender": gender,
            "password": password
        }

        save_student_info(student_id, info)
        messagebox.showinfo("Success", f"Sign up successful! Your ID is {student_id}")
        signup_window.destroy()
        show_dashboard()

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("400x400")
    signup_window.configure(bg="#FFF0F5")

    # Header frame (pack)
    header_frame = tk.Frame(signup_window, bg="#FFF0F5")
    header_frame.pack(fill="x")
    

    # Content frame (grid)
    form_frame = tk.Frame(signup_window, bg="#FFF0F5")
    form_frame.pack(fill="both", expand=True)

    fields = [
        ("Name", "entry_name"),
        ("Father Name", "entry_father"),
        ("Email", "entry_email"),
        ("Age", "entry_age"),
        ("Password", "entry_password")
    ]

    entries = {}

    for i, (label, var_name) in enumerate(fields):
        tk.Label(form_frame, text=label, bg="#FFF0F5").grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(form_frame, show="*" if "password" in var_name else None)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[var_name] = entry

    global entry_name, entry_father, entry_email, entry_age, entry_password
    entry_name = entries["entry_name"]
    entry_father = entries["entry_father"]
    entry_email = entries["entry_email"]
    entry_age = entries["entry_age"]
    entry_password = entries["entry_password"]

    tk.Label(form_frame, text="Gender", bg="#FFF0F5").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    gender_var = tk.StringVar()
    gender_frame = tk.Frame(form_frame, bg="#FFF0F5")
    gender_frame.grid(row=5, column=1, padx=10, pady=5)
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#FFF0F5").pack(side="left")
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#FFF0F5").pack(side="left")

    tk.Button(form_frame, text="Submit", command=submit_signup, bg="#0FDD3C", fg="white").grid(row=6, columnspan=2, pady=10)

# Login window
def login():
    def submit_login():
        student_id = entry_id.get()
        password = entry_password.get()

        if student_id in student_info and student_info[student_id]["password"] == password:
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            show_dashboard()
        else:
            messagebox.showerror("Error", "The student is not enrolled.")

    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("400x200")
    login_window.configure(bg="#F5F5DC")

    # Header (pack)
    header_frame = tk.Frame(login_window, bg="#F5F5DC")
    header_frame.pack(fill="x")
    

    # Content (grid)
    content_frame = tk.Frame(login_window, bg="#F5F5DC")
    content_frame.pack(fill="both", expand=True)

    tk.Label(content_frame, text="Student ID", bg="#F5F5DC").grid(row=0, column=0, padx=10, pady=10)
    entry_id = tk.Entry(content_frame)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(content_frame, text="Password", bg="#F5F5DC").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(content_frame, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(content_frame, text="Login", command=submit_login, bg="#2543F0", fg="white").grid(row=2, columnspan=2, pady=10)

# Main window
root = tk.Tk()
root.title("Learnify")
root.geometry("900x600")
root.configure(bg="#DBF4FD")



tk.Label(
    root,
    text="Welcome To Learnify \n where curiosity meets opportunity ",
    font=("Times New Roman", 24),
    bg="#DBF4FD"
).pack(pady=20)

tk.Button(root, text="Sign Up", command=signup, width=25, height=2, bg="#C72B25", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Login", command=login, width=25, height=2, bg="#58D348", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
