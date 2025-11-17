def warshall(matriz):
    n = len(matriz)
    alcan = [fila[:] for fila in matriz]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcan[i][j] = alcan[i][j] or (alcan[i][k] and alcan[k][j])
    return alcan
matriz_binaria = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

resultado = warshall(matriz_binaria)
print("Warshall:")
for fila in resultado:
    print(fila)
