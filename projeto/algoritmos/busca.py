def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

def busca_binaria(lista, elemento):
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (high + low) // 2
        if lista[mid] < elemento:
            low = mid + 1
        elif lista[mid] > elemento:
            high = mid - 1
        else:
            return mid
    return -1