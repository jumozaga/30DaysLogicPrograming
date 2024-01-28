def maximo_minimo(lista):
    return max(lista), min(lista)

lista = list(map(int, input('Digite uma lista de números separados por espaço: ').split()))
print('O máximo e o mínimo na lista são:', maximo_minimo(lista))
