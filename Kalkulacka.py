import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        messagebox.showerror("Invalid input", "Please select a valid operation")
        return

    result_label.config(text=f"Result: {result}")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar()
operation_var.set('1')

tk.Label(root, text="Select operation:").grid(row=2, column=0)
tk.Radiobutton(root, text="Add", variable=operation_var, value='1').grid(row=2, column=1)
tk.Radiobutton(root, text="Subtract", variable=operation_var, value='2').grid(row=3, column=1)
tk.Radiobutton(root, text="Multiply", variable=operation_var, value='3').grid(row=4, column=1)
tk.Radiobutton(root, text="Divide", variable=operation_var, value='4').grid(row=5, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0)
tk.Button(root, text="Exit", command=exit_program).grid(row=6, column=1)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()

