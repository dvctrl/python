import random

while True:
    n1 = random.randint(1,20)
    n2 = random.randint(1,10)
    
    if n1 > 10:
        if n2 < 5:
                print('1.1',n1)
                print('1.2',n2)
        else:
                print('2.1',n1)
    else:
        if n2 < 5:
                print('3.1',n2)
        else:
                print("4.1 valores não atendem os parametros")
    
    break
