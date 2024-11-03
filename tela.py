from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox
from Produto import Produto

root = tix.Tk()

class GradientFrame(Canvas):
    def __init__(self, parent, color1= "white", color2= "gray", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)
    def _draw_gradient(self, event= None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i)) 
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.descricao_entry.delete(0, END)
    
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.valor = self.valor_entry.get()
        self.descricao = self.descricao_entry.get()
    
    def add_item(self):
        
        self.variaveis()

        if(self.nome == "") or (self.codigo == "") or (self.valor == ""):
            msg = "Para cadastrar um novo produto é necessário \n"
            msg += "que seja digitado pelo menos um codigo, nome e valor"
            messagebox.showinfo("Cadastro de produtos - Aviso !!!", msg)
        else:
            novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    def select_lista(self):
        self.listaProd.delete(*self.listaProd.get_children())
        p = Produto('','','','')
        p.strConnect()
        lista = p.todos()

        for item in lista:
            self.listaProd.insert("", END, values=(item.id, item.codigo, item.nome, item.valor, item.descricao))
    
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaProd.selection()

        for n in self.listaProd.selection():
            col1, col2, col3, col4, col5 = self.listaProd.item(n, 'values')
            self.codigo_entry.insert(END, col2)
            self.nome_entry.insert(END, col3)
            self.valor_entry.insert(END, col4)
            self.descricao_entry.insert(END, col5)
        
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()

    def altera_item(self):
        self.variaveis()
        
        novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()
    
    def busca_item(self):
        self.listaProd.delete(*self.listaProd.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()

        p = Produto('', '', '', '')
        p.strConnect()
        lista = p.busca(nome)

        for item in lista:
            self.listaProd.insert("", END, values=(item.id, item.codigo, item.nome, item.valor, item.descricao))

        self.limpa_tela()

class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Produtos")
        self.root.configure(background= '#4682B4')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height=700)
        self.root.minsize(width= 500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, 
                                        bg="whitesmoke", 
                                        highlightbackground="#708090", highlightthickness=2)
        self.frame_1.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.46)
        
        self.frame_2 = Frame(self.root, bd=4, 
                                        bg="whitesmoke", 
                                        highlightbackground="#708090", highlightthickness=2)
        self.frame_2.place(relx= 0.02,rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame1(self):

        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background= "whitesmoke")
        self.aba2.configure(background= "whitesmoke")

        self.abas.add(self.aba1, text= "Produto")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx= 0, rely= 0, relwidth= 0.98, relheight= 0.98)

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight= 0.19)
        
        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white",
                                font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth=0.1, relheight= 0.15)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white", 
                                font= ('verdana', 8, 'bold'), command= self.busca_item)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth=0.1, relheight= 0.15)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg= "Digite no campo nome o produto que deseja pesquisar")

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.59, rely= 0.08, relwidth= 0.32, relheight= 0.19)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.add_item)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth=0.1, relheight= 0.15)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.altera_item)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth=0.1, relheight= 0.15)

        self.bt_alterar = tix.Balloon(self.aba1)
        self.bt_alterar.bind_widget(self.bt_alterar, balloonmsg= "Dê dois cliques no item da lista para trazer as informações do produto")

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.deleta_item)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth=0.1, relheight= 0.15)

        ### Criação da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text= "Código", bg= None, fg= '#107db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text= "Nome", bg= 'whitesmoke', fg= '#107db2')
        self.lb_nome.place(relx= 0.05, rely= 0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.35)

        ### Criação da label e entrada do valor
        self.lb_valor = Label(self.aba1, text= "Valor", bg= 'whitesmoke', fg= '#107db2')
        self.lb_valor.place(relx= 0.05, rely= 0.60)

        self.valor_entry = Entry(self.aba1)
        self.valor_entry.place(relx= 0.05, rely= 0.70, relwidth= 0.15)

        ### Criação da label e entrada do descrição
        self.lb_descricao = Label(self.aba1, text= "Descrição", bg= 'whitesmoke', fg= '#107db2')
        self.lb_descricao.place(relx= 0.5, rely= 0.35)

        self.descricao_entry = Entry(self.aba1)
        self.descricao_entry.place(relx= 0.5, rely= 0.45, relwidth= 0.4, relheight= 0.35)


    def lista_frame2(self):
        self.listaProd = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5"))
        self.listaProd.heading('#0', text="")
        self.listaProd.heading('#1', text="Id")
        self.listaProd.heading('#2', text="Codigo") 
        self.listaProd.heading('#3', text="Nome")
        self.listaProd.heading('#4', text="Valor")
        self.listaProd.heading('#5', text="Descricao")

        self.listaProd.column("#0", width=0)
        self.listaProd.column("#1", width=50)
        self.listaProd.column("#2", width=50)
        self.listaProd.column("#3", width=150)
        self.listaProd.column("#4", width=100)
        self.listaProd.column("#5", width=250)

        self.listaProd.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaProd.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaProd.bind("<Double-1>", self.OnDoubleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu = filemenu)
        menubar.add_cascade(label= "Sobre", menu = filemenu2)

        filemenu.add_command(label= "Limpar Produto", command= self.limpa_tela)
        filemenu.add_command(label="Sair", command= Quit)
        
Aplication()