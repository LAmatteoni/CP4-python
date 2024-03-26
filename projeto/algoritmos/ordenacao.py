def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista
