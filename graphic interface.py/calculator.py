import tkinter as tk

# Define basic arithmetic functions
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result: " + str(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    label_result.config(text="Result: " + str(result))

# Create window and components
window = tk.Tk()
window.title("Calculator")

label1 = tk.Label(window, text="Number 1:")
label1.grid(column=0, row=0)

entry1 = tk.Entry(window)
entry1.grid(column=1, row=0)

label2 = tk.Label(window, text="Number 2:")
label2.grid(column=0, row=1)

entry2 = tk.Entry(window)
entry2.grid(column=1, row=1)

button_add = tk.Button(window, text="+", command=add)
button_add.grid(column=0, row=2)

button_subtract = tk.Button(window, text="-", command=subtract)
button_subtract.grid(column=1, row=2)

button_multiply = tk.Button(window, text="*", command=multiply)
button_multiply.grid(column=2, row=2)

button_divide = tk.Button(window, text="/", command=divide)
button_divide.grid(column=3, row=2)

label_result = tk.Label(window, text="Result:")
label_result.grid(column=0, row=3)

# Run the window loop
window.mainloop()
