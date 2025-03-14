import sqlite3
from business.produto import Produto
from business.estoque import Estoque
from business.venda import Venda

# Testes de Unidade para o módulo de produto

def test_insercaoProduto():
    produto = Produto("P020", "Apagador", 20, "Apagador preto")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    row = produto.buscaCodigo("P020")
    assert len(row) == 1

def test_atualizacaoProduto():
    produto = Produto("P0021", "Calculadora", 50, "Calculadora cientifica")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    produto.nome = "Calculadora cientifica"
    produto.preco = 60
    produto.descricao = "Calculadora cientifica casio"
    produto.salvar(acao=2)  # Atualizar
    row = produto.buscaCodigo("P0021")
    assert len(row) == 1
    assert row[0].nome == "Calculadora cientifica"
    assert row[0].preco == 60
    assert row[0].descricao == "Calculadora cientifica casio"

def test_exclusaoProduto():
    produto = Produto("P0015", "Caneta", 15.50, "Caneta azul")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    produto.salvar(acao=3)  # Excluir
    row = produto.buscaCodigo("P0015")
    assert len(row) == 0

# Testes de Unidade para o módulo de estoque

def test_insercaoEstoque():
    produto = Produto("P0022", "Lapis", 3.50, "Lapis preto")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0022", "Lapis", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir
    row = estoque.buscaCodigo("P0022")
    assert len(row) == 1

def test_atualizacaoEstoque():
    produto = Produto("P0023", "Caderno", 10, "Caderno universitario")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0023", "Caderno", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    estoque.quantidade = 15
    estoque.minimo = 10
    estoque.maximo = 25
    estoque.salvar(acao=2)  # Atualizar
    
    row = estoque.buscaCodigo("P0023")
    assert len(row) == 1
    assert row[0].quantidade == 15
    assert row[0].minimo == 10
    assert row[0].maximo == 25

def test_exclusaoEstoque():
    produto = Produto("P0024", "Borracha", 5.50, "Borracha preta")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0024", "Borracha", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    estoque.salvar(acao=3)  # Excluir
    row = estoque.buscaCodigo("P0024")
    assert len(row) == 0

# Testes de Unidade para o módulo de venda
    
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
