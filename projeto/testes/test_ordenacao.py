from algoritmos.ordenacao import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Vetores fornecidos
vetor_ordenado_crescente = [3, 7, 33, 59, 71]
vetor_nao_ordenado = [71, 7, 3, 9, 7]
vetor_ordenado_descrescente = [71, 59, 33, 7, 3]
vetor_vazio = []
vetor_com_um_elemento = [42]
vetor_com_elementos_repetidos = [3, 7, 3, 9, 7]
vetor_com_elementos_negativos = [-5, -3, -9, -1]

# Função para testar os algoritmos de ordenação
def testar_ordenacao(algoritmo, vetor):
    print(f"Testando {algoritmo.__name__} com o vetor: {vetor}")
    vetor_ordenado = algoritmo(vetor)
    print(f"Vetor ordenado: {vetor_ordenado}\n")

# Testando cada algoritmo com cada vetor
testar_ordenacao(bubble_sort, vetor_ordenado_crescente)
testar_ordenacao(bubble_sort, vetor_nao_ordenado)
testar_ordenacao(bubble_sort, vetor_ordenado_descrescente)
testar_ordenacao(bubble_sort, vetor_vazio)
testar_ordenacao(bubble_sort, vetor_com_um_elemento)
testar_ordenacao(bubble_sort, vetor_com_elementos_repetidos)
testar_ordenacao(bubble_sort, vetor_com_elementos_negativos)

testar_ordenacao(selection_sort, vetor_ordenado_crescente)
testar_ordenacao(selection_sort, vetor_nao_ordenado)
testar_ordenacao(selection_sort, vetor_ordenado_descrescente)
testar_ordenacao(selection_sort, vetor_vazio)
testar_ordenacao(selection_sort, vetor_com_um_elemento)
testar_ordenacao(selection_sort, vetor_com_elementos_repetidos)
testar_ordenacao(selection_sort, vetor_com_elementos_negativos)

testar_ordenacao(insertion_sort, vetor_ordenado_crescente)
testar_ordenacao(insertion_sort, vetor_nao_ordenado)
testar_ordenacao(insertion_sort, vetor_ordenado_descrescente)
testar_ordenacao(insertion_sort, vetor_vazio)
testar_ordenacao(insertion_sort, vetor_com_um_elemento)
testar_ordenacao(insertion_sort, vetor_com_elementos_repetidos)
testar_ordenacao(insertion_sort, vetor_com_elementos_negativos)

testar_ordenacao(merge_sort, vetor_ordenado_crescente)
testar_ordenacao(merge_sort, vetor_nao_ordenado)
testar_ordenacao(merge_sort, vetor_ordenado_descrescente)
testar_ordenacao(merge_sort, vetor_vazio)
testar_ordenacao(merge_sort, vetor_com_um_elemento)
testar_ordenacao(merge_sort, vetor_com_elementos_repetidos)
testar_ordenacao(merge_sort, vetor_com_elementos_negativos)

testar_ordenacao(quick_sort, vetor_ordenado_crescente)
testar_ordenacao(quick_sort, vetor_nao_ordenado)
testar_ordenacao(quick_sort, vetor_ordenado_descrescente)
testar_ordenacao(quick_sort, vetor_vazio)
testar_ordenacao(quick_sort, vetor_com_um_elemento)
testar_ordenacao(quick_sort, vetor_com_elementos_repetidos)
testar_ordenacao(quick_sort, vetor_com_elementos_negativos)


# se nao der certo precisa tentar no terminal do windows, so colar esse codigo
#set PYTHONPATH=%PYTHONPATH%;c:\Users\William\Desktop\PYTHON\CP4-python\projeto\testes\test_ordenacao.py
#python c:\Users\William\Desktop\PYTHON\CP4-python\projeto\testes\test_ordenacao.py