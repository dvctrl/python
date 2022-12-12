matrizA = []
matrizB = []


qtLinhas = 3
qtColunas = 2

for i in range(0,qtLinhas,1):
    linhaA = [] 
    for j in range(0,qtColunas, 1):
        linhaA.append((int(input('insira o valor para a linha da matrizA -> '))))
    matrizA.append(linhaA[:])
    
for i in range(0,qtLinhas,1):
    linhaB = [] 
    for j in range(0,qtColunas, 1):
        linhaB.append((int(input('insira o valor para a linha da matrizB -> '))))
    matrizB.append(linhaB[:])

def somarMatrizes(matrizA,matrizB):
    if(len(matrizA)!=len(matrizB) or len(matrizA[0])!=len(matrizB[0])):
        return None
    matrizC = []
    for i in range(len(matrizA)):
        matrizC.append([])
        for j in range(len(matrizA[0])):
            matrizC[i].append(matrizA[i][j] + matrizB[i][j])
    return matrizC

soma = somarMatrizes(matrizA, matrizB) # soma e o nosso retorno, result
if soma is not None:
    print (f'o valor da primeira matriz {matrizA}')
    print (f'o valor da segunda matriz {matrizB}')
    print (f'o valor da segunda matriz {soma}')

else:
    print('Matrizes devem conter o mesmo numero de linhas e colunas')

