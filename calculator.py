import tkinter as tk
def click(event): 
    current_text = expression_entry.get()
    expression_entry.delete(0, tk.END) 
    expression_entry.insert(tk.END, current_text + event.widget.cget("text")) 
 
def evaluate_expression(): 
    expression = expression_entry.get()
    result = str(eval(expression))
    expression_entry.delete(0, tk.END)
    expression_entry. insert (tk.END, result) 
 
def clear_expression(): 
    expression_entry.delete(0, tk.END) 
 
root = tk.Tk() 
root.title("Simple Calculator") 
 
expression_entry = tk.Entry(root, font=("Arial", 20), bd=8, 
relief=tk.SUNKEN, justify='right')
expression_entry.grid(row=0, column=0, columnspan=4)
buttons = [ 
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+' 
] 
 
for i, button_text in enumerate(buttons): 
    button = tk.Button(root, text=button_text, font= ("Arial", 18), bd=4)
    button.grid(row = (i // 4) + 1, column=i % 4, sticky="nsew")
    if button_text == "=": 
        button.config(command=evaluate_expression)
    elif button_text == "C": 
        button.config(command=clear_expression)
    else: 
        button.bind("<Button-1>", click) 
 
for i in range(4): 
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1) 
 
root.mainloop() 
