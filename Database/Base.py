import sqlite3
from typing import List, Any
from IBase import IBase

class Base(IBase):

    # definindo o método que contém a string de conexão
    def _init_(self):
        self.connection_string = "MyStockDb.sqlite"

    # definindo o método salvar para Adicionar, Editar ou Remover um item da tabela
    def salvar(self, acao : int):
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            valores = []

            # _dict_ -> mapeia todos os atributos de instância do objeto atual
            # _items() -> fornece um par de chaves atributo e valor
            # o loop percorre cada par atributo/valor do objeto atual e adiciona na lista valores
            for attr, value in self.__dict__.items():
                valores.append(f"'{value}'")

            # Filtro de ação desejada do CRUD
            # self._class_._name_ -> retorna o nome da Classe para ser inserido como nome da tabela no banco
            # join -> concatena os valores da lista separando-os por vírgulas
            if acao == 1:
                query = f"INSERT INTO {self.__class__._name_} VALUES ({','.join(valores)})"
            elif acao == 2:
                query = f"UPDATE {self.__class__._name_} SET {','.join(valores)} WHERE id={self.id}"
            elif acao == 3:
                query = f"DELETE FROM {self.__class__._name_} WHERE id={self.id}"
            
            cursor.execute(query)
            connection.commit()
            
    # definindo o método que retorna todos os items de uma classe
    def todos(self) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__._name_}"
            cursor.execute(query)
            # retorna todas as linhas da tabela e armazena na variável rows
            rows = cursor.fetchall()

            # esse loop captura todas as tuplas da tabela 
            for row in rows:
                # cria uma instância do objeto atual
                obj = self.__class__.__new__(self.__class__)
                # atualiza os atributos utilizando os valores obtidos em row
                obj.__dict__.update(row)
                lista.append(obj)
            return lista
        
    def busca(self, id_busca: int) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__._name_} WHERE id = {self.id}"
            cursor.execute(query, (id_busca,))
            rows = cursor.fetchall()
            for row in rows:
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(row)
                lista.append(obj)
            return lista

    

