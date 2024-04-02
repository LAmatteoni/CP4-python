from algoritmos.busca import busca_sequencial, busca_binaria

def test_busca_sequencial():
    lista = [1, 2, 3, 4, 5]
    assert busca_sequencial(lista, 3) == 2
    assert busca_sequencial(lista, 6) == -1
    assert busca_sequencial([], 1) == -1
    assert busca_sequencial([1], 1) == 0

def test_busca_binaria():
    lista = [1, 2, 3, 4, 5]
    assert busca_binaria(lista, 3) == 2
    assert busca_binaria(lista, 6) == -1
    assert busca_binaria([], 1) == -1
    assert busca_binaria([1], 1) == 0

if __name__ == "__main__":
    test_busca_sequencial()
    test_busca_binaria()
    print("Todos os testes passaram.")