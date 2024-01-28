def palindromo_recursivo(palavra, inicio=0, fim=None):
    if fim is None:
        fim = len(palavra) - 1
    if inicio >= fim:
        return True
    else:
        return palavra[inicio] == palavra[fim] and palindromo_recursivo(palavra, inicio + 1, fim - 1)

palavra = input('Digite uma palavra: ')
if palindromo_recursivo(palavra):
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')
