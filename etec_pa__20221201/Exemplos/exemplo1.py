matriz = []
qt_linha = 3
qt_col = 2

for i in range(0, qt_linha, 1):
    linha = []
    for j in range(0, qt_col, 1):
        print('digite o valor do nome e sobrenome do caboclo')
        valor = input()
        linha.append(valor)
    matriz.append(linha[:])
print(matriz)