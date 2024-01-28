def media(numeros):
    positivos = [num for num in numeros if num >= 0]
    return sum(positivos) / len(positivos) if positivos else 0

numeros = list(map(int, input('Digite uma lista de números separados por espaço: ').split()))
print('A média dos números positivos é:', media(numeros))
