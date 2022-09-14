import random

x = random.randint(0, 100)
y = random.randint(0, 100)

print('valor de x é: ', x)
print('valor de y é: ', y)
if x < y:
        r = x + 5
        if r > y:
                print("valor final r(x) 1.1 é: ", r)
        else:
                print("valor de y 1.2 é: ", y)
else:
        r = y + 5
        if r > x:
                print("valor de r(y) 2.1 é: ", r)
        else:
                print("valor de x 2.2 é: ", x)
                
