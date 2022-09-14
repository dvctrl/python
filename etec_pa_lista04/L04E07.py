import random
while True:
       x = random.randint(0,100)
       y = random.randint(0,100)
       z = random.randint(0,100)

       if x > y:
              if z < y:
                     print("1.1 ", z)
                     print("1.2 ", y)
                     print("1.3 ", x)
              else:
                     if z > x:
                            print("2.1 ", y)
                            print("2.2 ", x)
                            print("2.3 ", z)
                     else:
                            print("3.1 ", y)
                            print("3.2 ", z)
                            print("3.2 ", x)
       else:
              if z < x:
                     print("4.1 ", z)  
                     print("4.2 ", x)
                     print("4.3 ", y)
              else:
                     if z > y:
                            print("5.1 ", x)  
                            print("5.2 ", y)
                            print("5.3 ", z)
                     else:
                            print("6.1 ", x)  
                            print("6.2 ", z)
                            print("6.3 ", y)
       print("______________________________")