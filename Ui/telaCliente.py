from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business.cliente import Cliente

class Funcs():

    # limpa todos os campos de inserção 
    def limpa_tela(self):
        self.cpf_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
    
    # atribui todos os campos a variáveis para 
    # facilitar a utilização

    def variaveis(self):
        self.cpf = self.cpf_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.endereco = self.endereco_entry.get()
    
    # método destinado a adição de itens no banco de dados
    def add_item(self):
        
        self.variaveis()

        # faz verificação se o campo nome, código ou valor está vazio
        # e exibe mensagem alerta caso for o caso
        if(self.nome == "") or (self.cpf == ""):
            msg = "Para cadastrar um novo cliente é necessário \n"
            msg += "que seja digitado pelo menos um CPF e nome"
            messagebox.showinfo("Cadastro de clientes - Aviso !!!", msg)
        # faz o cadastro do produto caso os campos estejam corretamente preenchidos
        else:
            novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    # faz um select no banco e insere os produtos na lista 
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        c = Cliente('','','','')
        c.strConnect()
        lista = c.todos()

        for item in lista:
            self.listaCli.insert("", END, values=(item.cpf, item.nome, item.telefone, item.endereco))
    
    # define o método do evento de dois cliques na lista e insere as linhas nos campos
    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.cpf_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.endereco_entry.insert(END, col4)
        
    # método que faz a exclusão do produto no banco de dados    
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()

    # método que faz a edição do produto no banco de dados
    def altera_item(self):
        self.variaveis()
        
        novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()
    
    # método que faz o select de um produto e trás a informações para os campos 
    def busca_item(self):
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()

        c = Cliente('', '', '', '')
        c.strConnect()
        lista = c.busca(nome)

        for item in lista:
            self.listaCli.insert("", END, values=(item.cpf, item.nome, item.telefone, item.endereco))

        self.limpa_tela()