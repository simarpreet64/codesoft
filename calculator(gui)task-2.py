import tkinter as tk

# Function to evaluate the expression
def abc():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("My Own Calculator")

# StringVar to store the result
result = tk.StringVar()

# Entry widget to input expression
entry = tk.Entry(root, textvariable=result, font=('Arial', 30))
entry.grid( column=0, row=0, columnspan=5, padx=15, pady=25, sticky="nsew")

# Buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '%', '+'
]

row_num = 1
col_num = 0
for button in buttons:
    tk.Button(root, text=button, font=('Arial', 20), command=lambda button=button: entry.insert(tk.END, button)).grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Button to evaluate expression
tk.Button(root, text="=", font=('Arial', 20), command=abc).grid(row=row_num, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Configure rows and columns to expand with the window
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
