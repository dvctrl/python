numeros = []

for i in range(0,15,1):
    numeros.append(int(input('insira um numero inteiro aqui:')))
    print(numeros[:])
print('valor final do seu array é: ',sum(numeros))
