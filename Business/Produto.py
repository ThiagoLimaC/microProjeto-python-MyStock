from Database.IBase import IBase
from Database.Base import Base
from typing import List

class Produto(Base):

    def _init_(self, id: int, nome: str, valor: float, descricao: str):
        super()._init_()
        self.id = id
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
