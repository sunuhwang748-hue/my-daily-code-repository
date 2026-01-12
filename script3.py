import tkinter as tk

expression = ""

def check(char):
    allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '+', '-', '*', '/', '.', '(', ')', '×', '÷', '=', '']
    return char in allowed

def click_button(value):
    global expression
    current_content = entry.get()

    if value == "=":
        full_expr = expression + current_content
        full_expr = full_expr.replace('×', '*').replace('÷', '/')
        if full_expr:
            try:
                result = eval(full_expr)
                print(result)
                entry.config(validate="none")
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
                entry.config(validate="key")
                expression = ""
            except:
                print("Error")
                entry.config(validate="none")
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
                entry.config(validate="key")
                expression = ""

    elif value == "C":
        expression = ""
        entry.config(validate="none")
        entry.delete(0, tk.END)
        entry.config(validate="key")

    elif value == "Del":
        entry.delete(len(current_content) - 1)

    elif value in ["+", "-", "×", "÷"]:
        if current_content:
            expression += current_content + value
            entry.config(validate="none")
            entry.delete(0, tk.END)
            entry.config(validate="key")
        elif expression and expression[-1] in ["+", "-", "×", "÷"]:
            expression = expression[:-1] + value

    elif value == "+/-":
        if current_content:
            entry.config(validate="none")
            if current_content.startswith('-'):
                entry.delete(0)
            else:
                entry.insert(0, '-')
            entry.config(validate="key")

    elif value == "( )":
        total_str = expression + current_content
        open_cnt = total_str.count('(')
        close_cnt = total_str.count(')')
        if open_cnt > close_cnt and (current_content and current_content[-1].isdigit()):
            entry.insert(tk.END, ")")
        else:
            entry.insert(tk.END, "(")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Jensen's Calc")

vcmd = root.register(check)

entry = tk.Entry(root, width=20, font=("Arial", 18), bd=0,
                 highlightthickness=0, justify='right', bg="#eeeeee",
                 validate="key", validatecommand=(vcmd, '%S'))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

root.bind('<Return>', lambda event: click_button("="))
root.bind('=', lambda event: click_button("="))
root.bind('<parenleft>', lambda event: entry.insert(tk.END, "("))
root.bind('<parenright>', lambda event: entry.insert(tk.END, ")"))

def add_button(text, row, column):
    button = tk.Button(root, text=text, width=4, height=2,
                       command=lambda: click_button(str(text)))
    button.grid(row=row, column=column, sticky='nsew')

add_button("C", 1, 0)
add_button("Del", 1, 1)
add_button("( )", 1, 2)
add_button("÷", 1, 3)
add_button(7, 2, 0)
add_button(8, 2, 1)
add_button(9, 2, 2)
add_button("×", 2, 3)
add_button(4, 3, 0)
add_button(5, 3, 1)
add_button(6, 3, 2)
add_button("-", 3, 3)
add_button(1, 4, 0)
add_button(2, 4, 1)
add_button(3, 4, 2)
add_button("+", 4, 3)
add_button("+/-", 5, 0)
add_button(0, 5, 1)
add_button(".", 5, 2)
add_button("=", 5, 3)

for i in range(4): root.grid_columnconfigure(i, weight=1)
for i in range(6): root.grid_rowconfigure(i, weight=1)

root.mainloop()