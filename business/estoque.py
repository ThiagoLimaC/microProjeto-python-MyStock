from database.base import Base
from typing import List

class Estoque(Base):

    def __init__(self, codigo: str, quantidade: int, quantMax: int, quantMin: int):
        self.codigo = codigo
        self.quantidade = quantidade
        self.quantMax = quantMax
        self.quantMin = quantMin
    
    def strConnect(self):
        super().__init__()