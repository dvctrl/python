x = int(input("digite o primeiro numero:"))
y = int(input("digite o segundo numero:"))
z = int(input("digite o terceiro numero:"))

if x < y:
        if x < z:
                r = x + 5
                print("o resultado de x.1 ",r)
        else:
                r = z + 5
                print("o resultado de z.1 ",r)
else:
        if y < z:
                r = y + 5
                print("o resultado de y.2 ",r)
        else:
                r = z + 5
                print("o resultado de z.2 ",r)
                
