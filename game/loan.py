import math
import tkinter as tk
from tkinter import Label, Entry, Button

class Money:
    def __init__(self):
        self.loan = 0
        self.rate = 0.0
        self.duration = 0

def calculate_loan():
    money = Money()

    money.loan = float(loan_entry.get())
    money.rate = float(rate_entry.get())
    money.duration = int(duration_entry.get())

    rate_of_interest = money.rate / 100.0

    result_text.set("Months\t\tInstallment\tInterest\t\tTotal Pay\tBalance\n")

    installment = money.loan / money.duration
    interest = (money.loan * rate_of_interest) / money.duration
    total_pay = installment + interest
    balance = money.loan - installment
    
    
    for i in range(2, money.duration + 1):
        monthly_interest = (balance * rate_of_interest) / money.duration
        total_pay = installment + monthly_interest
        balance -= installment

        result_text.set(result_text.get() + f"Month{i}\t\t{math.ceil(installment)}\t\t{math.ceil(interest)}\t\t{math.ceil(total_pay)}\t\t{math.ceil(balance)}\n")

root = tk.Tk()
root.title("Loan Calculator")
root.geometry("500x400")
heading = Label(root, text="The Loan Calculator",bg="light blue",fg="black",padx=13,pady="10",font="comicsansms  10 bold")
heading.pack()
loan_label = Label(root, text="Loan Amount:")
loan_label.pack()
loan_entry = Entry(root)
loan_entry.pack()

rate_label = Label(root, text="Interest Rate (%):")  
rate_label.pack()
rate_entry = Entry(root)
rate_entry.pack()

duration_label = Label(root, text="Loan Duration (months):")
duration_label.pack()
duration_entry = Entry(root)
duration_entry.pack()

calculate_button = Button(root, text="Calculate", command=calculate_loan)
calculate_button.pack()

result_text = tk.StringVar()
result_label = Label(root, textvariable=result_text, justify="left")
result_label.pack()
thank=Label(root,text="Thank You For Using Our Software",bg="light blue",fg="black",padx=1300,pady="10",font="comicsansms  10 bold")
thank.pack(side="bottom")
root.mainloop()
