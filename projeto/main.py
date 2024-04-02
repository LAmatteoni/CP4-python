import time
import matplotlib.pyplot as plt
from algoritmos.busca import busca_sequencial, busca_binaria
from algoritmos.ordenacao import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Função para testar os algoritmos de busca e ordenação
def testar_algoritmo(algoritmo, vetor, elemento=None):
    if elemento is not None:
        print(f"Testando {algoritmo.__name__} com o elemento: {elemento} na lista: {vetor}")
    else:
        print(f"Testando {algoritmo.__name__} com o vetor: {vetor}")
    inicio = time.time()
    resultado = algoritmo(vetor, elemento) if elemento is not None else algoritmo(vetor)
    fim = time.time()
    if elemento is not None:
        print(f"Resultado: {resultado}")
    else:
        print(f"Vetor ordenado: {resultado}")
    print(f"Tempo de execução: {fim - inicio} segundos\n")

# Testando cada algoritmo de busca com diferentes cenários
algoritmos_busca = [busca_sequencial, busca_binaria]
vetores_busca = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [1]]
elementos_busca = [3, 6, 5, 1, 1]

for algoritmo in algoritmos_busca:
    for vetor, elemento in zip(vetores_busca, elementos_busca):
        testar_algoritmo(algoritmo, vetor, elemento)

# Testando cada algoritmo de ordenação com diferentes vetores
algoritmos_ordenacao = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]
vetores_ordenacao = [[3, 7, 33, 59, 71], [71, 7, 3, 9, 7], [71, 59, 33, 7, 3], [], [42], [3, 7, 3, 9, 7], [-5, -3, -9, -1]]

for algoritmo in algoritmos_ordenacao:
    for vetor in vetores_ordenacao:
        testar_algoritmo(algoritmo, vetor)

# Geração de gráfico (exemplo simplificado, ajuste conforme necessário)
# Este é um exemplo simplificado de como você pode começar a gerar um gráfico.
# Você precisará ajustar este código para coletar e plotar os dados de desempenho reais.
tempos_execucao = [1.2, 0.8, 0.5, 0.3, 0.1] # Exemplo de tempos de execução
tamanhos_vetores = [5, 5, 5, 1, 1, 5, 5] # Exemplo de tamanhos dos vetores

plt.plot(tamanhos_vetores, tempos_execucao, marker='o')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (s)')
plt.title('Análise de Desempenho dos Algoritmos de Busca e Ordenação')
plt.legend(['Busca Sequencial', 'Busca Binária', 'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'])
plt.savefig('relatorio_grafico.png')
plt.show()
