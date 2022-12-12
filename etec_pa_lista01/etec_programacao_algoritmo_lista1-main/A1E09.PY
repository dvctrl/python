f = (int(input("Informe o valor da temperatura em Fahrenheit: ")))
c = float(5 * ((f-32) / 9))
c = "{:.2f}".format(c)
print("A  conversão da temperatura é: ", c,"ºC")