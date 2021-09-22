from tkinter import *
from time import sleep
from tkinter import messagebox
 
class AcesSocial:
    def __init__(self):
        root = Tk()
        root.geometry('320x500+200+100')
        root.title('AcesSocial')
        logo = PhotoImage(file = "LogoAcesSocial.png")
 
        fr1 = Frame(root, bg= "green")
        fr1.place(relx = 0.20, rely = 0.20, relwidth = 0.65, relheight = 0.30)
 
        img1 = Label (fr1, image = logo, bg = "gray", activebackground = "green")
        img1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
 
        btnInicio = Button(root, bg='#3ec4cd', text='Ir para o aplicativo', font='bold, 10', height=1, width=5, relief='flat')
        btnInicio.place(relx=0.35, rely=0.60, relwidth = 0.35, relheight = 0.10)
 
        root.mainloop()


 
AcesSocial()