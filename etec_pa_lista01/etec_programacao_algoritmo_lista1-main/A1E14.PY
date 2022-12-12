excesso = 50
multa = 4.00
pesopeixe = int(input("Insira quantos quilos de peixe: "))

if pesopeixe > excesso:
        print("vocÊ inseriu ", pesopeixe,"kg")
        print("Você excedeu ", (pesopeixe - excesso), "kg")
        print("Você deverá pagar R$",'{:.2f}'.format(multa*(pesopeixe - excesso)))
elif pesopeixe < excesso:
        print("O peso total do peixe foi de: ", '{:.2f}'.format(pesopeixe), "kg")

