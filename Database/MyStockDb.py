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

cursor.execute(create_table_query)

connection.commit()

connection.close()
