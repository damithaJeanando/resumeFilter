import tkinter
from tkinter import *
from tkinter import filedialog

import pdfParser
import resumeTemplate

root = Tk()
root.title("Resume Parser")
root.geometry("1500x700")

text_var = tkinter.StringVar(root)
text_varc = tkinter.StringVar(root)

T = tkinter.Text(root, height=30, width=70)
T.place(x=200, y=500)
T.pack()

T1 = tkinter.Text(root, height=30, width=70)
T1.place(x=700, y=700)
T1.pack()

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    response = pdfParser.findFilePath(filename)
    text_var.set(response)
    T.insert(tkinter.END, text_var.get())
    print(text_var.get())


button = tkinter.Button(root, text='Upload CV', command=UploadAction).place(x=300, y=500, width=100)


def ProcessAction(event=None):
    processed_resume = resumeTemplate.result
    text_varc.set(processed_resume)
    T1.insert(tkinter.END, text_varc.get())
    print(text_varc.get())

button_process = tkinter.Button(root, text='Process', command=ProcessAction).place(x=300, y=600, width=100)


root.mainloop()