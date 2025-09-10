import tkinter as tk
from tkinter import messagebox
import random
import header  #  header module


# Suggestion Logic Function

def suggest_courses():
    name = entry_name.get().strip()
    q1 = entry_q1.get().strip().lower()
    q2 = entry_q2.get().strip().lower()
    q3 = entry_q3.get().strip().lower()

    suggestions = []

    if "data" in q1 or "problem" in q3:
        suggestions.append("Data Science")
    if "creativity" in q1 or "art" in q3:
        suggestions.append("Graphic Design")
    if "business" in q1 or "selling" in q3:
        suggestions.append("Marketing")
    if "security" in q2:
        suggestions.append("Cybersecurity")
    if "technology" in q2:
        suggestions.append("Computer Science")
    if "design" in q2:
        suggestions.append("UI/UX Design")

    if suggestions:
        messagebox.showinfo("Course Suggestions", f"{name}, we suggest you explore: {', '.join(suggestions)}")
    else:
        messagebox.showinfo("Course Suggestions", "Please answer more clearly to get suggestions.")

# GUI Setup
root = tk.Tk()
root.title("Learnify")
root.geometry("600x500")
root.configure(bg="#e0f7fa")
root.eval('tk::PlaceWindow . center')

# Add the navigation header
header.create_header(root)

# Main content frame
main_frame = tk.Frame(root, bg="#e0f7fa")
main_frame.pack(expand=True, fill="both")


# Input Widgets
tk.Label(main_frame, text="Enter Student Name:", font=("Arial", 13), bg="#e0f7fa").pack()
entry_name = tk.Entry(main_frame, width=40, font=("Arial", 12))
entry_name.pack(pady=5)

tk.Label(main_frame, text="1. Do you prefer working with data, creativity, or business?", font=("Arial", 13), bg="#e0f7fa").pack(pady=10)
entry_q1 = tk.Entry(main_frame, width=50, font=("Arial", 12))
entry_q1.pack()

tk.Label(main_frame, text="2. Are you interested in technology, security, or design?", font=("Arial", 13), bg="#e0f7fa").pack(pady=10)
entry_q2 = tk.Entry(main_frame, width=50, font=("Arial", 12))
entry_q2.pack()

tk.Label(main_frame, text="3. Do you like problem solving, selling ideas, or creating art?", font=("Arial", 13), bg="#e0f7fa").pack(pady=10)
entry_q3 = tk.Entry(main_frame, width=50, font=("Arial", 12))
entry_q3.pack()

tk.Button(
    main_frame,
    text="Suggest Courses",
    command=suggest_courses,
    font=("Arial", 13, "bold"),
    bg="#148073",
    fg="white",
    padx=10,
    pady=5
).pack(pady=20)

# Start the GUI loop

root.mainloop()
