import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $).")

    common_passwords = ['password', '123456', 'qwerty', 'abc123']
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords.")

    if score >= 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, feedback = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}")
    
    feedback_text.delete(1.0, tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n\n")
        for item in feedback:
            feedback_text.insert(tk.END, f"- {item}\n")
    else:
        feedback_text.insert(tk.END, "Your password looks great!")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("700x600")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text=" Password Strength Checker ", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Password Entry Label
label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=5)

# Password Entry Field
entry = tk.Entry(root, width=35, show='*', font=("Arial", 12))
entry.pack(pady=5)

# Check Button
check_button = tk.Button(root, text="Check Strength", font=("Arial", 12, "bold"), command=on_check, bg="#4CAF50", fg="white", padx=10, pady=5)
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

# Feedback/Suggestions Text Box (Bigger size)
feedback_text = tk.Text(root, height=12, width=60, font=("Arial", 11), wrap="word")
feedback_text.pack(pady=10, padx=15, expand=True, fill='both')

# Run the GUI loop
root.mainloop()
