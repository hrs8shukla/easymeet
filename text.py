import tkinter as tk

master = tk.Tk()
master.geometry('300x300')
tk.Label(master, text="Date").grid(row=0)

def show_entry_fields():
    print("Date: %s" % (e1.get()))
    e1.delete(0, tk.END)
def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)
e1 = tk.Entry(master)

e1.grid(row=0, column=1)
tk.Button(master,
          text='Select .sbv transcript',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master, text='Select .xls spreadsheet', command=show_entry_fields).grid(row=3,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)
master.mainloop()