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

drop_table = '''
DROP TABLE Produto
'''

insert_query = '''
INSERT INTO Produto VALUES ('Borracha', 3.50, 'carai borracha mano')
'''

cursor.execute(create_tableProduto_query)
# cursor.execute(insert_query)

connection.commit()

connection.close()
