from tkinter import *
from tkinter import filedialog as fd
import openpyxl

def txtfile_opener():
    global txt
    txt = fd.askopenfilename()
def xlsfile_opener():
    global file
    file = fd.askopenfilename()
def attendence():
    book = openpyxl.load_workbook(file)
    sheet = book.active
    a = sheet['A1']
    print(a.value)
    book.save(file)
base = Tk()
base.geometry('150x150')
txt=""
file=""
button1 = Button(base, text ='Select a .txt/.sbv file', command = lambda:txtfile_opener())
button1.pack()
button2 = Button(base, text ='Select a .xls file', command = lambda:xlsfile_opener())
button2.pack()
button3 = Button(base,text='Submit',command =attendence).pack()
mainloop()