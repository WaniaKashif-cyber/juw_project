import tkinter as tk
import os

def create_header(root):
    header_frame = tk.Frame(root, bg="#003366")
    header_frame.pack(fill=tk.X)

    pages = {
        "Dashboard": "Dashboard.py",
        "Signup": "signup.py",
        "Update Profile": "update_profile.py",
        "   Enroll Courses": "Courses.py",
        "Courses": "3.py"      
    }

    for name, file in pages.items():
        btn = tk.Button(
            header_frame,
            text=name,
            bg="#0066cc",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=10,
            pady=5,
            command=lambda f=file: os.system(f"python {f}")
        )
        btn.pack(side=tk.LEFT, padx=10, pady=10)
