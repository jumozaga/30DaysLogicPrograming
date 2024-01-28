def transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def eh_simetrica(matriz):
    return matriz == transposta(matriz)

matriz = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print('A matriz é simétrica:', eh_simetrica(matriz))
