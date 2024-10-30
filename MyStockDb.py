import sqlite3

connection = sqlite3.connect("MyStockDb.sqlite")

cursor = connection.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    valor REAL NOT NULL,
    descricao TEXT
)
'''

insert_query = '''
INSERT INTO Produto VALUES ('Borracha', 3.50, 'carai borracha mano')
'''

cursor.execute(create_table_query)
cursor.execute(insert_query)

connection.commit()

connection.close()
