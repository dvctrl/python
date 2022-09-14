import random

n1 = random.randint(0,20)
n2 = random.randint(0,20)
n3 = random.randint(0,20)

print("n1 é: ", n1)
print("n2 é: ", n2)
print("n3 é: ", n3)
print("-------------")

if n1 > n2:
    if n2 < n3:
        if n3 > n1:
            while n1 < n3:
                print("1.1 O intervalo entre ambos é de ",n1)
                n1 = n1 + 1
        else:
            while n3 < n1:
                print("1.2 O intervalo entre ambos é de ",n3)
                n3 = n3 + 1
    else:
        while n2 < n1:
            print("1.3 O intervalo entre ambos é de ",n2)
            n2 = n2 + 1
else:
    if n1 < n3:
        if n3 > n2:
            while n2 < n3:
                print("2.1 O intervalo entre ambos é de ",n2)
                n2 = n2 + 1
        else:
            while n3 < n2:
                print("2.2 O intervalo entre ambos é de ",n3)
                n3 = n3 + 1
    else:
        while n1 < n2:
            print("2.3 O intervalo entre ambos é de ",n1)
            n1 = n1 + 1
            
print("-------------")
