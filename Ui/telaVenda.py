from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox
from datetime import date

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business.estoque import Estoque
from business.cliente import Cliente
from business.produto import Produto
from business.venda import Venda

class Funcs():

    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.nomeProduto_entry.delete(0, END)
        self.nomeCliente_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.dataVenda_entry.delete(0, END)

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.cpf = self.cpf_entry.get()
        self.quantidade = self.quantidade_entry.get()
        self.dataVenda = self.dataVenda_entry.get()

    def add_item(self):
        
        self.variaveis()

        # faz verificação se o campo nome, código ou valor está vazio
        # e exibe mensagem alerta caso for o caso
        if(self.codigo == "") or (self.cpf == "") or (self.quantidade == "") or (self.dataVenda == ""):
            msg = "Para cadastrar uma nova venda é necessário \n"
            msg += "que seja digitado pelo menos um codigo, cpf, quantidade e data da venda"
            messagebox.showinfo("Cadastro de venda - Aviso !!!", msg)
        # faz o cadastro do produto caso os campos estejam corretamente preenchidos
        else:
            novo_item = Venda(self.codigo, self.cpf, self.quantidade, self.dataVenda)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    def select_lista(self):
        self.listaVend.delete(*self.listaVend.get_children())
        v = Venda('','','','')
        v.strConnect()
        lista = v.todos()

        for item in lista:
            self.listaVend.insert("", END, values=(item.codigo, item.cpf, item.quantidade, item.dataVenda))
    

    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaVend.selection()

        for n in self.listaVend.selection():
            col1, col2, col3, col4 = self.listaVend.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.cpf_entry.insert(END, col2)
            self.quantidade_entry.insert(END, col3)
            self.dataVenda_entry.insert(END, col4)
    
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Estoque(self.codigo, self.cpf, self.quantidade, self.dataVenda)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()
    
    def altera_item(self):
        self.variaveis()

        novo_item = Venda(self.codigo, self.cpf, self.quantidade, self.dataVenda)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()

    def busca_item(self):
        
        self.nomeProduto_entry.insert(END, '%')
        nomeProduto = self.nomeProduto_entry.get()

        p = Produto('', '', '', '')
        p.strConnect()
        listaP = p.busca(nomeProduto)

        for prod in listaP:
            self.codigo_entry.insert(0, prod.codigo)

        self.nomeProduto_entry.delete(len(self.nomeProduto_entry.get())-1, END)

        self.nomeCliente_entry.insert(END, '%')
        nomeCliente = self.nomeCliente_entry.get()

        c = Cliente('', '', '', '')
        c.strConnect()
        listaC = c.busca(nomeCliente)

        for cli in listaC:
            self.cpf_entry.insert(0, cli.cpf)

        self.nomeCliente_entry.delete(len(self.nomeCliente_entry.get())-1, END)

    def estoque_baixo(self):

        prodE = Estoque('','','','','')
        prods = prodE.busca()


        if (self.quantidade_entry.get() <= self.quantMin_entry.get()):
            msg = "Quantidade de produto menor ou igual ao mínimo em estoque"
            messagebox.showinfo("Alerta de Estoque Baixo !!!", msg)

class telaVenda(Funcs):

    def __init__(self, aba1):
        self.aba1 = aba1
        self.wigets_venda()
        self.lista_venda()
        self.select_lista()

    def wigets_venda(self):

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.52, rely= 0.09, relwidth= 0.22, relheight= 0.09)
        
        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white",
                                font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.63, rely= 0.1, relwidth=0.1, relheight= 0.07)


        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white", 
                                font= ('verdana', 8, 'bold'), command= self.busca_item)
        self.bt_buscar.place(relx= 0.53, rely= 0.1, relwidth=0.1, relheight= 0.07)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg= "Digite no campo nome do produto e cliente que deseja pesquisar o código e cpf")

        ### Criação da label e entrada do codigo
        self.lb_nomeProduto = Label(self.aba1, text= "Nome do Produto", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_nomeProduto.place(relx= 0.05, rely= 0.05)

        self.nomeProduto_entry = Entry(self.aba1)
        self.nomeProduto_entry.place(relx= 0.05, rely= 0.11, relwidth= 0.45)

        self.lb_nomeCliente = Label(self.aba1, text= "Nome do Cliente", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_nomeCliente.place(relx= 0.05, rely= 0.17)

        self.nomeCliente_entry = Entry(self.aba1)
        self.nomeCliente_entry.place(relx= 0.05, rely= 0.22, relwidth= 0.45)

        ### Criação da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text= "Codigo do Produto", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_codigo.place(relx= 0.05, rely= 0.29)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx= 0.05, rely= 0.35, relwidth= 0.19)

        ### Criação da label e entrada do codigo
        self.lb_cpf = Label(self.aba1, text= "CPF do Cliente", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_cpf.place(relx= 0.3, rely= 0.29)

        self.cpf_entry = Entry(self.aba1)
        self.cpf_entry.place(relx= 0.3, rely= 0.35, relwidth= 0.23)

        ### Criação da label e entrada do codigo
        self.lb_quantidade = Label(self.aba1, text= "Quantidade", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_quantidade.place(relx= 0.57, rely= 0.29)

        self.quantidade_entry = Entry(self.aba1)
        self.quantidade_entry.place(relx= 0.57, rely= 0.35, relwidth= 0.13)

         ### Criação da label e entrada do codigo
        self.lb_dataVenda = Label(self.aba1, text= "Data da Venda", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_dataVenda.place(relx= 0.73, rely= 0.29)

        self.dataVenda_entry = Entry(self.aba1)
        self.dataVenda_entry.place(relx= 0.73, rely= 0.35, relwidth= 0.15)

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.35, rely= 0.43, relwidth= 0.32, relheight= 0.09)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.add_item)
        self.bt_novo.place(relx= 0.36, rely= 0.44, relwidth=0.1, relheight= 0.07)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.altera_item)
        self.bt_alterar.place(relx= 0.46, rely= 0.44, relwidth=0.1, relheight= 0.07)

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.deleta_item)
        self.bt_apagar.place(relx= 0.56, rely= 0.44, relwidth=0.1, relheight= 0.07)

    def lista_venda(self):
        self.style = ttk.Style() 
        
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

        self.listaVend = ttk.Treeview(self.aba1, height= 3, columns= ("col1", "col2", "col3", "col4"), style="Treeview")

        self.listaVend.heading('#0', text="")
        self.listaVend.heading('#1', text="Codigo Produto") 
        self.listaVend.heading('#2', text="CPF do Cliente") 
        self.listaVend.heading('#3', text="Quantidade")
        self.listaVend.heading('#4', text="Data da Venda")

        self.listaVend.column("#0", width=0, anchor= "center")
        self.listaVend.column("#1", width=65, anchor= "center")
        self.listaVend.column("#2", width=85, anchor= "center")
        self.listaVend.column("#3", width=55, anchor= "center")
        self.listaVend.column("#4", width=55, anchor= "center")

        self.listaVend.place(relx= 0.01, rely= 0.55, relwidth= 0.95, relheight= 0.44)

        self.scroolLista = Scrollbar(self.aba1, orient='vertical')
        self.listaVend.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.55, relwidth=0.045, relheight=0.44)

        self.listaVend.bind("<Double-1>", self.OnDoubleClick)