import sys
import os

# Adiciona o diretório raiz ao caminho
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from Produto import Produto
from typing import List

def main():
    # Cria uma nova instância de Produto
    novo_produto = Produto(nome="Monitor", valor=150.00, descricao="Monitor LED LCD LG")
    novo_produto.strConnect()
    novo_produto.salvar(1)  # Salva o produto no banco de dados
    print("Produto salvo com sucesso")
    

    # Lista todos os produtos
    lista_produtos = novo_produto.todos()
    for p in lista_produtos:
        print(f"Id: {p.id}")
        print(f"Nome: {p.nome}")
        print(f"Valor: {p.valor}")
        print(f"Descrição: {p.descricao}")

if __name__ == "__main__":
    main()
