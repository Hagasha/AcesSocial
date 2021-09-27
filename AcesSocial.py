from tkinter import *
from time import sleep
from tkinter import messagebox

 
class AcesSocial:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('320x500+200+100')
        self.root.title('AcesSocial')
        self.root.resizable(False,False)
        self.root["bg"] = '#f7f7f7'
        self.root.iconbitmap("pessoas.ico")
        
        self.logo = PhotoImage(file = "LogoAcesSocial.png")
 
        self.fr1 = Frame(self.root, bg= "green")
        self.fr1.place(relx = 0.20, rely = 0.09, relwidth = 0.65, relheight = 0.30)
 
        self.img1 = Label (self.fr1, image = self.logo, bg = "#f7f7f7", activebackground = "green")
        self.img1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.txt1 = Label(self.root,bg='#f7f7f7', text="Lei de garantias de direitos na Assistência Social", font='arial, 11', height=1, width=5, relief='flat' )
        self.txt1.place(relx= 0, rely=0.38, relwidth= 1, relheight= 0.10)
 
        self.btnInicio = Button(self.root, bg='#3ec4cd', text='Ir para o aplicativo', font='bold, 10', height=1, width=5, relief='flat', command=self.JanelaMenu)
        self.btnInicio.place(relx=0.13, rely=0.78, relwidth = 0.75, relheight = 0.10)
 
        self.root.mainloop()

    def semcomando(self):
        print('')


    def JanelaMenu(self):
        self.root.withdraw()
        self.jm = Tk()
        self.jm.geometry('320x500+200+100')
        self.jm.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm["bg"] = '#ffffff'
        self.jm.iconbitmap("pessoas.ico")
        

        self.barramenu = Menu(self.jm)
        self.contatos = Menu(self.barramenu, tearoff=0)
        self.contatos.add_command(label='Sobre', command=self.semcomando)
        self.contatos.add_command(label='Sair', command= self.jm.quit)
        self.barramenu.add_cascade(label="Opções", menu=self.contatos)
        

        self.pesquisar = Entry(self.jm, font= "Bold, 16")
        self.pesquisar.place(relx=0.10, rely=0.02, relwidth = 0.75, relheight = 0.08)
        
        self.btn1 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn1.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn2 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn2.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn3 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn3.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn4 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn4.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn5 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn5.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)
        self.btn6 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn6.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)

        self.jm.config(menu=self.barramenu)

  
AcesSocial()
