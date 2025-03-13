import sqlite3
from business.produto import Produto
from business.estoque import Estoque
from business.venda import Venda

# def test_exclusaoProduto():
#     produto = Produto("P0015", "Caneta", 15.50, "Caneta azul")
#     produto.strConnect()
#     produto.salvar(acao=1)  # Inserir
#     produto.salvar(acao=3)  # Excluir
#     row = produto.buscaCodigo("P0015")
#     assert len(row) == 0

def test_atualizaEstoque():
    produto = Produto("P0025", "Borracha", 5.50, "borracha preta")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0025", "Borracha", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    venda = Venda("P0025", "12345678901", 5, '2024-11-20', 5.50)
    venda.strConnect()
    venda.salvar(acao=1)  # Inserir

    row = estoque.buscaCodigo("P0025")
    estoque = row[0]
    assert len(row) == 1
    assert row[0].quantidade == 5
