def ordena_lista(lista):
    lista.sort()
    return lista

lista = list(map(int, input('Digite uma lista de números separados por espaço: ').split()))
print('A lista ordenada é:', ordena_lista(lista))
