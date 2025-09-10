import tkinter as tk
from tkinter import messagebox
import os
import json
import header  # ✅ Make sure this is present and valid

STUDENT_FILE = "student_info.json"

# Load student data
def load_students():
    if not os.path.exists(STUDENT_FILE):
        return {}
    with open(STUDENT_FILE, "r") as f:
        return json.load(f)

# Save student data
def save_students(data):
    with open(STUDENT_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Update function
def update_info():
    student_id = entry_id.get().strip()
    new_name = entry_name.get().strip()
    new_email = entry_email.get().strip()
    new_password = entry_password.get().strip()

    if not student_id or not new_name or not new_email or not new_password:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    students = load_students()

    if student_id not in students:
        messagebox.showerror("Error", "Student ID not found.")
        return

    # Update fields
    students[student_id]["name"] = new_name
    students[student_id]["email"] = new_email
    students[student_id]["password"] = new_password

    save_students(students)
    messagebox.showinfo("Success", "Student information updated successfully.")

# GUI setup
root = tk.Tk()
root.title("Learnify")
root.geometry("600x450")
root.configure(bg="#ADD8E6")
root.eval('tk::PlaceWindow . center')

header.create_header(root)

font_label = ("Arial", 14)
font_entry = ("Arial", 14)
font_button = ("Arial", 14, "bold")

center_frame = tk.Frame(root, bg="#ADD8E6")
center_frame.pack(expand=True)

tk.Label(center_frame, text="Student ID:", bg="#ADD8E6", font=font_label).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_id = tk.Entry(center_frame, font=font_entry)
entry_id.grid(row=0, column=1, padx=10, pady=10)

tk.Label(center_frame, text="New Name:", bg="#ADD8E6", font=font_label).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(center_frame, font=font_entry)
entry_name.grid(row=1, column=1, padx=10, pady=10)

tk.Label(center_frame, text="New Email:", bg="#ADD8E6", font=font_label).grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(center_frame, font=font_entry)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(center_frame, text="New Password:", bg="#ADD8E6", font=font_label).grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_password = tk.Entry(center_frame, font=font_entry, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=10)

update_button = tk.Button(center_frame, text="Update Info", command=update_info, font=font_button, bg="#178080", fg="white")
update_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
