import random
while True:
       x = random.randint(0,20)
       y = random.randint(0,20)

       if x > y:
              y = y * 10
              x = x / 2
       else:
              x = x * 10
              y = y / 2

       r = int(x + y)

       if r & 1:
              print("O valor é impar: ", r)
       else:
              print("O valor é par: ", r)

              
       break
print("______________________________")