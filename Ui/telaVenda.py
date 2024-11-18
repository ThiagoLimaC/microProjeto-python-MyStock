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
        v = Venda('','','','','')
        v.strConnect()
        lista = v.todos()

        for item in lista:
            self.listaVend.insert("", END, values=(item.codigo, item.cpf, item.quantidade, item.dataVenda))
    

    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaVend.selection()

        for n in self.listaVend.selection():
            col1, col2, col3, col4, col5 = self.listlistaVendaEst.item(n, 'values')
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

        novo_item = Venda(self.codigo, self.nome, self.quantidade, self.quantMax, self.quantMin)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()

    def busca_item(self):
        
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()

        e = Produto('', '', '', '')
        e.strConnect()
        lista = e.busca(nome)

        for item in lista:
            self.codigo_entry.insert(0, item.codigo)

        self.nome_entry.delete(len(self.nome_entry.get())-1, END)

    