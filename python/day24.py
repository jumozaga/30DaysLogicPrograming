def eh_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j and matriz[i][j] != 0:
                return False
    return True

matriz = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
print('A matriz é diagonal:', eh_diagonal(matriz))
