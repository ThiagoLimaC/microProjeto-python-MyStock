import sqlite3

connection = sqlite3.connect("MyStockDb.sqlite")

cursor = connection.cursor()

create_tableProduto_query = '''
CREATE TABLE IF NOT EXISTS Produto (
    codigo VARCHAR(7) PRIMARY KEY,
    nome TEXT NOT NULL,
    valor REAL NOT NULL,
    descricao TEXT
)
'''

create_tableEstoque_query = '''
CREATE TABLE IF NOT EXISTS Estoque (
    codigo VARCHAR(7) PRIMARY KEY,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    quantMax INTEGER NOT NULL,
    quantMin INTEGER NOT NULL, 
    FOREIGN KEY (codigo) REFERENCES Produto (codigo),
    FOREIGN KEY (nome) REFERENCES Produto (nome)
)
'''

create_tableCliente_query = '''
CREATE TABLE IF NOT EXISTS Cliente (
    cpf VARCHAR(11) PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    endereco TEXT
)
'''

create_tableVenda_query = '''
CREATE TABLE IF NOT EXISTS Venda (
    idVenda INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(7) NOT NULL,
    cpf VARCHAR(7) NOT NULL,
    quantidade INT NOT NULL,
    dataVenda DATE NOT NULL,
    FOREIGN KEY (codigo) REFERENCES Produto(codigo),
    FOREIGN KEY (cpf) REFERENCES Cliente(cpf)
)
'''

query = "DROP TABLE Venda"

cursor.execute(create_tableVenda_query)

connection.commit()

connection.close()
