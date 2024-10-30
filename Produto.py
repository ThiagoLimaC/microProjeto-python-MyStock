from Base import Base
from typing import List

class Produto(Base):

    def __init__(self, nome: str, valor: float, descricao: str):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def strConnect(self):
        super().__init__()
    