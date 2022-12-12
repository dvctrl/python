import string

alfa = list(string.ascii_lowercase)
mensagem = list(input('insira a mensagem -> '))
chave = int(input('insira quantas chaves serão necessarias para criptorafia -> '))
cripto = []

#criptografia
for letra in mensagem:
    indice = ord(letra)
    novoIndice = (indice + chave)
    if novoIndice > 122:
        novoIndice = (indice + chave)-len(alfa)
    cripto.append(chr(novoIndice))
print(f'--MENSAGEM CRIPGRTAFADA É -- {cripto} ---')

    

'''
- links de referencia de conteúdo 

- https://github.com/python-cafe/exemplos/blob/master/criptografia/cripto.py
- https://en.wikipedia.org/wiki/List_of_Unicode_characters
- https://www.programiz.com/python-programming/methods/built-in/chr
'''



    