from Base import Base
from typing import List

class Produto(Base):

    def __init__(self, codigo: str, nome: str, valor: float, descricao: str):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def strConnect(self):
        super().__init__()
    