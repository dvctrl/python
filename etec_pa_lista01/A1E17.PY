#variaveis
largura = int(input("Informe a largura: "))
comprimento = int(input("Informe a comprimento: "))
area = largura * comprimento
litrosg = 18
litrosp = 3.6
cobertura = 6
tamanho = input("Informe o tamanho da lata para comprar: tamanho P ou G: ")

if area > cobertura and tamanho == 'g': 
        metros = area * cobertura
        totallatas = metros / litrosg
        valor = totallatas * 80
        print("Area total é" ,area, "m²")
        print("A tinta ira cobrir uma area total de " ,metros, "m")
        print("O total de latas necessarias será de: ", '{:.0f}'.format(totallatas), "ao todo.")
        print("O valor final da compra é de: R$", '{:.2f}'.format(valor))

elif area > cobertura and tamanho == 'p':
        metros = area * cobertura
        totallatas = metros / litrosp
        valor = totallatas * 25
        print("Area total é" ,area, "m²")
        print("A tinta ira cobrir uma area total de " ,metros, "m²")
        print("O total de latas necessarias será de: ", '{:.0f}'.format(totallatas), "ao todo.")
        print("O valor final da compra é de: R$", '{:.2f}'.format(valor))

else:
    print("valor invalido, digite novamente")
    
