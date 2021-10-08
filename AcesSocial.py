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
        self.txt1 = Label(self.root,bg='#f7f7f7', text='''Lei de garantias 
de direitos na Assistência Social!''', font='arial, 13', height=1, width=5, relief='flat' )
        self.txt1.place(relx= 0, rely=0.38, relwidth= 1, relheight= 0.10)
 
        self.btnInicio = Button(self.root, bg='#836FFF', fg= 'white', text='Ir para o aplicativo', font='Arial, 15', height=1, width=5, relief='flat', command=self.JanelaMenu)
        self.btnInicio.place(relx=0.13, rely=0.78, relwidth = 0.80, relheight = 0.10)
 
        self.root.mainloop()
    def semcomando(self):
        print('')
    def msgsobre(self):
        messagebox.showinfo("AcesSocial - Sobre", "Esse projeto foi feito para ajudar as pessoas em vulnerabilidade social." )
    
    def barraOpcoes(self):
        self.telaOpcoes = Toplevel()
        self.telaOpcoes.geometry('320x500+200+100')
        self.telaOpcoes.resizable(True, True)
        self.telaOpcoes["bg"] = '#836FFF'
        self.telaOpcoes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")
        self.btnSobre = Button (self.telaOpcoes, text="Sobre", bg = '#E6E6FA', fg = "black", font = 'bold, 15', relief='flat', command=self.msgsobre)
        self.btnSobre.place(relx=0.10, rely=0.18, relwidth = 0.80, relheight = 0.10)
        self.btnSair = Button (self.telaOpcoes, text="Sair", bg = '#E6E6FA', fg = "black", font = 'bold, 15', relief='flat', command=self.telaOpcoes.quit)
        self.btnSair.place(relx=0.10, rely=0.38, relwidth = 0.80, relheight = 0.10)
        self.btnVoltarPrinc = Button(self.telaOpcoes, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

# Criando as telas com as informações de cada serviço social

    def Pestalozzi(self):
        self.ptlz = Toplevel()
        self.ptlz.geometry('320x500+200+100')
        self.ptlz.resizable(True, True)
        self.ptlz["bg"] = "#836FFF"
        self.ptlz.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.quadro = Label(self.ptlz, text=''' Sociedade Pestalozzi Resende 
Endereço: R. Cel. Rocha Santos,
656 - Jardim Brasilia 2
Resende - RJ, 27515-000, 
Telefone: (24) 3354-1460.''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.quadro.place(relx=0.00, rely=0.25, relheight=0.50, relwidth=1)

        self.linhaSuperior = Label(self.ptlz, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.ptlz, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def Asilo(self):
        self.telaAsilo = Toplevel()
        self.telaAsilo.geometry('320x500+200+100')
        self.telaAsilo.resizable(True, True)
        self.telaAsilo["bg"] = '#836FFF'
        self.telaAsilo.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtAsilo = Label(self.telaAsilo, text='''ILPI Asilo Nicolino Gulhot
Endereço: Av. Augusto de Carvalho, 
1080 - Parque Ipiranga,
Resende - RJ, 27516-240, 
Telefone: (24) 3354-6264''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtAsilo.place(relx=0.00, rely=0.25, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaAsilo, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaAsilo, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)


    def Forum(self):
        self.telaForum = Toplevel()
        self.telaForum.geometry('320x500+200+100')
        self.telaForum.resizable(True, True)
        self.telaForum["bg"] = '#836FFF'
        self.telaForum.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtForum = Label(self.telaForum, text='''Fórum de Resende
Endereço: 
Av. Rita Maria Ferreira da Rocha, 
500 - Jardim Jalisco, 
Resende - RJ, 27510-060, 
Telefone: (24) 3358-9600''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtForum.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaForum, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaForum, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)


    def Prefeitura(self):
        self.telaPref = Toplevel()
        self.telaPref.geometry('320x500+200+100')
        self.telaPref.resizable(True, True)
        self.telaPref["bg"] = '#836FFF'
        self.telaPref.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtPref = Label(self.telaPref, text='''Prefeitura Municipal de Resende
Endereço: 
R. Augusto Xavier de Lima, 
251 - Jardim Jalisco, 
Resende - RJ, 27510-070, 
Telefone: (24) 3354-6000''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtPref.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaPref, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaPref, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    
    def crasParaiso(self):
        self.telaParaiso = Toplevel()
        self.telaParaiso.geometry('320x500+200+100')
        self.telaParaiso.resizable(True, True)
        self.telaParaiso["bg"] = '#836FFF'
        self.telaParaiso.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtParaiso = Label(self.telaParaiso, text='''CRAS Paraíso
Endereço: 
Avenida Coronel Abílio Godoy,
127 - Paraíso, 
Resende - RJ, 
Telefone: (24) 3381-2074''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtParaiso.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaParaiso, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaParaiso, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    
    def crasToyota(self):
        self.telaToyota = Toplevel()
        self.telaToyota.geometry('320x500+200+100')
        self.telaToyota.resizable(True, True)
        self.telaToyota["bg"] = '#836FFF'
        self.telaToyota.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtToyota = Label(self.telaToyota, text='''CRAS Toyota
Endereço: 
Av. Projetada, 
s/n° - Toyota II
Resende - RJ, 
Telefone: (24) 3360-5098''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtToyota.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaToyota, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaToyota, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def crasItapuca(self):
        self.jm2.wm_withdraw()
        self.telaItapuca = Toplevel()
        self.telaItapuca.geometry('320x500+200+100')
        self.telaItapuca.resizable(True, True)
        self.telaItapuca["bg"] = '#836FFF'
        self.telaItapuca.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtItapuca = Label(self.telaItapuca, text='''CRAS Itapuca
Endereço: 
R. Euzebio Manoel da Glória, 
s/n° - Itapuca
Resende - RJ, 
Telefone: (24) 3360-5239''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtItapuca.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaItapuca, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaItapuca, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def crasItinerante(self):
        self.jm2.wm_withdraw()
        self.telaItinerante = Toplevel()
        self.telaItinerante.geometry('320x500+200+100')
        self.telaItinerante.resizable(True, True)
        self.telaItinerante["bg"] = '#836FFF'
        self.telaItinerante.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtItinerante = Label(self.telaItinerante, text='''CRAS Itinerante
Endereço: 
Rua do Rosário
n° 45 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9510''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtItinerante.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaItinerante, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaItinerante, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)
        
    def nossaCasa(self):
        self.jm2.wm_withdraw()
        self.telanossaCasa = Toplevel()
        self.telanossaCasa.geometry('320x500+200+100')
        self.telanossaCasa.resizable(True, True)
        self.telanossaCasa["bg"] = '#836FFF'
        self.telanossaCasa.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtnossaCasa = Label(self.telanossaCasa, text='''Abrigo nossa Casa
Endereço: 
Av.Rita Maria Ferreira da Rocha
n° 1301 - Jardim Jalisco
Resende - RJ, 
Telefone: (24) 3360-9888''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtnossaCasa.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telanossaCasa, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telanossaCasa, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)
    
    def crasLavapes(self):
        self.jm2.wm_withdraw()
        self.telaLavapes = Toplevel()
        self.telaLavapes.geometry('320x500+200+100')
        self.telaLavapes.resizable(True, True)
        self.telaLavapes["bg"] = '#836FFF'
        self.telaLavapes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtLavapes = Label(self.telaLavapes, text='''CRAS Lavapés
Endereço: 
Rua Eduardo Cotrim
n° 36 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9887''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtLavapes.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaLavapes, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telaLavapes, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def crasJDEsperanca(self):
        self.jm2.wm_withdraw()
        self.telajdEsperanca = Toplevel()
        self.telajdEsperanca.geometry('320x500+200+100')
        self.telajdEsperanca.resizable(True, True)
        self.telajdEsperanca["bg"] = '#836FFF'
        self.telajdEsperanca.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtjdEsperanca = Label(self.telajdEsperanca, text='''CRAS Jardim Esperança
Endereço: 
Rua Frei Tito
n° 27 - Fazenda da Barra I
Resende - RJ, 
Telefone: (24) 3354-4676''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtjdEsperanca.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telajdEsperanca, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPrinc = Button(self.telajdEsperanca, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)


    def cciToboga(self):
        self.jm2.wm_withdraw()
        self.telacciToboga = Toplevel()
        self.telacciToboga.geometry('320x500+200+100')
        self.telacciToboga.resizable(True, True)
        self.telacciToboga["bg"] = '#836FFF'
        self.telacciToboga.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtcciToboga = Label(self.telacciToboga, text='''CCI Tobogã
Endereço: 
Rua Governador Portela
s/n° (Parque Tobogã) - Manejo.
Resende - RJ, 
Telefone: (24) 3360-0685''',
        bg='#836FFF', fg='white',font='bold, 10')

        self.linhaSuperior = Label(self.telacciToboga, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.txtcciToboga.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)
        self.btnVoltarPrinc = Button(self.telacciToboga, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def cciAlegria(self):
        self.jm3.wm_withdraw()
        self.telacciAlegria = Toplevel()
        self.telacciAlegria.geometry('320x500+200+100')
        self.telacciAlegria.resizable(True, True)
        self.telacciAlegria["bg"] = '#836FFF'
        self.telacciAlegria.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtcciAlegria = Label(self.telacciAlegria, text='''CCI Cidade Alegria
Endereço: 
Rua das Samambaias, 
s/n - Cidade Alegria.
Resende - RJ, 
Telefone: (24) 3359-5557''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtcciAlegria.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telacciAlegria, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telacciAlegria, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def cciParaiso(self):
        self.jm3.wm_withdraw()
        self.telacciParaiso = Toplevel()
        self.telacciParaiso.geometry('320x500+200+100')
        self.telacciParaiso.resizable(True, True)
        self.telacciParaiso["bg"] = '#836FFF'
        self.telacciParaiso.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtcciParaiso = Label(self.telacciParaiso, text='''CCI Paraíso
Endereço: 
Rua Dom Bosco, 
s/n (Parque Paraíso) - Paraíso.
Resende - RJ, 
Telefone: (24) 3360-3707''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtcciParaiso.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telacciParaiso, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telacciParaiso, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def FmlAcolhedora(self):
        self.jm3.wm_withdraw()
        self.telaFmlAcolhedora = Toplevel()
        self.telaFmlAcolhedora.geometry('320x500+200+100')
        self.telaFmlAcolhedora.resizable(True, True)
        self.telaFmlAcolhedora["bg"] = '#836FFF'
        self.telaFmlAcolhedora.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtFmlAcolhedora = Label(self.telaFmlAcolhedora, text='''Programa Família Acolhedora
Endereço: 
Rua Pandiá Calógeras, 
n° 157 - Jardim Jalisco
Resende - RJ, 
Telefone: (24) 3381-6174''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtFmlAcolhedora.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaFmlAcolhedora, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaFmlAcolhedora, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def Creas(self):
        self.jm3.wm_withdraw()
        self.telaCreas = Toplevel()
        self.telaCreas.geometry('320x500+200+100')
        self.telaCreas.resizable(True, True)
        self.telaCreas["bg"] = '#836FFF'
        self.telaCreas.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtCreas = Label(self.telaCreas, text='''CREAS
Endereço: 
Rua Natanael Galvão, 
n° 48 - Jardim Tropical
Resende - RJ, 
Telefone: (24) 3360-9775''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtCreas.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaCreas, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaCreas, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def Pop(self):
        self.jm3.wm_withdraw()
        self.telaPop = Toplevel()
        self.telaPop.geometry('320x500+200+100')
        self.telaPop.resizable(True, True)
        self.telaPop["bg"] = '#836FFF'
        self.telaPop.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtPop = Label(self.telaPop, text='''Centro POP (Centro de
referência especializado para 
a população em situação de rua)
Endereço: 
Rua do Rosário, n° 230 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9739''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtPop.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaPop, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaPop, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def Seas(self):
        self.jm3.wm_withdraw()
        self.telaSeas = Toplevel()
        self.telaSeas.geometry('320x500+200+100')
        self.telaSeas.resizable(True, True)
        self.telaSeas["bg"] = '#836FFF'
        self.telaSeas.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtSeas = Label(self.telaSeas, text='''SEAS
Endereço: 
Rua Luis Rocha Miranda, 
n° 44 - Centro
Resende - RJ, 
Telefone: (24) 3360-9939''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtSeas.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaSeas, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaSeas, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def BolsaFml(self):
        self.jm4.wm_withdraw()
        self.telaBolsaFml = Toplevel()
        self.telaBolsaFml.geometry('320x500+200+100')
        self.telaBolsaFml.resizable(True, True)
        self.telaBolsaFml["bg"] = '#836FFF'
        self.telaBolsaFml.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtBolsaFml = Label(self.telaBolsaFml, text='''DIRETORIA DE CAD. ÚNICO
E PROGRAMA BOLSA FAMÍLIA
Endereço: 
Rua Luis Rocha Miranda, 
n° 44 - Centro
Resende - RJ, 
Telefone: (24) 3354-1458
cadastrounico.resende@hotmail.com''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtBolsaFml.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaBolsaFml, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaBolsaFml, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def IncProdutiva(self):
        self.jm4.wm_withdraw()
        self.telaInc = Toplevel()
        self.telaInc.geometry('320x500+200+100')
        self.telaInc.resizable(True, True)
        self.telaInc["bg"] = '#836FFF'
        self.telaInc.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtInc = Label(self.telaInc, text='''Inclusão Produtiva
Endereço: 
Estrada Resende-Riachuelo, 
s/n, Morada da Colina
Resende - RJ, 
Telefone: (24) 3355 8693''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtInc.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaInc, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaInc, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def PolPessoasDeficientes(self):
        self.jm4.wm_withdraw()
        self.telaPolDeficiemtes = Toplevel()
        self.telaPolDeficiemtes.geometry('320x500+200+100')
        self.telaPolDeficiemtes.resizable(True, True)
        self.telaPolDeficiemtes["bg"] = '#836FFF'
        self.telaPolDeficiemtes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtPolDef = Label(self.telaPolDeficiemtes, text='''Coordenadoria de Políticas 
para as Pessoas com Deficiência
Endereço: 
Av. Riachuelo, 
n° 232 - Nova Liberdade
Resende - RJ, 
Telefone: (24) 3381-4297
cpd.resenderj@bol.com.br''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtPolDef.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaPolDeficiemtes, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaPolDeficiemtes, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def ConselhosMunicipais(self):
        self.jm4.wm_withdraw()
        self.telaConsMun = Toplevel()
        self.telaConsMun.geometry('320x500+200+100')
        self.telaConsMun.resizable(True, True)
        self.telaConsMun["bg"] = '#836FFF'
        self.telaConsMun.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtConsMun = Label(self.telaConsMun, text='''Casa dos Conselhos Municipais
Endereço: 
Rua do Rosário, 
nº 45 - Lavapés
Resende - RJ, 
Telefone: (24) 3381 - 8674 / (24) 3354 - 6365
casadosconselhosresende@gmail.com''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtConsMun.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaConsMun, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaConsMun, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)

    def Niam(self):
        self.jm4.wm_withdraw()
        self.telaNiam = Toplevel()
        self.telaNiam.geometry('320x500+200+100')
        self.telaNiam.resizable(True, True)
        self.telaNiam["bg"] = '#836FFF'
        self.telaNiam.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")

        self.txtNiam = Label(self.telaNiam, text='''NIAM - Núcleo Integrado 
de Atendimento à Mulher
Endereço: 
Rua Macedo de Miranda, 
nº 81, bairro Jardim Jalisco I
Resende - RJ, 
Telefone: (24) 3360-9824
niamresende@yahoo.com.br''',
        bg='#836FFF', fg='white',font='bold, 10')
        self.txtNiam.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.50)

        self.linhaSuperior = Label(self.telaNiam, bg='black')
        self.linhaSuperior.place(relx=0.0, rely=0.1, relheight=0.0, relwidth=1)

        self.btnVoltarPag3 = Button(self.telaNiam, text = "< Voltar", bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.02, relheight=0.08, relwidth=0.20)




# Crianddo primeira página com os serviços sociais

    def JanelaMenu(self):
        self.root.withdraw()
        self.jm = Tk()
        self.jm.geometry('320x500+200+100')
        self.jm.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm["bg"] = '#836FFF'
        self.jm.iconbitmap("pessoas.ico")
        self.imgPesquisa = PhotoImage (file = "lupa.png")
        self.imgConfig = PhotoImage(file = "imgConfig.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")


        self.txt3 = Label(self.jm,bg='#836FFF', fg ='black', text='''Encontre informações de 
serviços sociais aqui!
Página 1''', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)


        self.btnConfig = Button (self.jm, text = "Opções", bg ='#E6E6FA', fg = "black", font='bold, 10', relief='flat', command = self.barraOpcoes)
        self.btnConfig.place(relx=0.80, rely=0.03, relheight=0.06, relwidth=0.15)


        self.btn1 = Button(self.jm, bg='#E6E6FA', text='CRAS Toyota', font='bold, 10', height=1, width=5, relief='flat', command=self.crasToyota)
        self.btn1.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn2 = Button(self.jm, bg='#E6E6FA', text='CRAS Paraíso', font='bold, 10', height=1, width=5, relief='flat', command=self.crasParaiso)
        self.btn2.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn3 = Button(self.jm, bg='#E6E6FA', text='Prefeitura de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Prefeitura)
        self.btn3.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn4 = Button(self.jm, bg='#E6E6FA', text='Fórum de Resende', font='bold, 10', height=1, width=5, relief='flat', command=self.Forum)
        self.btn4.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn5 = Button(self.jm, bg='#E6E6FA', text='Asilo Nicolino Gulhot', font='bold, 10', height=1, width=5, relief='flat', command=self.Asilo)
        self.btn5.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn6 = Button(self.jm, bg='#E6E6FA', text='Pestalozzi', font='bold, 10', height=1, width=5, relief='flat', command=self.Pestalozzi)
        self.btn6.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm, text = "Avançar", bg ='#E6E6FA', fg = "black", font='bold, 10', relief='flat', command = self.Menu2)
        self.btnPagina1.place(relx=0.75, rely=0.92, relwidth = 0.20, relheight = 0.05)

# Criando segunda pagina de serviços

    def Menu2(self):
        self.jm.withdraw()
        self.jm2 = Tk()
        self.jm2.geometry('320x500+200+100')
        self.jm2.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm2["bg"] = '#836FFF'
        self.jm2.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt3 = Label(self.jm2,bg='#836FFF', text='Página 2', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn7 = Button(self.jm2, bg='#E6E6FA', text='CRAS Itapuca', font='bold, 10', height=1, width=5, relief='flat', command=self.crasItapuca)
        self.btn7.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn8 = Button(self.jm2, bg='#E6E6FA', text='Abrigo Nossa Casa', font='bold, 10', height=1, width=5, relief='flat', command=self.nossaCasa)
        self.btn8.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn9 = Button(self.jm2, bg='#E6E6FA', text='CCI Tobogã', font='bold, 10', height=1, width=5, relief='flat', command=self.cciToboga)
        self.btn9.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn10 = Button(self.jm2, bg='#E6E6FA', text='CRAS Jardim Esperança', font='bold, 10', height=1, width=5, relief='flat', command=self.crasJDEsperanca)
        self.btn10.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn11 = Button(self.jm2, bg='#E6E6FA', text='CRAS Lavapés', font='bold, 10', height=1, width=5, relief='flat', command=self.crasLavapes)
        self.btn11.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn12= Button(self.jm2, bg='#E6E6FA', text='CRAS Itinerante', font='bold, 10', height=1, width=5, relief='flat', command=self.crasItinerante)
        self.btn12.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm2, text = "Avançar", bg ='#E6E6FA', fg='black', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnPagina1.place(relx=0.75, rely=0.92, relwidth = 0.20, relheight = 0.05)

        self.btnVoltarPrinc = Button(self.jm2, text='Voltar', bg ='#836FFF', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


# Criando terceira página de serviços

    def Menu3(self):
        self.jm2.withdraw()
        self.jm3 = Tk()
        self.jm3.geometry('320x500+200+100')
        self.jm3.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm3["bg"] = '#836FFF'
        self.jm3.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt3 = Label(self.jm3,bg='#836FFF', text='Página 3', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn13 = Button(self.jm3, bg='#E6E6FA', text='CCI Cidade Alegria', font='bold, 10', height=1, width=5, relief='flat', command=self.cciAlegria)
        self.btn13.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn14= Button(self.jm3, bg='#E6E6FA', text='CCI Paraíso', font='bold, 10', height=1, width=5, relief='flat', command=self.cciParaiso)
        self.btn14.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn15= Button(self.jm3, bg='#E6E6FA', text='Programa Família Acolhedora', font='bold, 10', height=1, width=5, relief='flat', command=self.FmlAcolhedora)
        self.btn15.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn16 = Button(self.jm3, bg='#E6E6FA', text='CREAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Creas)
        self.btn16.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn17 = Button(self.jm3, bg='#E6E6FA', text='Centro POP', font='bold, 10', height=1, width=5, relief='flat', command=self.Pop)
        self.btn17.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn18= Button(self.jm3, bg='#E6E6FA', text='SEAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Seas)
        self.btn18.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm3, text = "Avançar", bg ='#E6E6FA', fg='black', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnPagina1.place(relx=0.75, rely=0.92, relwidth = 0.20, relheight = 0.05)

        self.btnVoltarPag2 = Button(self.jm3, text='Voltar', bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPag2.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    
# Criando quarta página de serviços

    def Menu4(self):
        self.jm3.withdraw()
        self.jm4 = Tk()
        self.jm4.geometry('320x500+200+100')
        self.jm4.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm4["bg"] = '#836FFF'
        self.jm4.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setaReturn.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt4 = Label(self.jm4,bg='#836FFF', text='Página 4', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt4.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn19 = Button(self.jm4, bg='#E6E6FA', text='Diretoria de Cad. único e Bolsa Família', font='bold, 10', height=1, width=5, relief='flat', command=self.BolsaFml)
        self.btn19.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn20= Button(self.jm4, bg='#E6E6FA', text='Inclusão Produtiva', font='bold, 10', height=1, width=5, relief='flat', command=self.IncProdutiva)
        self.btn20.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn21= Button(self.jm4, bg='#E6E6FA', text='Políticas para Pessoas com Deficiência', font='bold, 10', height=1, width=5, relief='flat', command=self.PolPessoasDeficientes)
        self.btn21.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn22 = Button(self.jm4, bg='#E6E6FA', text='Casa dos Conselhos Municipais', font='bold, 10', height=1, width=5, relief='flat', command=self.ConselhosMunicipais)
        self.btn22.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn23 = Button(self.jm4, bg='#E6E6FA', text='Núcleo Integrado de Atendimento à Mulher', font='bold, 10', height=1, width=5, relief='flat', command=self.Niam)
        self.btn23.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn24= Button(self.jm4, bg='#E6E6FA', text='SEAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Seas)
        self.btn24.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)


        self.btnVoltarPag3 = Button(self.jm4, text='Voltar', bg ='#836FFF', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)




AcesSocial()
