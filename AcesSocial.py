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
        self.jm2.wm_withdraw()
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

    def crasItinerante(self):
        self.jm2.wm_withdraw()
        self.telaItinerante = Toplevel()
        self.telaItinerante.geometry('320x500+200+100')
        self.telaItinerante.resizable(True, True)
        self.telaItinerante["bg"] = '#ffffff'
        self.telaItinerante.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtItinerante = Label(self.telaItinerante,bg='#ffffff', text='''CRAS Itinerante
Endereço: 
Rua do Rosário
n° 45 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9510''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtItinerante.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaItinerante, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)
        
    def nossaCasa(self):
        self.jm2.wm_withdraw()
        self.telanossaCasa = Toplevel()
        self.telanossaCasa.geometry('320x500+200+100')
        self.telanossaCasa.resizable(True, True)
        self.telanossaCasa["bg"] = '#ffffff'
        self.telanossaCasa.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtnossaCasa = Label(self.telanossaCasa,bg='#ffffff', text='''Abrigo nossa Casa
Endereço: 
Av.Rita Maria Ferreira da Rocha
n° 1301 - Jardim Jalisco
Resende - RJ, 
Telefone: (24) 3360-9888''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtnossaCasa.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telanossaCasa, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)
    
    def crasLavapes(self):
        self.jm2.wm_withdraw()
        self.telaLavapes = Toplevel()
        self.telaLavapes.geometry('320x500+200+100')
        self.telaLavapes.resizable(True, True)
        self.telaLavapes["bg"] = '#ffffff'
        self.telaLavapes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtLavapes = Label(self.telaLavapes,bg='#ffffff', text='''CRAS Lavapés
Endereço: 
Rua Eduardo Cotrim
n° 36 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9887''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtLavapes.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telaLavapes, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def crasJDEsperanca(self):
        self.jm2.wm_withdraw()
        self.telajdEsperanca = Toplevel()
        self.telajdEsperanca.geometry('320x500+200+100')
        self.telajdEsperanca.resizable(True, True)
        self.telajdEsperanca["bg"] = '#ffffff'
        self.telajdEsperanca.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtjdEsperanca = Label(self.telajdEsperanca,bg='#ffffff', text='''CRAS Jardim Esperança
Endereço: 
Rua Frei Tito
n° 27 - Fazenda da Barra I
Resende - RJ, 
Telefone: (24) 3354-4676''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtjdEsperanca.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telajdEsperanca, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


    def cciToboga(self):
        self.jm2.wm_withdraw()
        self.telacciToboga = Toplevel()
        self.telacciToboga.geometry('320x500+200+100')
        self.telacciToboga.resizable(True, True)
        self.telacciToboga["bg"] = '#ffffff'
        self.telacciToboga.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtcciToboga = Label(self.telacciToboga,bg='#ffffff', text='''CCI Tobogã
Endereço: 
Rua Governador Portela
s/n° (Parque Tobogã) - Manejo.
Resende - RJ, 
Telefone: (24) 3360-0685''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtcciToboga.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPrinc = Button(self.telacciToboga, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def cciAlegria(self):
        self.jm3.wm_withdraw()
        self.telacciAlegria = Toplevel()
        self.telacciAlegria.geometry('320x500+200+100')
        self.telacciAlegria.resizable(True, True)
        self.telacciAlegria["bg"] = '#ffffff'
        self.telacciAlegria.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtcciAlegria = Label(self.telacciAlegria,bg='#ffffff', text='''CCI Cidade Alegria
Endereço: 
Rua das Samambaias, 
s/n - Cidade Alegria.
Resende - RJ, 
Telefone: (24) 3359-5557''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtcciAlegria.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telacciAlegria, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def cciParaiso(self):
        self.jm3.wm_withdraw()
        self.telacciParaiso = Toplevel()
        self.telacciParaiso.geometry('320x500+200+100')
        self.telacciParaiso.resizable(True, True)
        self.telacciParaiso["bg"] = '#ffffff'
        self.telacciParaiso.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtcciParaiso = Label(self.telacciParaiso,bg='#ffffff', text='''CCI Paraíso
Endereço: 
Rua Dom Bosco, 
s/n (Parque Paraíso) - Paraíso.
Resende - RJ, 
Telefone: (24) 3360-3707''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtcciParaiso.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telacciParaiso, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def FmlAcolhedora(self):
        self.jm3.wm_withdraw()
        self.telaFmlAcolhedora = Toplevel()
        self.telaFmlAcolhedora.geometry('320x500+200+100')
        self.telaFmlAcolhedora.resizable(True, True)
        self.telaFmlAcolhedora["bg"] = '#ffffff'
        self.telaFmlAcolhedora.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtFmlAcolhedora = Label(self.telaFmlAcolhedora,bg='#ffffff', text='''Programa Família Acolhedora
Endereço: 
Rua Pandiá Calógeras, 
n° 157 - Jardim Jalisco
Resende - RJ, 
Telefone: (24) 3381-6174
''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtFmlAcolhedora.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaFmlAcolhedora, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def Creas(self):
        self.jm3.wm_withdraw()
        self.telaCreas = Toplevel()
        self.telaCreas.geometry('320x500+200+100')
        self.telaCreas.resizable(True, True)
        self.telaCreas["bg"] = '#ffffff'
        self.telaCreas.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtCreas = Label(self.telaCreas,bg='#ffffff', text='''CREAS
Endereço: 
Rua Natanael Galvão, 
n° 48 - Jardim Tropical
Resende - RJ, 
Telefone: (24) 3360-9775''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtCreas.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaCreas, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def Pop(self):
        self.jm3.wm_withdraw()
        self.telaPop = Toplevel()
        self.telaPop.geometry('320x500+200+100')
        self.telaPop.resizable(True, True)
        self.telaPop["bg"] = '#ffffff'
        self.telaPop.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtPop = Label(self.telaPop,bg='#ffffff', text='''Centro POP (Centro de
referência especializado para 
a população em situação de rua)
Endereço: 
Rua do Rosário, n° 230 - Lavapés
Resende - RJ, 
Telefone: (24) 3360-9739''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtPop.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaPop, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def Seas(self):
        self.jm3.wm_withdraw()
        self.telaSeas = Toplevel()
        self.telaSeas.geometry('320x500+200+100')
        self.telaSeas.resizable(True, True)
        self.telaSeas["bg"] = '#ffffff'
        self.telaSeas.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtSeas = Label(self.telaSeas,bg='#ffffff', text='''SEAS
Endereço: 
Rua Luis Rocha Miranda, 
n° 44 - Centro
Resende - RJ, 
Telefone: (24) 3360-9939''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtSeas.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaSeas, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def BolsaFml(self):
        self.jm4.wm_withdraw()
        self.telaBolsaFml = Toplevel()
        self.telaBolsaFml.geometry('320x500+200+100')
        self.telaBolsaFml.resizable(True, True)
        self.telaBolsaFml["bg"] = '#ffffff'
        self.telaBolsaFml.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtBolsaFml = Label(self.telaBolsaFml,bg='#ffffff', text='''DIRETORIA DE CAD. ÚNICO
E PROGRAMA BOLSA FAMÍLIA
Endereço: 
Rua Luis Rocha Miranda, 
n° 44 - Centro
Resende - RJ, 
Telefone: (24) 3354-1458
cadastrounico.resende@hotmail.com''',
        font='arial, 10', height=1, width=5, relief='flat')
        self.txtBolsaFml.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaBolsaFml, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def IncProdutiva(self):
        self.jm4.wm_withdraw()
        self.telaInc = Toplevel()
        self.telaInc.geometry('320x500+200+100')
        self.telaInc.resizable(True, True)
        self.telaInc["bg"] = '#ffffff'
        self.telaInc.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtInc = Label(self.telaInc,bg='#ffffff', text='''Inclusão Produtiva
Endereço: 
Estrada Resende-Riachuelo, 
s/n, Morada da Colina
Resende - RJ, 
Telefone: (24) 3355 8693''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtInc.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaInc, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def PolPessoasDeficientes(self):
        self.jm4.wm_withdraw()
        self.telaPolDeficiemtes = Toplevel()
        self.telaPolDeficiemtes.geometry('320x500+200+100')
        self.telaPolDeficiemtes.resizable(True, True)
        self.telaPolDeficiemtes["bg"] = '#ffffff'
        self.telaPolDeficiemtes.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtPolDef = Label(self.telaPolDeficiemtes,bg='#ffffff', text='''Coordenadoria de Políticas 
para as Pessoas com Deficiência
Endereço: 
Av. Riachuelo, 
n° 232 - Nova Liberdade
Resende - RJ, 
Telefone: (24) 3381-4297
cpd.resenderj@bol.com.br''',
        font='arial, 10', height=1, width=5, relief='flat')
        self.txtPolDef.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaPolDeficiemtes, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def ConselhosMunicipais(self):
        self.jm4.wm_withdraw()
        self.telaConsMun = Toplevel()
        self.telaConsMun.geometry('320x500+200+100')
        self.telaConsMun.resizable(True, True)
        self.telaConsMun["bg"] = '#ffffff'
        self.telaConsMun.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtConsMun = Label(self.telaConsMun,bg='#ffffff', text='''Casa dos Conselhos Municipais
Endereço: 
Rua do Rosário, 
nº 45 - Lavapés
Resende - RJ, 
Telefone: (24) 3381 - 8674 / (24) 3354 - 6365
casadosconselhosresende@gmail.com''',
        font='arial, 10', height=1, width=5, relief='flat')
        self.txtConsMun.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaConsMun, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    def Niam(self):
        self.jm4.wm_withdraw()
        self.telaNiam = Toplevel()
        self.telaNiam.geometry('320x500+200+100')
        self.telaNiam.resizable(True, True)
        self.telaNiam["bg"] = '#ffffff'
        self.telaNiam.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")

        self.txtNiam = Label(self.telaNiam,bg='#ffffff', text='''NIAM - Núcleo Integrado 
de Atendimento à Mulher
Endereço: 
Rua Macedo de Miranda, 
nº 81, bairro Jardim Jalisco I
Resende - RJ, 
Telefone: (24) 3360-9824
niamresende@yahoo.com.br''',
        font='arial, 15', height=1, width=5, relief='flat')
        self.txtNiam.place(relx=0.00, rely=0.20, relwidth= 1, relheight= 0.40)
        self.btnVoltarPag3 = Button(self.telaNiam, image = self.imgVoltar, bg ='white', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)




# Crianddo primeira página com os serviços sociais

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
        self.imgPagina = PhotoImage(file="setaPagina.png")



        #self.txt3 = Label (self.jm, bg='black', text="Procure por um serviço social aqui!", font='arial, 11', height=1, width=5, relief='flat' )
        #self.txt1.place(relx= 0.06, rely=0.03, relwidth= 0.08, relheight= 0.20)
        self.txt3 = Label(self.jm,bg='white', text='''Encontre informações de 
serviços sociais aqui!
Página 1''', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)


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
        self.jm.withdraw()
        self.jm2 = Tk()
        self.jm2.geometry('320x500+200+100')
        self.jm2.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm2["bg"] = '#ffffff'
        self.jm2.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt3 = Label(self.jm2,bg='white', text='Página 2', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn7 = Button(self.jm2, bg='#7ca4da', text='CRAS Itapuca', font='bold, 10', height=1, width=5, relief='flat', command=self.crasItapuca)
        self.btn7.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn8 = Button(self.jm2, bg='#7ca4da', text='Abrigo Nossa Casa', font='bold, 10', height=1, width=5, relief='flat', command=self.nossaCasa)
        self.btn8.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn9 = Button(self.jm2, bg='#7ca4da', text='CCI Tobogã', font='bold, 10', height=1, width=5, relief='flat', command=self.cciToboga)
        self.btn9.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn10 = Button(self.jm2, bg='#7ca4da', text='CRAS Jardim Esperança', font='bold, 10', height=1, width=5, relief='flat', command=self.crasJDEsperanca)
        self.btn10.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn11 = Button(self.jm2, bg='#7ca4da', text='CRAS Lavapés', font='bold, 10', height=1, width=5, relief='flat', command=self.crasLavapes)
        self.btn11.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn12= Button(self.jm2, bg='#7ca4da', text='CRAS Itinerante', font='bold, 10', height=1, width=5, relief='flat', command=self.crasItinerante)
        self.btn12.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm2, text = "Avançar", bg ='#3ec4cd', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnPagina1.place(relx=0.75, rely=0.90, relwidth = 0.20, relheight = 0.10)

        self.btnVoltarPrinc = Button(self.jm2, text='Voltar', bg ='white', font='bold, 10', relief='flat', command = self.JanelaMenu)
        self.btnVoltarPrinc.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)


# Criando terceira página de serviços

    def Menu3(self):
        self.jm2.withdraw()
        self.jm3 = Tk()
        self.jm3.geometry('320x500+200+100')
        self.jm3.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm3["bg"] = '#ffffff'
        self.jm3.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt3 = Label(self.jm3,bg='white', text='Página 3', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt3.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn13 = Button(self.jm3, bg='#7ca4da', text='CCI Cidade Alegria', font='bold, 10', height=1, width=5, relief='flat', command=self.cciAlegria)
        self.btn13.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn14= Button(self.jm3, bg='#7ca4da', text='CCI Paraíso', font='bold, 10', height=1, width=5, relief='flat', command=self.cciParaiso)
        self.btn14.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn15= Button(self.jm3, bg='#7ca4da', text='Programa Família Acolhedora', font='bold, 10', height=1, width=5, relief='flat', command=self.FmlAcolhedora)
        self.btn15.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn16 = Button(self.jm3, bg='#7ca4da', text='CREAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Creas)
        self.btn16.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn17 = Button(self.jm3, bg='#7ca4da', text='Centro POP', font='bold, 10', height=1, width=5, relief='flat', command=self.Pop)
        self.btn17.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn18= Button(self.jm3, bg='#7ca4da', text='SEAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Seas)
        self.btn18.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnPagina1 = Button (self.jm3, text = "Avançar", bg ='#3ec4cd', font='bold, 10', relief='flat', command = self.Menu4)
        self.btnPagina1.place(relx=0.75, rely=0.90, relwidth = 0.20, relheight = 0.10)

        self.btnVoltarPag2 = Button(self.jm3, text='Voltar', bg ='white', font='bold, 10', relief='flat', command = self.Menu2)
        self.btnVoltarPag2.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)

    
# Criando quarta página de serviços

    def Menu4(self):
        self.jm2.withdraw()
        self.jm4 = Tk()
        self.jm4.geometry('320x500+200+100')
        self.jm4.title('AcesSocial')
        self.root.resizable(False,False)
        self.jm4["bg"] = '#ffffff'
        self.jm4.iconbitmap("pessoas.ico")
        self.imgVoltar = PhotoImage(file = "setavoltar.png")
        self.imgPagina = PhotoImage(file="setaPagina.png")
        self.txt4 = Label(self.jm4,bg='white', text='Página 4', font='arial, 9', height=1, width=5, relief='flat' )
        self.txt4.place(relx= 0.11, rely=0.00, relwidth= 0.80, relheight= 0.10)

        self.btn19 = Button(self.jm4, bg='#7ca4da', text='Diretoria de Cad. único e Bolsa Família', font='bold, 10', height=1, width=5, relief='flat', command=self.BolsaFml)
        self.btn19.place(relx=0.10, rely=0.13, relwidth = 0.80, relheight = 0.10)
        self.btn20= Button(self.jm4, bg='#7ca4da', text='Inclusão Produtiva', font='bold, 10', height=1, width=5, relief='flat', command=self.IncProdutiva)
        self.btn20.place(relx=0.10, rely=0.78, relwidth = 0.80, relheight = 0.10)
        self.btn21= Button(self.jm4, bg='#7ca4da', text='Políticas para Pessoas com Deficiência', font='bold, 10', height=1, width=5, relief='flat', command=self.PolPessoasDeficientes)
        self.btn21.place(relx=0.10, rely=0.65, relwidth = 0.80, relheight = 0.10)
        self.btn22 = Button(self.jm4, bg='#7ca4da', text='Casa dos Conselhos Municipais', font='bold, 10', height=1, width=5, relief='flat', command=self.ConselhosMunicipais)
        self.btn22.place(relx=0.10, rely=0.52, relwidth = 0.80, relheight = 0.10)
        self.btn23 = Button(self.jm4, bg='#7ca4da', text='Núcleo Integrado de Atendimento à Mulher', font='bold, 10', height=1, width=5, relief='flat', command=self.Niam)
        self.btn23.place(relx=0.10, rely=0.39, relwidth = 0.80, relheight = 0.10)
        self.btn24= Button(self.jm4, bg='#7ca4da', text='SEAS', font='bold, 10', height=1, width=5, relief='flat', command=self.Seas)
        self.btn24.place(relx=0.10, rely=0.26, relwidth = 0.80, relheight = 0.10)

        self.btnVoltarPag3 = Button(self.jm4, text='Voltar', bg ='white', font='bold, 10', relief='flat', command = self.Menu3)
        self.btnVoltarPag3.place(relx=0.02, rely=0.03, relheight=0.08, relwidth=0.20)



AcesSocial()
