import tkinter as tk
from tkinter import filedialog
window = tk.Tk()
label = tk.Label(text="Date")
entry = tk.Entry()
label.pack()
entry.pack()
name = entry.get()
print(name)
window.mainloop()