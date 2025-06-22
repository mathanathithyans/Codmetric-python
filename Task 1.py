import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(symbol):
    entry.insert(tk.END, symbol)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        cmd = button_equal if symbol == '=' else lambda s=symbol: button_click(s)
        tk.Button(root, text=symbol, width=5, height=2, font=('Arial', 20), command=cmd).grid(row=i+1, column=j, padx=5, pady=5)

tk.Button(root, text="C", width=22, height=2, font=('Arial', 16), command=button_clear, bg="#f44336", fg="white").grid(row=5, column=0, columnspan=4, pady=10)
root.mainloop()
