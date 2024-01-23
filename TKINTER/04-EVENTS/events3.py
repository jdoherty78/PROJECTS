import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("350x600")
root.title("Event GUI app")
root.iconbitmap("python_icon.ico")
root.config(bg = "lightgreen")

def clear_text():
    return

text = tk.Text(root, width = 40, height = 20)
text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
text.config(bg="pink", borderwidth=5)

btn = tk.Button(root, text="Clear", command=clear_text)
btn.config(bg="orange", fg="black", padx=10, pady=10, borderwidth=5)
btn.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


# run ze application
root.mainloop()