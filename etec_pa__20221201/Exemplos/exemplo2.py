matriz = []
qt_linha = 3
qt_col = 2

for i in range(0, qt_linha, 1):
    linha = []
    print('digite o nome da sua cidade')
    for j in range(0, qt_col, 1):
        valor = input()
        linha.append(valor)
    matriz.append(linha[:])
print('escolha uma cidade')
cidade = input()
for i in range(0, qt_linha, 1):
    if matriz[i][1] == cidade:
        print("nome:",matriz[i][0])

print(matriz[:])