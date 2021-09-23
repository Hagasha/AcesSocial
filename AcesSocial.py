from tkinter import *
from time import sleep
from tkinter import messagebox
 
class AcesSocial:
    def __init__(self):
        root = Tk()
        root.geometry('320x500+200+100')
        root.title('AcesSocial')
        root.resizable(True,True)
        root["bg"] = '#f7f7f7'
        root.iconbitmap("pessoas.ico")
        
        logo = PhotoImage(file = "LogoAcesSocial.png")
 
        fr1 = Frame(root, bg= "green")
        fr1.place(relx = 0.20, rely = 0.09, relwidth = 0.65, relheight = 0.30)
 
        img1 = Label (fr1, image = logo, bg = "#f7f7f7", activebackground = "green")
        img1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        txt1 = Label(root,bg='#f7f7f7', text="Lei de garantias de direitos na Assistência Social", font='arial, 11', height=1, width=5, relief='flat' )
        txt1.place(relx= 0, rely=0.38, relwidth= 1, relheight= 0.10)
 
        btnInicio = Button(root, bg='#3ec4cd', text='Ir para o aplicativo', font='bold, 10', height=1, width=5, relief='flat')
        btnInicio.place(relx=0.13, rely=0.78, relwidth = 0.75, relheight = 0.10)
 
        root.mainloop()
        
        
AcesSocial()
