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

drop_table = '''
DROP TABLE Estoque
'''

insert_query = '''
INSERT INTO Produto VALUES ('Borracha', 3.50, 'carai borracha mano')
'''

cursor.execute(create_tableEstoque_query)
# cursor.execute(insert_query)

connection.commit()

connection.close()
