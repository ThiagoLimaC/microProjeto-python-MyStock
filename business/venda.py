from database.base import Base
from typing import List
from datetime import date
import sqlite3

class Venda(Base):
    
    primary_keys = ('codigo', 'cpf')

    def __init__(self, codigo: str, cpf: str, quantidade: int, dataVenda: date):
        self.codigo = codigo
        self.cpf = cpf
        self.quantidade = quantidade
        self.dataVenda = dataVenda

    def strConnect(self):
        super().__init__()
