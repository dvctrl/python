from xmlrpc.client import boolean


h = float(input("Insira sua altura: "))
s = input("Insira seu sexo: ")

if s == 'homem' :
    imc =  (72.7*h) - 58
    print("Seu IMC é: ", '{:.2f}'.format(imc))
elif s == 'mulher' : 
    imc =  (62.1*h) - 44.7
    print("Seu IMC é: ", '{:.2f}'.format(imc))
else:
    print("insira uma informação valida")
