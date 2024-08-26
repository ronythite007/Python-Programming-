import tkinter as tk
from tkinter import messagebox
from tabulate import tabulate
import pandas as pd

# In-memory user database
user_data = {}
current_user_email = None  # Track the email of the currently logged-in user

# Sample doctor schedule
doctor_schedule = {
    "Doctor Name": ["Dr. Peter Parker", "Dr. Joshi", "Dr. Kulkarni", "Dr. Shukla"],
    "Education": ["MBBS MS", "MBBS MS", "MBBS MS", "MBBS MS"],
    "Speciality": ["Surgeon", "Surgeon", "Baby specialist", "Women Specialist"],
    "Availability Time": ["7:00 to 10:00", "7:00 to 10:00", "9:00 to 12:00", "7:00 to 10:00"],
    "Action": ["P", "J", "K", "S"]
}

# Create the main window
root = tk.Tk()
root.title("City Hospital Appointment Booking")

# Function to handle login
def login():
    global current_user_email
    email = entry_email.get()
    password = entry_password.get()

    if email in user_data and user_data[email]["password"] == password:
        current_user_email = email
        show_basic_info_form()
    else:
        messagebox.showerror("Login Failed", "Invalid email or password.")

# Create and place login widgets
label_email = tk.Label(root, text="Email ID:")
label_password = tk.Label(root, text="Password:")
entry_email = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
button_login = tk.Button(root, text="Login", command=login)

# Function to show basic info form
def show_basic_info_form():
    clear_login_form()
    label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    label_age.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    label_contact.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_name.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entry_age.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    entry_contact.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    button_continue.grid(row=5, column=0, columnspan=2, pady=10)

# Function to clear login form
def clear_login_form():
    label_email.grid_forget()
    label_password.grid_forget()
    entry_email.grid_forget()
    entry_password.grid_forget()
    button_login.grid_forget()

# Function to handle continuing to make an appointment
def continue_to_make_appointment():
    name = entry_name.get()
    age = entry_age.get()
    contact = entry_contact.get()

    if name and age and contact:
        show_doctor_schedule()
    else:
        messagebox.showerror("Incomplete Information", "Please fill in all fields.")

# Create and place basic info widgets
label_name = tk.Label(root, text="Name:")
label_age = tk.Label(root, text="Age:")
label_contact = tk.Label(root, text="Contact Number:")
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_contact = tk.Entry(root)
button_continue = tk.Button(root, text="Continue", command=continue_to_make_appointment)

# Function to show doctor schedule
def show_doctor_schedule():
    clear_basic_info_form()
    df = pd.DataFrame(doctor_schedule)
    doctor_schedule_table = tabulate(df, headers="keys", tablefmt="pretty")  # Format the doctor schedule as a table
    messagebox.showinfo("Doctor Schedule", doctor_schedule_table)
    button_appointment.grid(row=1, column=0, columnspan=2, pady=10)

# Function to clear basic info form
def clear_basic_info_form():
    label_name.grid_forget()
    label_age.grid_forget()
    label_contact.grid_forget()
    entry_name.grid_forget()
    entry_age.grid_forget()
    entry_contact.grid_forget()
    button_continue.grid_forget()

# Create and place appointment widgets
button_appointment = tk.Button(root, text="Make Appointment", command="make_appointment")

# Place login widgets initially
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_password.grid(row=1, column=1, padx=10, pady=5, sticky="w")
button_login.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()
