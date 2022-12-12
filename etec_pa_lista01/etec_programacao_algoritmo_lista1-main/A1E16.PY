#variaveis
largura = int(input("Informe a largura: "))
comprimento = int(input("Informe a comprimento: "))
area = largura * comprimento
litros = 18
cobertura = 3

if area > cobertura: 
        metros = area * cobertura
        totallatas = metros / litros
        valor = totallatas * 80
        print("Area total é" ,area, "m²")
        print("A tinta ira cobrir uma area total de " ,metros, "m")
        print("O total de latas necessarias será de: ", '{:.0f}'.format(totallatas), "ao todo.")
        print("O valor final da compra é de: R$", '{:.2f}'.format(valor))
else:
    print("valor invalido, digite novamente")


