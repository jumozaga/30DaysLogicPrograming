def palindromo(palavra):
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra: ')
if palindromo(palavra):
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')
