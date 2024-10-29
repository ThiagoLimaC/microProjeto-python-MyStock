import sqlite3
from typing import List, Any
from IBase import IBase

class Base(IBase):

    # definindo o método que contém a string de conexão
    def _init_(self, connection_string: str):
        self.connection_string = myStockBd.sqlite

    def salvar(self, acao : int):
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            valores = []

            for attr, value in self.__dict__.items():
                valores.append(f"'{value}'")

            if acao == 1:
                query = f"INSERT INTO {self.__class__._name_} VALUES ({','.join(valores)})"
            elif acao == 2:
                query = f"UPDATE {self.__class__._name_} SET {','.join(valores)} WHERE id=?"
            if acao == 3:
                query = f"DELETE FROM {self.__class__._name_} WHERE id=?"

            

    def todos(self) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__._name_}"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(row)
                lista.append(obj)
            return lista
        
    def busca(self, id_busca: int) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__._name_} WHERE id = ?"
            cursor.execute(query, (id_busca,))
            rows = cursor.fetchall()
            for row in rows:
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(row)
                lista.append(obj)
            return lista

    

