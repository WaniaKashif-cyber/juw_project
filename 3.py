import tkinter as tk
from tkinter import ttk

# List of courses
courses = [
    "Python",
    "Java",
    "Web Development",
    "Data Science",
    "Cyber Security",
    "Video Game Developer",
    "App Developer",
    "Ethical Hacking",
    "Cloud Computing",
    "Digital Marketing",
    "Data Analysis",
    "Machine Learning",
    

]

# Create main window
root = tk.Tk()
root.title("Course Catalog")
root.geometry("700x550")
root.configure(bg="#E0F7FA")  

# Heading (Centered and with larger font)
title = tk.Label(
    root,
    text="📚 Available Courses",
    font=("Helvetica", 24, "bold"),
    bg="#E0F7FA",
    fg="#333"
)
title.pack(pady=20)

# Create frame to hold course cards
course_frame = tk.Frame(root, bg="#E0F7FA")
course_frame.pack(pady=10)

# Create course "cards"
def create_course_cards():
    columns = 3
    for idx, course in enumerate(courses):
        row = idx // columns
        col = idx % columns

        # Each course card
        card = tk.Frame(
            course_frame,
            bg="white",
            bd=2,
            relief="groove",
            width=180,
            height=100
        )
        card.grid(row=row, column=col, padx=20, pady=20)

        label = tk.Label(
            card,
            text=course,
            bg="white",
            fg="#007ACC",
            font=("Arial", 14, "bold"),
            wraplength=160,
            justify="center"
        )
        label.place(relx=0.5, rely=0.5, anchor="center")

create_course_cards()

# Run the app
root.mainloop()
