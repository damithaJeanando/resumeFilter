import tkinter as tk
from tkinter import *
from tkinter import filedialog

import pdfParser
import resumeTemplate

root = Tk()
root.title("Resume Parser")
root.geometry("700x700")



text_resume = tk.StringVar(root)
text_name = tk.StringVar(root)
text_title = tk.StringVar(root)
text_address = tk.StringVar(root)
text_phone = tk.StringVar(root)
text_email = tk.StringVar(root)
text_skills = tk.StringVar(root)
text_experience = tk.StringVar(root)
text_education = tk.StringVar(root)



T = Text(root, height=30, width=70)
T.pack()



def UploadAction(event=None):

    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    response = pdfParser.findFilePath(filename)
    text_resume.set(response)
    T.insert(tk.END, text_resume.get())



button = tk.Button(root, text='Upload CV', command=UploadAction).place(x=300, y=500, width=100)


# def ProcessAction(event=None):
#     processed_resume = pdfParser.extractData()
#     text_varc.set(processed_resume)
#     T1.insert(tk.END, text_varc.get())
#     print(text_varc.get())

def create_window():

    window = tk.Toplevel(root)
    sample_resume_lbl = tk.Label(window, text='Sample Resume Template', font='Helvetica 20 bold')

    name_lbl = tk.Label(window, text='Name : ', font='Helvetica 14')
    title_lbl = tk.Label(window, text='Title : ', font='Helvetica 14')
    address_lbl = tk.Label(window, text='Address : ', font='Helvetica 14')
    phone_lbl = tk.Label(window, text='Phone : ', font='Helvetica 14')
    email_lbl = tk.Label(window, text='Email : ', font='Helvetica 14')
    skills_lbl = tk.Label(window, text='Skills : ', font='Helvetica 14')
    experience_lbl = tk.Label(window, text='Experience : ', font='Helvetica 14')
    education_lbl = tk.Label(window, text='Education : ', font='Helvetica 14')



    Name = Text(window, height=2, width=70)
    Title = Text(window, height=2, width=70)
    Address = Text(window, height=3, width=70)
    Phone = Text(window, height=2, width=70)
    Email = Text(window, height=2, width=70)
    Skills = Text(window, height=2, width=70)
    Experience = Text(window, height=20, width=70)
    Education = Text(window, height=10, width=70)

    processed_resume_name = pdfParser.return_name()
    processed_resume_title = pdfParser.return_title()
    processed_resume_address = pdfParser.return_address()
    processed_resume_phone = pdfParser.return_phoneNumber()
    processed_resume_email = pdfParser.return_email()
    processed_resume_skills = pdfParser.return_skills()
    processed_resume_experience = pdfParser.return_experience()
    processed_resume_education = pdfParser.return_education()


    text_name.set(processed_resume_name)
    text_title.set(processed_resume_title)
    text_address.set(processed_resume_address)
    text_phone.set(processed_resume_phone)
    text_email.set(processed_resume_email)
    text_skills.set(processed_resume_skills)
    text_experience.set(processed_resume_experience)
    text_education.set(processed_resume_education)

    Name.insert(tk.END, text_name.get())
    Title.insert(tk.END, text_title.get())
    Address.insert(tk.END, text_address.get())
    Phone.insert(tk.END, text_phone.get())
    Email.insert(tk.END, text_email.get())
    Skills.insert(tk.END, text_skills.get())
    Experience.insert(tk.END, text_experience.get())
    Education.insert(tk.END, text_education.get())

    sample_resume_lbl.grid(row=0, column=1, sticky=N)
    name_lbl.grid(row=1, sticky=W)
    title_lbl.grid(row=2, sticky=W)
    address_lbl.grid(row=3, sticky=W)
    phone_lbl.grid(row=4, sticky=W)
    email_lbl.grid(row=5, sticky=W)
    skills_lbl.grid(row=6, sticky=W)
    experience_lbl.grid(row=7, sticky=W)
    education_lbl.grid(row=8, sticky=W)


    Name.grid(row=1, column=1)
    Title.grid(row=2, column=1)
    Address.grid(row=3, column=1)
    Phone.grid(row=4, column=1)
    Email.grid(row=5, column=1)
    Skills.grid(row=6, column=1)
    Experience.grid(row=7, column=1)
    Education.grid(row=8, column=1)

button_generate = tk.Button(root, text='Generate Sample Resume', command=create_window).place(x=250, y=600, width=200)


root.mainloop()