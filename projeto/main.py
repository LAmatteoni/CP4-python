import random
import time
import matplotlib.pyplot as plt
from algoritmos.busca import busca_sequencial, busca_binaria
from algoritmos.ordenacao import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort_wrapper, partition_wrapper

resultados = {}

def gerar_lista(tamanho_lista):
    """Gera uma lista de números aleatórios de um tamanho especificado."""
    return [random.randint(1, 10000) for _ in range(tamanho_lista)]

algoritmos_ordenacao = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort_wrapper,
    partition_wrapper
]

algoritmos_busca = [
    busca_sequencial,
    busca_binaria
]

def medir_tempo_execucao(algoritmo, lista, *args):
    """Mede o tempo de execução de um algoritmo."""
    inicio = time.time()
    resultado = algoritmo(lista, *args)
    fim = time.time()
    return fim - inicio, resultado

def testar_algoritmos_ordenacao(tamanho_lista):
    """Testa os algoritmos de ordenação e armazena os tempos de execução."""
    lista = gerar_lista(tamanho_lista)
    for algoritmo in algoritmos_ordenacao:
        lista_ordenada = lista.copy()
        tempo_execucao, _ = medir_tempo_execucao(algoritmo, lista_ordenada)
        # Atualize o dicionário de resultados
        if algoritmo.__name__ not in resultados:
            resultados[algoritmo.__name__] = []
        resultados[algoritmo.__name__].append(tempo_execucao)
        print(f"{algoritmo.__name__}: {tempo_execucao:.5f} segundos")

def testar_algoritmos_busca(tamanho_lista):
    """Testa os algoritmos de busca e imprime o tempo de execução."""
    lista = gerar_lista(tamanho_lista)
    elemento = random.choice(lista)  # Escolha um elemento aleatório da lista
    lista_ordenada = sorted(lista)  # Ordena a lista para a busca binária
    for algoritmo in algoritmos_busca:
        if algoritmo == busca_binaria:
            tempo_execucao, resultado = medir_tempo_execucao(algoritmo, lista_ordenada, elemento)
        else:
            tempo_execucao, resultado = medir_tempo_execucao(algoritmo, lista, elemento)
        
        if resultado is not None:
            print(f"{algoritmo.__name__}: Elemento encontrado na posição {resultado}")
        else:
            print(f"{algoritmo.__name__}: {tempo_execucao:.5f} segundos")

def testar_algoritmos_ordenacao_varios_tamanhos(tamanhos_lista):
    """Testa os algoritmos de ordenação com diferentes tamanhos de lista e imprime o tempo de execução."""
    for tamanho_lista in tamanhos_lista:
        print(f"\nTestando algoritmos de ordenação com {tamanho_lista} elementos:")
        testar_algoritmos_ordenacao(tamanho_lista)

def testar_algoritmos_busca_varios_tamanhos(tamanhos_lista):
    """Testa os algoritmos de busca com diferentes tamanhos de lista e imprime o tempo de execução."""
    for tamanho_lista in tamanhos_lista:
        print(f"\nTestando algoritmos de busca com {tamanho_lista} elementos:")
        testar_algoritmos_busca(tamanho_lista)

def gerar_grafico_resultados_ordenacao(tamanhos_lista):
    """Gera um gráfico dos resultados dos tempos de execução dos algoritmos de ordenação."""
    fig, ax = plt.subplots()
    for algoritmo, tempos in resultados.items():
        # Ignora os algoritmos de busca
        if "busca" not in algoritmo:
            ax.plot(tamanhos_lista, tempos, label=algoritmo, marker='o')
    ax.set_xlabel('Tamanho da Lista')
    ax.set_ylabel('Tempo de Execução (segundos)')
    ax.set_title('Comparação de Tempo de Execução dos Algoritmos de Ordenação')
    ax.legend() # Garante que a legenda seja exibida
    plt.savefig('relatorio_grafico_ordenacao.png')
    plt.show()

# Lista de tamanhos de lista para testar
tamanhos_lista = [100, 1000, 10000]

testar_algoritmos_ordenacao_varios_tamanhos(tamanhos_lista)

# Gerar gráfico dos resultados dos algoritmos de ordenação
gerar_grafico_resultados_ordenacao(tamanhos_lista)


