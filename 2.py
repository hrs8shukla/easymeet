from tkinter import *
from tkinter import filedialog
base = Tk()
# Create a canvas
base.geometry('600x600')
base.configure(bg='grey')
base.title("Attendence Marker")
# Function for opening the file
def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)
def text_opener():
   input = filedialog.askopenfile(initialdir="/")
   print(input)
   for i in input:
      print(i)

w = Label(base, text="Attendence marker using Meet transcript",pady=10,padx=10,bg='grey')
w.config(font=("Courier", 16))
w.pack()
# Button label
q = Label(base, text="Date",pady=20,bg='grey')
q.pack()
T = Text(base, height=2, width=30)
T.pack()

x = Button(base, text ='Select a .sbv/.txt transcript file', pady=10,padx=10,bg='grey',command = lambda:text_opener())
x.pack()
y = Button(base, text ='Select a .xls file',pady=20,bg='grey',command = lambda:file_opener())
y.pack()
z = Label(base, text="Developed by Harshit Shukla",pady=20,bg='grey')
z.pack()
mainloop()