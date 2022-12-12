#11% desconto de renda
#8% inss 
#5% sindicato

#valor original
salario = float(input("Informe o seu salario bruto: "))

imposto = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
desconto = imposto + inss + sindicato
liquido = salario - desconto


print("Salario bruto R$:          ", salario)
print("Desconto IR R$:            ", imposto)
print("Desconto inss R$:          ", inss)
print("Desconto sindicato R$:     ", sindicato)
print("O seu valor salário liquido é de R$", liquido)
