import random
while True:
       a = random.randint(0,20)
       b = random.randint(0,20)
       c = random.randint(0,20)
       d = random.randint(0,20)

       r1 = a + b 
       r2 = c - d
       r = r1 + r2

       if r > 10:
              print("Resultado maior que dez! Confira o resultado: ", r)
       else:
              print("Resultado menor/igual que dez! Confira o resultado: ", r)

       print("__________________________")