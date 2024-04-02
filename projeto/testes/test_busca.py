import sys
sys.path.insert(0, 'C:/Users/William/Desktop/PYTHON/CP4-python/projeto/algoritmos')
try:
    import busca
    print("Módulo busca importado com sucesso.")
except ImportError:
    print("Falha ao importar o módulo busca.")

def test_busca_sequencial():
    lista = [1, 2, 3, 4, 5]
    assert busca.busca_sequencial(lista, 3) == 2
    assert busca.busca_sequencial(lista, 6) == -1
    assert busca.busca_sequencial([], 1) == -1
    assert busca.busca_sequencial([1], 1) == 0

def test_busca_binaria():
    lista = [1, 2, 3, 4, 5]
    assert busca.busca_binaria(lista, 3) == 2
    assert busca.busca_binaria(lista, 6) == -1
    assert busca.busca_binaria([], 1) == -1
    assert busca.busca_binaria([1], 1) == 0

if __name__ == "__main__":
    test_busca_sequencial()
    test_busca_binaria()
    print("Todos os testes passaram.")
