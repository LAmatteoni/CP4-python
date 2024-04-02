# Biblioteca de Algoritmos Personalizada

Este projeto tem como foco o estudo prático de algoritmos de busca e ordenação aplicados a cenários reais. Ele inclui o desenvolvimento de uma biblioteca personalizada em Python que incorpora as técnicas de ordenação e busca estudadas, seguindo as melhores práticas de programação orientada a objetos (POO).

## Estrutura da Biblioteca

A biblioteca está estruturada da seguinte forma:

projeto/
│
├── algoritmos/
│ ├── init.py
│ ├── ordenacao.py
│ └── busca.py
│
├── testes/
│ ├── init.py
│ ├── test_ordenacao.py
│ └── test_busca.py
│
└── main.py


- O pacote `algoritmos` contém módulos para ordenação (`ordenacao.py`) e busca (`busca.py`).
- O pacote `testes` contém módulos para testar os algoritmos de ordenação e busca.
- `main.py` é a aplicação principal onde a biblioteca personalizada é utilizada como um módulo.

## Implementações

### Algoritmos de Ordenação

Todos os algoritmos de ordenação estudados estão implementados no módulo `ordenacao.py`.

### Algoritmos de Busca

Todos os algoritmos de busca estudados estão implementados no módulo `busca.py`.

## Testes

O pacote de testes inclui testes para validar a funcionalidade da biblioteca. Os testes cobrem diferentes tamanhos de entrada e condições, como listas ordenadas e não ordenadas.

### Testes de Ordenação

- Vetor ordenado crescente: [3, 7, 33, 59, 71]
- Vetor não ordenado: [71, 7, 3, 9, 7]
- Vetor ordenado decrescente: [71, 59, 33, 7, 3]
- Vetor vazio: []
- Vetor com um único elemento: [42]
- Vetor com elementos repetidos: [3, 7, 3, 9, 7]
- Vetor com elementos negativos: [-5, -3, -9, -1]

### Testes de Busca

- Busca por um elemento presente no vetor.
- Busca por um elemento não presente no vetor.
- Busca em um vetor vazio.
- Busca em um vetor com um único elemento.

## Análise de Desempenho e Relatórios de Teste

A análise de desempenho é realizada para determinar a eficiência dos algoritmos. Esta análise calcula o tempo de execução de cada algoritmo.

### Passos:

1. Importar módulos necessários: Importar os módulos de ordenação e busca da biblioteca, juntamente com módulos adicionais como `time`, `random` e `matplotlib.pyplot`.

2. Gerar dados de teste: Criar listas de diferentes tamanhos para testar os algoritmos de ordenação e busca.

3. Medir tempo de execução: Para cada lista de teste, medir o tempo de execução de cada algoritmo de ordenação e busca.

4. Armazenar resultados: Armazenar os resultados dos tempos de execução em um dicionário.

5. Gerar gráfico: Usar `matplotlib.pyplot` para gerar um gráfico comparando o tempo de execução dos algoritmos em função do tamanho da lista de teste.

6. Salvar gráfico: Salvar o gráfico como uma imagem.

7. Identificar o algoritmo campeão: Analisar o gráfico para determinar qual algoritmo teve o melhor desempenho em termos de tempo de execução.


## Contribuidores

- [Lucca]
- [Willian]
- [G.Onodera]


