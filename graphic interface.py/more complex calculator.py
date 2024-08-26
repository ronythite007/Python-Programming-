import tkinter as tk

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '^':
        result = power(num1, num2)
    elif operation == '%':
        result = mod(num1, num2)
    else:
        result = "Invalid operation"

    result_label.config(text=result)

# create GUI window
window = tk.Tk()
window.title("Calculator")

# create entry fields and labels for input
entry1 = tk.Entry(window)
entry1.grid(row=0, column=0)
label1 = tk.Label(window, text="Enter first number:")
label1.grid(row=0, column=1)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=0)
label2 = tk.Label(window, text="Enter second number:")
label2.grid(row=1, column=1)

# create drop-down menu for selecting operation
operations = ['+', '-', '*', '/', '^', '%']
operation_var = tk.StringVar(window)
operation_var.set(operations[0]) # set default value
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.grid(row=2, column=0)

# create button to calculate result
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0)

# create label to display result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0)

# start the GUI
window.mainloop()
