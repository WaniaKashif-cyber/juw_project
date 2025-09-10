import tkinter as tk
from tkinter import messagebox
import os
import header  # Import the header navigation

# ---------- Data Setup ----------
available_courses = ["Data Security","cyber security" , "web development","app development"," digital marketing","Ethical hacking","Video game developer","Cloud computing",  "Data Analysis","Machine Learning","Artificial Intelligence"]
data_file = "students.txt"
student_enrollments = {}

# ---------- File Handling ----------
def load_from_file():
    student_enrollments.clear()
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        student_id, name, courses_str = parts
                        courses = courses_str.split(",") if courses_str else []
                        student_enrollments[student_id] = {"name": name, "courses": courses}

def save_to_file():
    with open(data_file, "w") as f:
        for student_id, info in student_enrollments.items():
            courses_str = ",".join(info["courses"])
            f.write(f"{student_id}|{info['name']}|{courses_str}\n")

# ---------- Core Logic ----------
def enroll_course():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    selected_indices = course_listbox.curselection()

    if not student_id or not name:
        messagebox.showwarning("Input Error", "Please enter both Student ID and Name.")
        return

    if not selected_indices:
        messagebox.showwarning("No Course Selected", "Please select at least one course.")
        return

    selected_courses = [available_courses[i] for i in selected_indices]

    if student_id not in student_enrollments:
        student_enrollments[student_id] = {"name": name, "courses": []}
    else:
        student_enrollments[student_id]["name"] = name

    current_courses = student_enrollments[student_id]["courses"]
    added_courses = []

    for course in selected_courses:
        if course not in current_courses:
            if len(current_courses) < 2:
                current_courses.append(course)
                added_courses.append(course)
            else:
                messagebox.showerror("Limit Reached", f"{name} can only be enrolled in 2 courses.")
                break

    if added_courses:
        save_to_file()
        messagebox.showinfo("Enrolled", f"{name} enrolled in: {', '.join(added_courses)}")

    update_enrollment_display(student_id)

def update_enrollment_display(student_id):
    student = student_enrollments.get(student_id)
    if student:
        enrolled = student["courses"]
        name = student["name"]
        enrolled_courses_label.config(text=f"{name}'s Courses: {', '.join(enrolled)}")
    else:
        enrolled_courses_label.config(text="")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Learnify")
root.geometry("700x500")
root.configure(bg="#E0F7FA")
root.eval('tk::PlaceWindow . center')

header.create_header(root)  # Add top header navigation

font_label = ("Arial", 14)
font_entry = ("Arial", 14)
font_button = ("Arial", 14, "bold")

center_frame = tk.Frame(root, bg="#E0F7FA")
center_frame.pack(expand=True)

# Student ID
tk.Label(center_frame, text="Student ID:", bg="#E0F7FA", font=font_label).grid(row=0, column=0, padx=10, pady=10, sticky="e")
id_entry = tk.Entry(center_frame, font=font_entry)
id_entry.grid(row=0, column=1, padx=10, pady=10)

# Student Name
tk.Label(center_frame, text="Student Name:", bg="#E0F7FA", font=font_label).grid(row=1, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(center_frame, font=font_entry)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# Course List
tk.Label(center_frame, text="Select Courses (max 2):", bg="#E0F7FA", font=font_label).grid(row=2, column=0, padx=10, pady=10, sticky="ne")
course_listbox = tk.Listbox(center_frame, selectmode=tk.MULTIPLE, height=5, font=font_entry, exportselection=0)
for course in available_courses:
    course_listbox.insert(tk.END, course)
course_listbox.grid(row=2, column=1, padx=10, pady=10)

# Enroll Button
enroll_button = tk.Button(center_frame, text="Enroll", command=enroll_course, font=font_button, bg="#4CAF50", fg="white")
enroll_button.grid(row=3, column=0, columnspan=2, pady=20)

# Enrollment Status
enrolled_courses_label = tk.Label(center_frame, text="", bg="#E0F7FA", font=font_label)
enrolled_courses_label.grid(row=4, column=0, columnspan=2, pady=10)

# Load existing data
load_from_file()

root.mainloop()
