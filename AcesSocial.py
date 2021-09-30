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

    def msgsobre(self):
        messagebox.showinfo("AcesSocial - Sobre", "Esse projeto foi feito para ajudar as pessoas em vulnerabilidade social." )

    

    def barraOpcoes(self):
        self.telaOpcoes = Toplevel()
        self.telaOpcoes.geometry('320x500+200+100')
        self.telaOpcoes.resizable(True, True)
        self.telaOpcoes["bg"] = '#ffffff'
        self.telaOpcoes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.btnSobre = Button (self.telaOpcoes, text="Sobre", bg = '#3ec4cd', font = 'bold, 15', relief='flat', command=self.msgsobre)
        self.btnSobre.place(relx=0.10, rely=0.18, relwidth = 0.80, relheight = 0.10)
        self.btnSair = Button (self.telaOpcoes, text="Sair", bg = '#3ec4cd', font = 'bold, 15', relief='flat', command=self.telaOpcoes.quit)
        self.btnSair.place(relx=0.10, rely=0.38, relwidth = 0.80, relheight = 0.10)
        self.btnVoltarPrinc = Button(self.telaOpcoes, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


    def Pestalozzi(self):
        self.ptlz = Toplevel()
        self.ptlz.geometry('320x500+200+100')
        self.ptlz.resizable(True, True)
        self.ptlz["bg"] = '#ffffff'
        self.ptlz.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")


        self.txtPtlz = Label(self.ptlz,bg='#ffffff', text='''Sociedade Pestalozzi Resende 
Endereço: R. Cel. Rocha Santos, 
num: 656 - Jardim Brasilia 2,
Resende - RJ, 27515-000,
Telefone: (24) 3354-1460.''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtPtlz.place(relx=0.02, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.ptlz, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def Asilo(self):
        self.telaAsilo = Toplevel()
        self.telaAsilo.geometry('320x500+200+100')
        self.telaAsilo.resizable(True, True)
        self.telaAsilo["bg"] = '#ffffff'
        self.telaAsilo.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtAsilo = Label(self.telaAsilo,bg='#ffffff', text='''ILPI Asilo Nicolino Gulhot
Endereço: Av. Augusto de Carvalho, 
1080 - Parque Ipiranga,
Resende - RJ, 27516-240, 
Telefone: (24) 3354-6264''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtAsilo.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaAsilo, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


    def Forum(self):
        self.telaForum = Toplevel()
        self.telaForum.geometry('320x500+200+100')
        self.telaForum.resizable(True, True)
        self.telaForum["bg"] = '#ffffff'
        self.telaForum.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtForum = Label(self.telaForum,bg='#ffffff', text='''Fórum de Resende
Endereço: 
Av. Rita Maria Ferreira da Rocha, 
500 - Jardim Jalisco, 
Resende - RJ, 27510-060, 
Telefone: (24) 3358-9600''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtForum.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaForum, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


    def Prefeitura(self):
        self.telaPref = Toplevel()
        self.telaPref.geometry('320x500+200+100')
        self.telaPref.resizable(True, True)
        self.telaPref["bg"] = '#ffffff'
        self.telaPref.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtPref = Label(self.telaPref,bg='#ffffff', text='''Prefeitura Municipal de Resende
Endereço: 
R. Augusto Xavier de Lima, 
251 - Jardim Jalisco, 
Resende - RJ, 27510-070, 
Telefone: (24) 3354-6000''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtPref.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaPref, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)



        

    def JanelaMenu(self):
        self.root.withdraw()
        self.jm = Tk()
        self.jm.geometry('320x500+200+100')
        self.jm.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm["bg"] = '#ffffff'
        self.jm.iconbitmap("pessoas.ico")
        self.imgPesquisa = PhotoImage (file = "lupa.png")
        self.imgConfig = PhotoImage(file = "imgConfig.png")


        self.txt3 = Label(self.jm,bg='white', text="Pesquise um serviço social aqui!", font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.01, rely=0.08, relwidth= 0.80, relheight= 0.06)
        

        self.btnConfig = Button (self.jm, text = "Opções", bg ='#3ec4cd', font='bold, 10', relief='flat', command = self.barraOpcoes)
        self.btnConfig.place(relx=0.80, rely=0.03, relheight=0.06, relwidth=0.15)
        
         
        self.pesquisar = Entry(self.jm, font= "Bold, 16")
        self.pesquisar.place(relx=0.02, rely=0.13, relwidth = 0.70, relheight = 0.08)
        
        self.btn1 = Button(self.jm, bg='#7ca4da', text='exemplo', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn1.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn2 = Button(self.jm, bg='#7ca4da', text='Prefeitura de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Prefeitura)
        self.btn2.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn3 = Button(self.jm, bg='#7ca4da', text='Fórum de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Forum)
        self.btn3.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn4 = Button(self.jm, bg='#7ca4da', text='Asilo Nicolino Gulhot', font='bold, 10', height=1, width=5, relief='flat', command=self.Asilo)
        self.btn4.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn5 = Button(self.jm, bg='#7ca4da', text='Pestalozzi', font='bold, 10', height=1, width=5, relief='flat', command=self.Pestalozzi)
        self.btn5.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPesquisa = Button(self.jm, text = 'Pesquisar', font = 'bold, 10', relief='flat', bg='#3ec4cd', command=self.semcomando)
        self.btnPesquisa.place(relx=0.75, rely=0.13, relheight=0.08, relwidth=0.20)

  
AcesSocial()
