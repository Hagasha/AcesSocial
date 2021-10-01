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

        self.btnSobre = Button (self.telaOpcoes, text="Sobre", bg = '#3ec4cd', font = 'bold, 15', relief='raised', command=self.msgsobre)
        self.btnSobre = Button (self.telaOpcoes, text="Sobre", bg = '#3ec4cd', font = 'bold, 15', relief='flat', command=self.msgsobre)
        self.btnSobre.place(relx=0.10, rely=0.18, relwidth = 0.80, relheight = 0.10)
        self.btnSair = Button (self.telaOpcoes, text="Sair", bg = '#3ec4cd', font = 'bold, 15', relief='raised', command=self.telaOpcoes.quit)
        self.btnSair = Button (self.telaOpcoes, text="Sair", bg = '#3ec4cd', font = 'bold, 15', relief='flat', command=self.telaOpcoes.quit)
        self.btnSair.place(relx=0.10, rely=0.38, relwidth = 0.80, relheight = 0.10)
        self.btnVoltarPrinc = Button(self.telaOpcoes, image = self.imgVoltar, bg ='white', font='bold, 10', command = self.JanelaMenu)
        self.btnVoltarPrinc = Button(self.telaOpcoes, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

# Criando as telas com as informações de cada serviço social

    def Pestalozzi(self):
        self.ct = Toplevel()
        self.ct.geometry('320x500+200+100')
        self.ct.resizable(True, True)
        self.ct["bg"] = '#ffffff'
        self.ct.iconbitmap("pessoas.ico")

        self.txt2 = Label(self.ct,bg='#ffffff', text='''Sociedade Pestalozzi Resende 
Endereço: R. Cel. Rocha Santos,
656 - Jardim Brasilia 2
Resende - RJ, 27515-000, 
Telefone: (24) 3354-1460.''',
        font='arial, ', height=1, width=5, relief='flat')
        self.txt2.place(relx=0, rely=0.38, relwidth= 1, relheight= 0.18)
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

    
    def crasParaiso(self):
        self.telaParaiso = Toplevel()
        self.telaParaiso.geometry('320x500+200+100')
        self.telaParaiso.resizable(True, True)
        self.telaParaiso["bg"] = '#ffffff'
        self.telaParaiso.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtParaiso = Label(self.telaParaiso,bg='#ffffff', text='''CRAS Paraíso
Endereço: 
Avenida Coronel Abílio Godoy,
127 - Paraíso, 
Resende - RJ, 
Telefone: (24) 3381-2074''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtParaiso.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaParaiso, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    
    def crasToyota(self):
        self.telaToyota = Toplevel()
        self.telaToyota.geometry('320x500+200+100')
        self.telaToyota.resizable(True, True)
        self.telaToyota["bg"] = '#ffffff'
        self.telaToyota.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtToyota = Label(self.telaToyota,bg='#ffffff', text='''CRAS Toyota
Endereço: 
Av. Projetada, 
s/n° - Toyota II
Resende - RJ, 
Telefone: (24) 3360-5098''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtToyota.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaToyota, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def crasItapuca(self):
        self.telaItapuca = Toplevel()
        self.telaItapuca.geometry('320x500+200+100')
        self.telaItapuca.resizable(True, True)
        self.telaItapuca["bg"] = '#ffffff'
        self.telaItapuca.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtItapuca = Label(self.telaItapuca,bg='#ffffff', text='''CRAS Itapuca
Endereço: 
R. Euzebio Manoel da Glória, 
s/n° - Itapuca
Resende - RJ, 
Telefone: (24) 3360-5239''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtItapuca.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaItapuca, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)




# Crianddo primeira página com os serviços sociais

    def JanelaMenu(self):
        self.jm = Tk()
        self.jm.geometry('320x500+200+100')
        self.jm.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm["bg"] = '#ffffff'
        self.jm.iconbitmap("pessoas.ico")
        self.imgPesquisa = PhotoImage (file = "lupa.png")
        self.imgConfig = PhotoImage(file = "imgConfig.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")


        #self.txt3 = Label (self.jm, bg='black', text="Procure por um serviço social aqui!", font='arial, 11', height=1, width=5, relief='flat' )
        #self.txt1.place(relx= 0.06, rely=0.03, relwidth= 0.08, relheight= 0.20)
        self.txt3 = Label(self.jm,bg='white', text='''Encontre informações de 
serviços sociais aqui!
Página 1''', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.01, rely=0.02, relwidth= 0.80, relheight= 0.10)


        self.btnConfig = Button (self.jm, text = "Opções", bg ='#3ec4cd', font='bold, 10', relief='flat', command = self.barraOpcoes)
        self.btnConfig.place(relx=0.80, rely=0.03, relheight=0.06, relwidth=0.15)


        self.btn1 = Button(self.jm, bg='#7ca4da', text='CRAS Toyota', font='bold, 10', height=1, width=5, relief='flat', command=self.crasToyota)
        self.btn1.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn2 = Button(self.jm, bg='#7ca4da', text='CRAS Paraíso', font='bold, 10', height=1, width=5, relief='flat', command=self.crasParaiso)
        self.btn2.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn3 = Button(self.jm, bg='#7ca4da', text='Prefeitura de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Prefeitura)
        self.btn3.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn4 = Button(self.jm, bg='#7ca4da', text='Fórum de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Forum)
        self.btn4.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn5 = Button(self.jm, bg='#7ca4da', text='Asilo Nicolino Gulhot', font='bold, 10', height=1, width=5, relief='flat', command=self.Asilo)
        self.btn5.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn6 = Button(self.jm, bg='#7ca4da', text='Pestalozzi', font='bold, 10', height=1, width=5, relief='flat', command=self.Pestalozzi)
        self.btn6.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm, text = "Avançar", bg ='#3ec4cd', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnPagina1.place(relx=0.75, rely=0.90, relwidth = 0.20, relheight = 0.10)

# Criando segunda pagina de serviços

    def Menu2(self):
        self.jm2 = Tk()
        self.jm2.geometry('320x500+200+100')
        self.jm2.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm2["bg"] = '#ffffff'
        self.jm2.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")

        self.btn6 = Button(self.jm2, bg='#7ca4da', text='CRAS Itapuca', font='bold, 10', height=1, width=5, relief='flat', command=self.crasItapuca)
        self.btn6.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn7 = Button(self.jm2, bg='#7ca4da', text='CRAS Paraíso', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn7.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn8 = Button(self.jm2, bg='#7ca4da', text='Prefeitura de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn8.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn9 = Button(self.jm2, bg='#7ca4da', text='Fórum de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn9.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn10 = Button(self.jm2, bg='#7ca4da', text='Asilo Nicolino Gulhot', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn10.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn11= Button(self.jm2, bg='#7ca4da', text='Pestalozzi', font='bold, 10', height=1, width=5, relief='flat', command=self.semcomando)
        self.btn11.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)








AcesSocial()
