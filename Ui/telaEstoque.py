from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business.estoque import Estoque

class Funcs():

    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.quantMax_entry.delete(0, END)
        self.quantMin_entry.delete(0, END)

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.quantidade = self.quantidade_entry.get()
        self.quantMax = self.quantMax_entry.get()
        self.quantMin = self.quantMin_entry.get()

    def add_item(self):
        
        self.variaveis()

        # faz verificação se o campo nome, código ou valor está vazio
        # e exibe mensagem alerta caso for o caso
        if(self.codigo == "") or (self.quantidade == "") or (self.quantMin == ""):
            msg = "Para cadastrar um novo produto no estoque é necessário \n"
            msg += "que seja digitado pelo menos um codigo, quantidade e minímo"
            messagebox.showinfo("Cadastro de produtos no estoque - Aviso !!!", msg)
        # faz o cadastro do produto caso os campos estejam corretamente preenchidos
        else:
            novo_item = Estoque(self.codigo, self.quantidade, self.quantMax, self.quantMin)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    def select_lista(self):
        self.listaEst.delete(*self.listaEst.get_children())
        p = Estoque('','','','')
        p.strConnect()
        lista = p.todos()

        for item in lista:
            self.listaEst.insert("", END, values=(item.codigo, item.quantidade, item.quantMax, item.quantMin))
    

    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaEst.selection()

        for n in self.listaEst.selection():
            col1, col2, col3, col4 = self.listaEst.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.quantidade_entry.insert(END, col2)
            self.quantMax_entry.insert(END, col3)
            self.quantMin_entry.insert(END, col4)
    
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Estoque(self.codigo, self.quantidade, self.quantMax, self.quantMin)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()
    
    def altera_item(self):
        self.variaveis()
        
        novo_item = Estoque(self.codigo, self.quantidade, self.quantMax, self.quantMin)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()

    def busca_item(self):
        self.listaEst.delete(*self.listaEst.get_children())

        self.codigo_entry.insert(END, '%')
        codigo = self.codigo_entry.get()

        p = Estoque('', '', '', '')
        p.strConnect()
        lista = p.busca(codigo)

        for item in lista:
            self.listaProd.insert("", END, values=(item.codigo, item.nome, item.valor, item.descricao))

        self.limpa_tela()

class telaEstoque(Funcs):

    def __init__(self, aba1):
        self.aba1 = aba1
        self.wigets_estoque()
        self.lista_estoque()
        self.select_lista()

    def wigets_estoque(self):
        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.29, rely= 0.05, relwidth= 0.22, relheight= 0.11)

        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white",
                                font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.3, rely= 0.07, relwidth=0.1, relheight= 0.07)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white", 
                                font= ('verdana', 8, 'bold'), command= self.busca_item)
        self.bt_buscar.place(relx= 0.4, rely= 0.07, relwidth=0.1, relheight= 0.07)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg= "Digite no campo nome o produto que deseja pesquisar")

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.59, rely= 0.05, relwidth= 0.32, relheight= 0.11)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.add_item)
        self.bt_novo.place(relx= 0.6, rely= 0.07, relwidth=0.1, relheight= 0.07)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.altera_item)
        self.bt_alterar.place(relx= 0.7, rely= 0.07, relwidth=0.1, relheight= 0.07)

        self.bt_alterar = tix.Balloon(self.aba1)
        self.bt_alterar.bind_widget(self.bt_alterar, balloonmsg= "Dê dois cliques no item da lista para trazer as informações do produto")

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.deleta_item)
        self.bt_apagar.place(relx= 0.8, rely= 0.07, relwidth=0.1, relheight= 0.07)

        ### Criação da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text= "Código do Produto", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx= 0.05, rely= 0.11, relwidth= 0.19)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text= "Nome do Produto", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_nome.place(relx= 0.05, rely= 0.2)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx= 0.05, rely= 0.25, relwidth= 0.35)

        ### Criação da label e entrada do valor
        self.lb_quantidade = Label(self.aba1, text= "Quantidade em estoque", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_quantidade.place(relx= 0.05, rely= 0.33)

        self.quantidade_entry = Entry(self.aba1)
        self.quantidade_entry.place(relx= 0.05, rely= 0.39, relwidth= 0.24)

        ### Criação da label e entrada do valor
        self.lb_quantMax = Label(self.aba1, text= "Quantidade Máxima", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_quantMax.place(relx= 0.5, rely= 0.2)

        self.quantMax_entry = Entry(self.aba1)
        self.quantMax_entry.place(relx= 0.5, rely= 0.26, relwidth= 0.21)

        ### Criação da label e entrada do descrição
        self.lb_quantMin = Label(self.aba1, text= "Quantidade Mínima", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_quantMin.place(relx= 0.5, rely= 0.33)

        self.quantMin_entry = Entry(self.aba1)
        self.quantMin_entry.place(relx= 0.5, rely= 0.39, relwidth= 0.21)
    

    def lista_estoque(self):
        self.style = ttk.Style() 
        
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

        self.listaEst = ttk.Treeview(self.aba1, height= 3, columns= ("col1", "col2", "col3", "col4"), style="Treeview")

        self.listaEst.heading('#0', text="")
        self.listaEst.heading('#1', text="Codigo Produto") 
        self.listaEst.heading('#2', text="Quantidade")
        self.listaEst.heading('#3', text="Quant Max")
        self.listaEst.heading('#4', text="Quant Min")

        self.listaEst.column("#0", width=0, anchor= "center")
        self.listaEst.column("#1", width=50, anchor= "center")
        self.listaEst.column("#2", width=55, anchor= "center")
        self.listaEst.column("#3", width=150, anchor= "center")
        self.listaEst.column("#4", width=100, anchor= "center")

        self.listaEst.place(relx= 0.01, rely= 0.5, relwidth= 0.95, relheight= 0.49)

        self.scroolLista = Scrollbar(self.aba1, orient='vertical')
        self.listaEst.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.5, relwidth=0.045, relheight=0.49)

        self.listaEst.bind("<Double-1>", self.OnDoubleClick)