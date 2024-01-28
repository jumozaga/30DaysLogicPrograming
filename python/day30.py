def maior_elemento(matriz):
    return max(max(linha) for linha in matriz)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('O maior elemento na matriz é:', maior_elemento(matriz))
