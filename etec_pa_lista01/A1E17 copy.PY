cobertura = 6
comprimento = 0
largura = 0

litro = {
        'pequeno': 3.6,
        'grande' : 18,
        'misto'  : 18 + 3.6 
}
valores = {
        'pequeno' : 25,
        'grande'  : 80,
        'misto'   : 80 + 25  
}


while True:
        comprimento = int(input("Informe o comprimento: "))
        largura     = int(input("Informe a largura: "))
       
        area = comprimento * largura
        metros = area * cobertura
        latastt = metros / litro['grande']
        galaott = metros / litro['pequeno']
        mistott = metros / litro['misto']

        

        pergunta = input("Informe o tamanho da lata que deseja - Unidades 'Grande', 'Pequena' ou 'Misto': ")
        if pergunta == 'grande':
                print("--Você escolheu o tamanho: ",litro['grande'],"litros")
                print("--O valor uni. lata R$: ", '{:.2f}'.format(valores['grande']))
                print("--a area total é de: ", area,"m²") 
                print("--Sugestão de compras: ", '{:.0f}'.format(latastt),"unidades")   
        elif pergunta == 'pequeno':
                print("--Você escolheu o tamanho: ",litro['pequeno'],"litros")
                print("--O valor uni. lata R$:", '{:.2f}'.format(valores['pequeno']))
                print("--a area total é de: ", area,"m²") 
                print("--Sugestão de compras: ", '{:.0f}'.format(galaott),"unidades")   
        elif pergunta == 'misto':
                        print("--Você escolheu o tamanho: ",(litro['misto']*0.10),"litros")
                        print("--O valor soma da lata e galão R$:", '{:.2f}'.format(valores['misto']))
                        print("--a area total é de: ", area,"m²") 
                        print("--a area de cobertura é de: ", metros,"m²") 
                        print("--Sugestão de compras: ", '{:.0f}'.format(mistott),"unidades")
                        print("Valor final da compra ------------- R$", round(mistott * valores['misto'],6))   

        else:
                print("Valor invalido, informe um valor valido")
        
        

