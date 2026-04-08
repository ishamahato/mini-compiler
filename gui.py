import tkinter as tk
from parser import parse

from intermediate_code import generate_TAC
from lexer import tokenize


def compile_code():
    output_text.delete("1.0", tk.END)
    expression = input_text.get("1.0", tk.END).strip()

    try:
        tokens = tokenize(expression)
        left, right = parse(tokens)
        tac, result = generate_TAC(right)

        for line in tac:
            output_text.insert(tk.END, line + "\n")

        output_text.insert(tk.END, f"{left} = {result}")

    except Exception as e:
        output_text.insert(tk.END, str(e))


# GUI Window
root = tk.Tk()
root.title("Mini Compiler")
root.geometry("500x400")

# Input Label
tk.Label(root, text="Enter Expression:", font=("Arial", 12)).pack()

# Input Box
input_text = tk.Text(root, height=3)
input_text.pack()

# Compile Button
tk.Button(root, text="Compile", command=compile_code).pack(pady=10)

# Output Label
tk.Label(root, text="Output:", font=("Arial", 12)).pack()

# Output Box
output_text = tk.Text(root, height=10)
output_text.pack()

# Run GUI
root.mainloop()
